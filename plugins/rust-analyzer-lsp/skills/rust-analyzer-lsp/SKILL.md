---
name: rust-analyzer-lsp
description: rust-analyzer language server for Rust projects in Google Antigravity.
---

# Rust Language Server (rust-analyzer)

Language Server Protocol integration for Google Antigravity. Provides code intelligence, diagnostics, go-to-definition, find-references, and type inspection.

## Supported Extensions
`.rs`

## Prerequisites & Installation
Ensure `rust-analyzer` is installed and available on your system PATH:

rustup component add rust-analyzer

## Antigravity Workflow
1. When editing or analyzing files matching .rs, the agent can invoke `rust-analyzer` to verify syntax and type soundness.
2. Run language diagnostics via `run_command`:
   ```bash
   rust-analyzer --version
   ```
3. Use language intelligence to trace symbol definitions and inspect API boundaries with zero ambiguity.
