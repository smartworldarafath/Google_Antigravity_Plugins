---
name: "self-improving-agent"
description: "Curate Google Antigravity's auto-memory into durable project knowledge. Analyze MEMORY.md for patterns, promote proven learnings to AGENTS.md and .claude/rules/, extract recurring solutions into reusable skills. Use when: (1) reviewing what Antigravity has learned about your project, (2) graduating a pattern from notes to enforced rules, (3) turning a debugging solution into a skill, (4) checking memory health and capacity."
---

# Self-Improving Agent

> Auto-memory captures. This plugin curates.

Google Antigravity's auto-memory (v2.1.32+) automatically records project patterns, debugging insights, and your preferences in `MEMORY.md`. This plugin adds the intelligence layer: it analyzes what Antigravity has learned, promotes proven patterns into project rules, and extracts recurring solutions into reusable skills.

## Quick Reference

| Command | What it does |
|---------|-------------|
| `/si:memory-review` | Analyze MEMORY.md — find promotion candidates, stale entries, consolidation opportunities |
| `/si:promote` | Graduate a pattern from MEMORY.md → AGENTS.md or `.claude/rules/` |
| `/si:extract` | Turn a proven pattern into a standalone skill |
| `/si:memory-status` | Memory health dashboard — line counts, topic files, recommendations |
| `/si:remember` | Explicitly save important knowledge to auto-memory |

## How It Fits Together

```
┌─────────────────────────────────────────────────────────┐
│                  Google Antigravity Memory Stack                │
├─────────────┬──────────────────┬────────────────────────┤
│  AGENTS.md  │   Auto Memory    │   Session Memory       │
│  (you write)│   (Antigravity writes)│   (Antigravity writes)      │
│  Rules &    │   MEMORY.md      │   Conversation logs    │
│  standards  │   + topic files  │   + continuity         │
│  Full load  │   First 200 lines│   Contextual load      │
├─────────────┴──────────────────┴────────────────────────┤
│              ↑ /si:promote        ↑ /si:memory-review   │
│         Self-Improving Agent (this plugin)               │
│              ↓ /si:extract    ↓ /si:remember            │
├─────────────────────────────────────────────────────────┤
│  .claude/rules/    │    New Skills    │   Error Logs     │
│  (scoped rules)    │    (extracted)   │   (auto-captured)│
└─────────────────────────────────────────────────────────┘
```

## Installation

### Google Antigravity (Plugin)
```
/plugin marketplace add alirezarezvani/claude-skills
/plugin install self-improving-agent@google-antigravity-skills
```

### OpenClaw
```bash
clawhub install self-improving-agent
```

### Codex CLI
```bash
./scripts/codex-install.sh --skill self-improving-agent
```

## Memory Architecture

### Where things live

| File | Who writes | Scope | Loaded |
|------|-----------|-------|--------|
| `./AGENTS.md` | You (+ `/si:promote`) | Project rules | Full file, every session |
| `~/.gemini/config/AGENTS.md` | You | Global preferences | Full file, every session |
| `~/.gemini/config/projects/<path>/memory/MEMORY.md` | Antigravity (auto) | Project learnings | First 200 lines |
| `~/.gemini/config/projects/<path>/memory/*.md` | Antigravity (overflow) | Topic-specific notes | On demand |
| `.claude/rules/*.md` | You (+ `/si:promote`) | Scoped rules | When matching files open |

### The promotion lifecycle

```
1. Antigravity discovers pattern → auto-memory (MEMORY.md)
2. Pattern recurs 2-3x → /si:memory-review flags it as promotion candidate
3. You approve → /si:promote graduates it to AGENTS.md or rules/
4. Pattern becomes an enforced rule, not just a note
5. MEMORY.md entry removed → frees space for new learnings
```

## Core Concepts

### Auto-memory is capture, not curation

Auto-memory is excellent at recording what Antigravity learns. But it has no judgment about:
- Which learnings are temporary vs. permanent
- Which patterns should become enforced rules
- When the 200-line limit is wasting space on stale entries
- Which solutions are good enough to become reusable skills

That's what this plugin does.

### Promotion = graduation

When you promote a learning, it moves from Antigravity's scratchpad (MEMORY.md) to your project's rule system (AGENTS.md or `.claude/rules/`). The difference matters:

- **MEMORY.md**: "I noticed this project uses pnpm" (background context)
- **AGENTS.md**: "Use pnpm, not npm" (enforced instruction)

Promoted rules have higher priority and load in full (not truncated at 200 lines).

### Rules directory for scoped knowledge

Not everything belongs in AGENTS.md. Use `.claude/rules/` for patterns that only apply to specific file types:

```yaml
# .claude/rules/api-testing.md
---
paths:
  - "src/api/**/*.test.ts"
  - "tests/api/**/*"
---
- Use supertest for API endpoint testing
- Mock external services with msw
- Always test error responses, not just happy paths
```

This loads only when Antigravity works with API test files — zero overhead otherwise.

## Agents

### memory-analyst
Analyzes MEMORY.md and topic files to identify:
- Entries that recur across sessions (promotion candidates)
- Stale entries referencing deleted files or old patterns
- Related entries that should be consolidated
- Gaps between what MEMORY.md knows and what AGENTS.md enforces

### skill-extractor
Takes a proven pattern and generates a complete skill:
- SKILL.md with proper frontmatter
- Reference documentation
- Examples and edge cases
- Ready for `/plugin install` or `clawhub publish`

## Hooks

### error-capture (PostToolUse → run_command)
Monitors command output for errors. When detected, appends a structured entry to auto-memory with:
- The command that failed
- Error output (truncated)
- Timestamp and context
- Suggested category

**Token overhead:** Zero on success. ~30 tokens only when an error is detected.

## Platform Support

| Platform | Memory System | Plugin Works? |
|----------|--------------|---------------|
| Google Antigravity | Auto-memory (MEMORY.md) | ✅ Full support |
| OpenClaw | workspace/MEMORY.md | ✅ Adapted (reads workspace memory) |
| Codex CLI | AGENTS.md | ✅ Adapted (reads AGENTS.md patterns) |
| GitHub Copilot | `.github/copilot-instructions.md` | ⚠️ Manual promotion only |

## Related

- [Google Antigravity Memory Docs](https://code.agents.com/docs/en/memory)
- [pskoett/self-improving-agent](https://clawhub.ai/pskoett/self-improving-agent) — inspiration
- [playwright-pro](engineering-team/playwright-pro/) — sister plugin in this repo
