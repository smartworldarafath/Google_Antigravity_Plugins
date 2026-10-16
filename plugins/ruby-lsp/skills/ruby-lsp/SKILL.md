---
name: ruby-lsp
description: Ruby LSP language server for Ruby and Rails projects in Google Antigravity.
---

# Ruby Language Server

Language Server Protocol integration for Google Antigravity. Provides code intelligence, diagnostics, go-to-definition, find-references, and type inspection.

## Supported Extensions
`.rb`, `.rake`, `.gemspec`, `.ru`, `.erb`

## Prerequisites & Installation
Ensure `ruby-lsp` is installed and available on your system PATH:

gem install ruby-lsp

## Antigravity Workflow
1. When editing or analyzing files matching .rb, .rake, .gemspec, .ru, .erb, the agent can invoke `ruby-lsp` to verify syntax and type soundness.
2. Run language diagnostics via `run_command`:
   ```bash
   ruby-lsp --version
   ```
3. Use language intelligence to trace symbol definitions and inspect API boundaries with zero ambiguity.
