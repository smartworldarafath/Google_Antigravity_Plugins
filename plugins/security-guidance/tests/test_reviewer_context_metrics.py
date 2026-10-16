"""The agentic reviewer reports, as counts only, how its view_file/run_command/run_command calls
went and whether the directory it ran in was still there."""
import json
import os
import shutil
import sys
import types

import pytest

import llm
import security_reminder_hook as hook


class _ToolUse:
    def __init__(self, id, name):
        self.id, self.name, self.input = id, name, {}


class _ToolResult:
    def __init__(self, tool_use_id, is_error=None):
        self.tool_use_id, self.is_error, self.content = tool_use_id, is_error, ""


@pytest.fixture
def sdk(monkeypatch, tmp_path):
    """Stand-in for claude_agent_sdk whose reviewer replays `script.messages`
    and then returns no findings. Like the SDK, it cannot start in a
    directory that does not exist."""
    script = types.SimpleNamespace(messages=[], before_result=lambda: None)

    class ClaudeAgentOptions:
        def __init__(self, **kwargs):
            self.kwargs = kwargs

    class AssistantMessage:
        def __init__(self, *content):
            self.content = list(content)

    class UserMessage:
        def __init__(self, content):
            self.content = content

    class ResultMessage:
        subtype, usage, total_cost_usd = "success", {}, 0.0
        structured_output = {"findings": []}

    async def query(prompt, options):
        if not os.path.isdir(options.kwargs["cwd"]):
            raise RuntimeError("Working directory does not exist")
        for m in script.messages:
            yield m
        script.before_result()
        yield ResultMessage()

    mod = types.ModuleType("claude_agent_sdk")
    mod.ClaudeAgentOptions, mod.ResultMessage, mod.query = ClaudeAgentOptions, ResultMessage, query
    mod.AssistantMessage = AssistantMessage
    monkeypatch.setitem(sys.modules, "claude_agent_sdk", mod)
    monkeypatch.setenv("SG_AGENTIC_CLI_PATH", "")
    monkeypatch.setenv("SECURITY_WARNINGS_STATE_DIR", str(tmp_path / "state"))
    for var in ("SG_AGENTIC_CONTEXT_DIR", "SG_AGENTIC_DEBUG_DIR", "SG_AGENTIC_MODEL"):
        monkeypatch.delenv(var, raising=False)
    script.assistant, script.user = AssistantMessage, UserMessage
    return script


def _review(repo):
    return llm.agentic_review(str(repo), [("a.py", "+x = 1\n")], ["a.py"])[2]


class TestAgenticReview:
    def test_clean_review_counts_calls_and_no_errors(self, sdk, tmp_path):
        sdk.messages = [sdk.assistant(_ToolUse("t1", "view_file")),
                        sdk.user([_ToolResult("t1", is_error=False)])]
        m = _review(tmp_path)
        assert m["rv_tool_calls"] == 1
        assert "rv_tool_err" not in m and "rv_cwd_gone" not in m

    def test_errored_file_tool_results_are_counted(self, sdk, tmp_path):
        sdk.messages = [
            sdk.assistant(_ToolUse("t1", "view_file")),
            sdk.user([_ToolResult("t1", is_error=True)]),
            sdk.assistant(_ToolUse("t2", "run_command"), _ToolUse("t3", "run_command")),
            sdk.user([_ToolResult("t2", is_error=True), _ToolResult("t3", is_error=False)]),
            sdk.user("plain text"),
        ]
        m = _review(tmp_path)
        assert (m["rv_tool_calls"], m["rv_tool_err"]) == (3, 2)

    def test_other_tools_are_not_counted(self, sdk, tmp_path):
        # A rejected structured-output attempt or a denied tool is not a
        # sign of missing context.
        sdk.messages = [
            sdk.assistant(_ToolUse("t1", "StructuredOutput"), _ToolUse("t2", "run_command")),
            sdk.user([_ToolResult("t1", is_error=True), _ToolResult("t2", is_error=True)]),
        ]
        m = _review(tmp_path)
        assert "rv_tool_calls" not in m and "rv_tool_err" not in m

    def test_directory_missing_before_the_review(self, sdk, tmp_path):
        m = _review(tmp_path / "removed")
        assert m["agentic_fallback"].startswith("investigate:")
        assert m["rv_cwd_gone"] == 1

    def test_directory_removed_during_the_review(self, sdk, tmp_path):
        repo = tmp_path / "wt"
        repo.mkdir()
        sdk.messages = [sdk.assistant(_ToolUse("t1", "view_file")),
                        sdk.user([_ToolResult("t1", is_error=True)])]
        sdk.before_result = lambda: shutil.rmtree(repo)
        m = _review(repo)
        assert (m["rv_cwd_gone"], m["rv_tool_err"]) == (2, 1)

    def test_counts_survive_a_failed_investigate(self, sdk, tmp_path, monkeypatch):
        async def query(prompt, options):
            yield sdk.assistant(_ToolUse("t1", "view_file"))
            yield sdk.user([_ToolResult("t1", is_error=True)])
            raise RuntimeError("inner CLI exited")

        monkeypatch.setattr(sys.modules["claude_agent_sdk"], "query", query)
        m = _review(tmp_path)
        assert m["agentic_fallback"].startswith("investigate:")
        assert (m["rv_tool_calls"], m["rv_tool_err"]) == (1, 1)


class TestEmittedRow:
    @pytest.fixture(autouse=True)
    def _clean_tail(self, monkeypatch):
        monkeypatch.setattr(hook, "_TAIL_METRICS", {})

    def _row(self, capsys):
        return json.loads(capsys.readouterr().out)["metrics"]

    def test_context_keys_come_last_in_priority_order(self, capsys):
        hook._note_reviewer_context(
            {"rv_tool_calls": 4, "rv_tool_err": 2, "rv_cwd_gone": 2, "investigate_turns": 5})
        hook.emit_metrics({"vulns_found": 0, "review_ms": 10})
        keys = list(self._row(capsys))
        assert keys[-5:] == ["vulns_found", "review_ms", "rv_cwd_gone", "rv_tool_err", "rv_tool_calls"]

    def test_zero_or_absent_keys_are_left_out(self, capsys):
        hook._note_reviewer_context({"rv_tool_calls": 3, "rv_tool_err": 0})
        hook.emit_metrics({"vulns_found": 0})
        row = self._row(capsys)
        assert row["rv_tool_calls"] == 3
        assert "rv_tool_err" not in row and "rv_cwd_gone" not in row

    def test_failed_review_row_keeps_vulns_found_ahead_of_context_keys(self, capsys):
        hook._note_reviewer_context({"rv_cwd_gone": 1})
        with pytest.raises(SystemExit):
            hook._exit_review_failed("Commit", "s1", {"files_reviewed": 1}, 500)
        keys = list(self._row(capsys))
        assert keys.index("vulns_found") < keys.index("rv_cwd_gone") == len(keys) - 1


class TestRace:
    def test_context_kept_when_the_fallback_result_replaces_a_failed_agentic_run(self, monkeypatch):
        import time

        def agentic(*a):
            time.sleep(0.3)  # fails after the fallback has started
            return None, [], {"agentic_fallback": "investigate:RuntimeError",
                              "rv_cwd_gone": 2, "rv_tool_err": 4, "rv_tool_calls": 5}

        monkeypatch.setenv("SG_AGENTIC_RACE_DELAY_S", "0")
        monkeypatch.delenv("SG_AGENTIC_NO_RACE", raising=False)
        monkeypatch.setattr(hook, "agentic_review", agentic)

        def single_shot(*a, **k):
            time.sleep(0.6)
            return None, []

        monkeypatch.setattr(hook, "analyze_code_security", single_shot)
        monkeypatch.setattr(hook.llm, "last_review_failed", lambda: False)
        _, _, m = hook._agentic_review_with_race("/nonexistent", [("a.py", "+x")], ["a.py"], [])
        assert m["race_winner"] == 2 and m["agentic"] is False
        assert (m["rv_cwd_gone"], m["rv_tool_err"], m["rv_tool_calls"]) == (2, 4, 5)
