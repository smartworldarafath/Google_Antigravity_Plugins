---
name: php-lsp
description: PHP language server integration for PHP and Laravel projects in Google Antigravity.
---

# PHP Language Server (Intelephense)

Language Server Protocol integration for Google Antigravity. Provides code intelligence, diagnostics, go-to-definition, find-references, and type inspection.

## Supported Extensions
`.php`

## Prerequisites & Installation
Ensure `intelephense` is installed and available on your system PATH:

npm install -g intelephense

## Antigravity Workflow
1. When editing or analyzing files matching .php, the agent can invoke `intelephense` to verify syntax and type soundness.
2. Run language diagnostics via `run_command`:
   ```bash
   intelephense --version
   ```
3. Use language intelligence to trace symbol definitions and inspect API boundaries with zero ambiguity.
