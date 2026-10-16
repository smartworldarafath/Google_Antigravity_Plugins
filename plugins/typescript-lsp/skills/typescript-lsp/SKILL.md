---
name: typescript-lsp
description: TypeScript and JavaScript language server for Node.js, React, and web projects in Google Antigravity.
---

# TypeScript/JavaScript Language Server

Language Server Protocol integration for Google Antigravity. Provides code intelligence, diagnostics, go-to-definition, find-references, and type inspection.

## Supported Extensions
`.ts`, `.tsx`, `.js`, `.jsx`, `.mts`, `.cts`, `.mjs`, `.cjs`

## Prerequisites & Installation
Ensure `typescript-language-server` is installed and available on your system PATH:

npm install -g typescript-language-server typescript

## Antigravity Workflow
1. When editing or analyzing files matching .ts, .tsx, .js, .jsx, .mts, .cts, .mjs, .cjs, the agent can invoke `typescript-language-server` to verify syntax and type soundness.
2. Run language diagnostics via `run_command`:
   ```bash
   typescript-language-server --version
   ```
3. Use language intelligence to trace symbol definitions and inspect API boundaries with zero ambiguity.
