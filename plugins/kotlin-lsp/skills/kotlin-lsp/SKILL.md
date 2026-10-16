---
name: kotlin-lsp
description: Kotlin language server for Kotlin and Android projects in Google Antigravity.
---

# Kotlin Language Server

Language Server Protocol integration for Google Antigravity. Provides code intelligence, diagnostics, go-to-definition, find-references, and type inspection.

## Supported Extensions
`.kt`, `.kts`

## Prerequisites & Installation
Ensure `kotlin-lsp` is installed and available on your system PATH:

Download from Kotlin Language Server releases or build via gradle.

## Antigravity Workflow
1. When editing or analyzing files matching .kt, .kts, the agent can invoke `kotlin-lsp` to verify syntax and type soundness.
2. Run language diagnostics via `run_command`:
   ```bash
   kotlin-lsp --version
   ```
3. Use language intelligence to trace symbol definitions and inspect API boundaries with zero ambiguity.
