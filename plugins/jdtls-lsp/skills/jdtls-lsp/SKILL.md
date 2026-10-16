---
name: jdtls-lsp
description: Eclipse JDT.LS language server for Java projects in Google Antigravity.
---

# Java Language Server (Eclipse JDT.LS)

Language Server Protocol integration for Google Antigravity. Provides code intelligence, diagnostics, go-to-definition, find-references, and type inspection.

## Supported Extensions
`.java`

## Prerequisites & Installation
Ensure `jdtls` is installed and available on your system PATH:

Install Eclipse JDT.LS or via package manager (`brew install jdtls` or `apt install jdtls`)

## Antigravity Workflow
1. When editing or analyzing files matching .java, the agent can invoke `jdtls` to verify syntax and type soundness.
2. Run language diagnostics via `run_command`:
   ```bash
   jdtls --version
   ```
3. Use language intelligence to trace symbol definitions and inspect API boundaries with zero ambiguity.
