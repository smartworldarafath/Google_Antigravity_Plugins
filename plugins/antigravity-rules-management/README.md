# Antigravity Rules Management

> Google Antigravity Plugin

# AGENTS.md Management Plugin

Tools to maintain and improve AGENTS.md files - audit quality, capture session learnings, and keep project memory current.

## What It Does

Two complementary tools for different purposes:

| | claude-md-improver (skill) | /revise-claude-md (command) |
|---|---|---|
| **Purpose** | Keep AGENTS.md aligned with codebase | Capture session learnings |
| **Triggered by** | Codebase changes | End of session |
| **Use when** | Periodic maintenance | Session revealed missing context |

## Usage

### Skill: claude-md-improver

Audits AGENTS.md files against current codebase state:

```
"audit my AGENTS.md files"
"check if my AGENTS.md is up to date"
```

<img src="claude-md-improver-example.png" alt="AGENTS.md improver showing quality scores and recommended updates" width="600">

### Command: /revise-claude-md

Captures learnings from the current session:

```
/revise-claude-md
```

<img src="revise-claude-md-example.png" alt="Revise command capturing session learnings into AGENTS.md" width="600">

## Author

Isabella He (isabella@anthropic.com)
