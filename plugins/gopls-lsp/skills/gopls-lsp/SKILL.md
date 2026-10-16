---
name: gopls-lsp
description: Go language server (gopls) integration for Google Antigravity, providing analysis, package navigation, and refactoring.
---

# Go Language Server (gopls)

Language Server Protocol integration for Google Antigravity. Provides code intelligence, diagnostics, go-to-definition, find-references, and type inspection.

## Supported Extensions
`.go`

## Prerequisites & Installation
Ensure `gopls` is installed and available on your system PATH:

go install golang.org/x/tools/gopls@latest

## Antigravity Workflow
1. When editing or analyzing files matching .go, the agent can invoke `gopls` to verify syntax and type soundness.
2. Run language diagnostics via `run_command`:
   ```bash
   gopls --version
   ```
3. Use language intelligence to trace symbol definitions and inspect API boundaries with zero ambiguity.
