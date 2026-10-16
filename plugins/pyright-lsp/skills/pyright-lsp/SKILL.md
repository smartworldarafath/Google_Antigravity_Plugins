---
name: pyright-lsp
description: Pyright static type checker and language server for Python projects in Google Antigravity.
---

# Python Language Server (Pyright)

Language Server Protocol integration for Google Antigravity. Provides code intelligence, diagnostics, go-to-definition, find-references, and type inspection.

## Supported Extensions
`.py`, `.pyi`

## Prerequisites & Installation
Ensure `pyright-langserver` is installed and available on your system PATH:

npm install -g pyright  OR  pip install pyright

## Antigravity Workflow
1. When editing or analyzing files matching .py, .pyi, the agent can invoke `pyright-langserver` to verify syntax and type soundness.
2. Run language diagnostics via `run_command`:
   ```bash
   pyright-langserver --version
   ```
3. Use language intelligence to trace symbol definitions and inspect API boundaries with zero ambiguity.
