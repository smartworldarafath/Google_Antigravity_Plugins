"""A commit still under review is not sent through a second review."""
import contextlib
import json
import os
import subprocess
import sys
import time

import pytest

from conftest import (
    HOOK_SCRIPT, bash_payload, commit_file, git, make_repo, metrics_of, run_hook,
)

import diffstate

pytest.importorskip("fcntl")

_HOLD = (
    "import fcntl, os, sys, time\n"
    "fd = os.open(sys.argv[1], os.O_RDWR | os.O_CREAT, 0o600)\n"
    "fcntl.flock(fd, fcntl.LOCK_EX)\n"
    "print('held', flush=True)\n"
    "time.sleep(float(sys.argv[2]))\n"
)


@contextlib.contextmanager
def _held_by_another_review(repo, sha, seconds=60):
    """A marker on `sha` that a live process holds, as a running review does."""
    marker = repo / ".git" / f"sg-inflight-{sha}"
    p = subprocess.Popen([sys.executable, "-c", _HOLD, str(marker), str(seconds)],
                         stdout=subprocess.PIPE, text=True)
    try:
        assert p.stdout.readline().strip() == "held"
        yield marker
    finally:
        p.kill()
        p.wait()
        p.stdout.close()


@contextlib.contextmanager
def _hook_in_background(payload, env):
    p = subprocess.Popen(
        [sys.executable, str(HOOK_SCRIPT)], stdin=subprocess.PIPE,
        stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True, env=env,
    )
    try:
        p.stdin.write(json.dumps(payload))
        p.stdin.close()
        yield p
    finally:
        if p.poll() is None:
            p.kill()
        p.wait()
        p.stdout.close()


def _repo_with_remote(tmp_path):
    repo = make_repo(tmp_path / "repo", {"app.py": "print('hi')\n"})
    remote = tmp_path / "remote.git"
    git(tmp_path, "init", "-q", "--bare", str(remote))
    git(repo, "remote", "add", "origin", str(remote))
    git(repo, "push", "-q", "-u", "origin", "main")
    return repo, remote


def _markers(repo):
    return [n for n in os.listdir(repo / ".git") if n.startswith("sg-inflight-")]


def _wait_until(cond, what, timeout=20):
    end = time.time() + timeout
    while time.time() < end:
        if cond():
            return
        time.sleep(0.05)
    raise AssertionError(f"timed out waiting for {what}")


def _reviews(stub_api):
    return [c for c in stub_api.calls if c.endswith("/v1/messages")]


def _commit_and_push(repo, remote):
    base = git(repo, "rev-parse", "HEAD").strip()
    sha, commit_out = commit_file(repo, "handlers.py", "def h(x):\n    return x\n")
    git(repo, "push", "-q", "origin", "main")
    push_out = f"To {remote}\n   {base[:7]}..{sha[:7]}  main -> main\n"
    return base, sha, commit_out, push_out


def test_push_right_after_commit_runs_one_review(tmp_path, hook_env, stub_api):
    repo, remote = _repo_with_remote(tmp_path)
    base, sha, commit_out, push_out = _commit_and_push(repo, remote)
    stub_api.delay = 6
    with _hook_in_background(bash_payload(repo, "git commit -m change", commit_out),
                             hook_env) as commit:
        _wait_until(lambda: _markers(repo), "the commit review's marker")
        rc, so, _ = run_hook(bash_payload(repo, "git push origin main", push_out), hook_env)
        commit.wait(timeout=60)

    m = metrics_of(so)
    assert rc == 0 and m["push_sweep"] is True
    assert m["pushed"] == 1 and m["unreviewed"] == 0
    assert m.get("inflight_wait_s", 0) >= 1
    assert len(_reviews(stub_api)) == 1
    assert sha in diffstate._load_reviewed_shas(str(repo))
    assert _markers(repo) == []


def test_push_reviews_commit_whose_review_died(tmp_path, hook_env, stub_api):
    repo, remote = _repo_with_remote(tmp_path)
    base, sha, _, push_out = _commit_and_push(repo, remote)
    with _held_by_another_review(repo, sha):
        pass  # killed: its marker file stays, its lock does not
    assert _markers(repo) == [f"sg-inflight-{sha}"]
    rc, so, _ = run_hook(bash_payload(repo, "git push origin main", push_out), hook_env)

    m = metrics_of(so)
    assert m["unreviewed"] == 1 and "inflight_wait_s" not in m
    assert len(_reviews(stub_api)) == 1
    assert _markers(repo) == []


def test_push_reviews_commit_whose_review_ended_without_a_verdict(tmp_path, hook_env, stub_api):
    repo, remote = _repo_with_remote(tmp_path)
    base, sha, _, push_out = _commit_and_push(repo, remote)
    with _held_by_another_review(repo, sha, seconds=3):
        rc, so, _ = run_hook(bash_payload(repo, "git push origin main", push_out), hook_env)

    m = metrics_of(so)
    assert m["unreviewed"] == 1
    assert m["files_reviewed"] == 1 and len(_reviews(stub_api)) == 1
    assert sha in diffstate._load_reviewed_shas(str(repo))


def test_push_stops_waiting_after_the_limit(tmp_path, hook_env, stub_api):
    repo, remote = _repo_with_remote(tmp_path)
    base, sha, _, push_out = _commit_and_push(repo, remote)
    env = {**hook_env, "SG_INFLIGHT_WAIT_S": "2"}
    with _held_by_another_review(repo, sha):
        rc, so, _ = run_hook(bash_payload(repo, "git push origin main", push_out), env)

    m = metrics_of(so)
    assert m["unreviewed"] == 1 and m["inflight_wait_s"] >= 2
    assert len(_reviews(stub_api)) == 1


def test_push_does_not_wait_when_an_earlier_commit_needs_review_anyway(tmp_path, hook_env, stub_api):
    repo, remote = _repo_with_remote(tmp_path)
    base = git(repo, "rev-parse", "HEAD").strip()
    commit_file(repo, "outside.py", "def o(x):\n    return x\n")
    sha, _ = commit_file(repo, "handlers.py", "def h(x):\n    return x\n")
    git(repo, "push", "-q", "origin", "main")
    push_out = f"To {remote}\n   {base[:7]}..{sha[:7]}  main -> main\n"
    with _held_by_another_review(repo, sha):
        rc, so, _ = run_hook(bash_payload(repo, "git push origin main", push_out), hook_env)

    m = metrics_of(so)
    assert m["pushed"] == 2 and m["unreviewed"] == 2 and "inflight_wait_s" not in m
    assert m["files_reviewed"] == 2


def test_push_does_not_record_the_range_when_head_moves_during_the_wait(tmp_path, hook_env, stub_api):
    repo, remote = _repo_with_remote(tmp_path)
    base, sha, _, push_out = _commit_and_push(repo, remote)
    env = {**hook_env, "SG_INFLIGHT_WAIT_S": "10"}
    with _held_by_another_review(repo, sha):
        with _hook_in_background(bash_payload(repo, "git push origin main", push_out),
                                 env) as push:
            time.sleep(5)
            git(repo, "checkout", "-q", "-b", "elsewhere", base)
            so = push.stdout.read()
            push.wait(timeout=60)

    m = metrics_of(so)
    assert m["skip_reason"] == 44 and m.get("inflight_wait_s", 0) >= 1
    assert _reviews(stub_api) == []
    assert sha not in diffstate._load_reviewed_shas(str(repo))


def test_next_quiet_commit_leaves_a_running_review_its_commit(tmp_path, hook_env, stub_api):
    repo = make_repo(tmp_path / "repo", {"app.py": "print('hi')\n"})
    commit_file(repo, "a.py", "def a(x):\n    return x\n")
    stub_api.delay = 6
    with _hook_in_background(bash_payload(repo, "git commit -q -m a"), hook_env) as first:
        _wait_until(lambda: _markers(repo), "the first review's marker")
        commit_file(repo, "b.py", "def b(x):\n    return x\n")
        rc, so, _ = run_hook(bash_payload(repo, "git commit -q -m b"), hook_env)
        first.wait(timeout=60)

    m = metrics_of(so)
    assert m["sha_via_reflog"] is True and m["reflog_shas_n"] == 1
    assert m["files_reviewed"] == 1
    assert _markers(repo) == []


def test_marker_is_not_taken_from_a_live_review(tmp_path):
    repo = make_repo(tmp_path / "repo")
    sha = git(repo, "rev-parse", "HEAD").strip()
    with _held_by_another_review(repo, sha) as marker:
        diffstate._mark_inflight(str(repo), [sha])
        assert diffstate._inflight_held == {}
        assert diffstate._load_inflight_shas(str(repo), [sha]) == {sha}
    assert diffstate._load_inflight_shas(str(repo), [sha]) == set()
    assert marker.exists()  # fresh leftovers stay; old ones are removed
    old = time.time() - diffstate._INFLIGHT_GC_AGE_S - 5
    os.utime(marker, (old, old))
    diffstate._mark_inflight(str(repo), [])
    assert not marker.exists()


def test_no_marker_is_left_where_files_cannot_be_locked(tmp_path, monkeypatch):
    repo = make_repo(tmp_path / "repo")
    sha = git(repo, "rev-parse", "HEAD").strip()

    def no_locks(fd, exclusive):
        raise OSError(37, "No locks available")
    monkeypatch.setattr(diffstate, "_flock_nb", no_locks)
    diffstate._mark_inflight(str(repo), [sha])
    assert _markers(repo) == [] and diffstate._inflight_held == {}
    (repo / ".git" / f"sg-inflight-{sha}").write_text("")
    assert diffstate._load_inflight_shas(str(repo), [sha]) == set()


def test_own_marker_is_held_until_released(tmp_path):
    repo = make_repo(tmp_path / "repo")
    sha = git(repo, "rev-parse", "HEAD").strip()
    diffstate._mark_inflight(str(repo), [sha, "not-a-sha"])
    marker = repo / ".git" / f"sg-inflight-{sha}"
    try:
        assert _markers(repo) == [marker.name]
        assert diffstate._load_inflight_shas(str(repo), [sha]) == set()
        probe = (
            "import sys; sys.path.insert(0, sys.argv[1]); import diffstate; "
            "print(sorted(diffstate._load_inflight_shas(sys.argv[2], [sys.argv[3]])))"
        )
        seen = subprocess.run(
            [sys.executable, "-c", probe, os.path.dirname(diffstate.__file__), str(repo), sha],
            capture_output=True, text=True).stdout.strip()
        assert seen == str([sha])
        reviewed, waited = diffstate._reviewed_after_inflight(str(repo), [sha], 5)
        assert reviewed == set() and waited == 0.0
    finally:
        diffstate._release_inflight()
    assert not marker.exists()
