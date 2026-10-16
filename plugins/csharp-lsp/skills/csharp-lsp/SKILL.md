---
name: csharp-lsp
description: C# language server integration for Google Antigravity, providing semantic analysis, completions, and Roslyn diagnostics.
---

# C# Language Server

Language Server Protocol integration for Google Antigravity. Provides code intelligence, diagnostics, go-to-definition, find-references, and type inspection.

## Supported Extensions
`.cs`

## Prerequisites & Installation
Ensure `csharp-ls` is installed and available on your system PATH:

dotnet tool install -g csharp-ls

## Antigravity Workflow
1. When editing or analyzing files matching .cs, the agent can invoke `csharp-ls` to verify syntax and type soundness.
2. Run language diagnostics via `run_command`:
   ```bash
   csharp-ls --version
   ```
3. Use language intelligence to trace symbol definitions and inspect API boundaries with zero ambiguity.
