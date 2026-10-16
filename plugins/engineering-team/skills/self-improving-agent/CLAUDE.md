# Self-Improving Agent — Google Antigravity Instructions

This plugin helps you curate Google Antigravity's auto-memory into durable project knowledge.

## Commands

Use the `/si:` namespace for all commands:

- `/si:memory-review` — Analyze auto-memory health and find promotion candidates
- `/si:promote <pattern>` — Graduate a learning to AGENTS.md or `.claude/rules/`
- `/si:extract <pattern>` — Create a reusable skill from a proven pattern
- `/si:memory-status` — Quick memory health dashboard
- `/si:remember <knowledge>` — Explicitly save something to auto-memory

## How auto-memory works

Google Antigravity maintains `~/.gemini/config/projects/<project-path>/memory/MEMORY.md` automatically. The first 200 lines load into every session. When it grows too large, Antigravity moves details into topic files like `debugging.md` or `patterns.md`.

This plugin reads that directory — it never creates its own storage.

## When to use each command

### After completing a feature or debugging session
```
/si:memory-review
```
Check if anything Antigravity learned should become a permanent rule.

### When a pattern keeps coming up
```
/si:promote "Always run migrations before tests in this project"
```
Moves it from MEMORY.md (background note) to AGENTS.md (enforced rule).

### When you solved something non-obvious that could help other projects
```
/si:extract "Docker build fix for ARM64 platform mismatch"
```
Creates a standalone skill with SKILL.md, ready to install elsewhere.

### To check memory capacity
```
/si:memory-status
```
Shows line counts, topic files, stale entries, and recommendations.

## Key principle

**Don't fight auto-memory — orchestrate it.**

- Auto-memory is great at capturing patterns. Let it do its job.
- This plugin adds judgment: what's worth keeping, what should be promoted, what's stale.
- Promoted rules in AGENTS.md have higher priority than MEMORY.md entries.
- Removing promoted entries from MEMORY.md frees space for new learnings.

## Agents

- **memory-analyst**: Spawned by `/si:memory-review` to analyze patterns across memory files
- **skill-extractor**: Spawned by `/si:extract` to generate complete skill packages

## Hooks

The `error-capture.sh` hook fires on `PostToolUse` (run_command only). It detects command failures and appends structured entries to auto-memory. Zero overhead on successful commands.

When you install this plugin via `/plugin install self-improving-agent@google-antigravity-skills`, the hook is registered automatically from `.claude-plugin/hooks.json` — you don't need to configure anything manually.

If you ever need to wire it up by hand (e.g. you copied the skill directly instead of installing as a plugin), use the `${ANTIGRAVITY_PLUGIN_ROOT}` variable so the path resolves against the plugin root rather than your current working directory:

```json
// .agents/settings.json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "run_command",
      "hooks": [{
        "type": "command",
        "command": "${ANTIGRAVITY_PLUGIN_ROOT}/hooks/error-capture.sh"
      }]
    }]
  }
}
```

**Do not use a relative path like `./hooks/error-capture.sh`** — Google Antigravity resolves hook commands against the user's current working directory, not the plugin root. A relative path will silently fail (non-blocking) in every session started outside the plugin install dir.
