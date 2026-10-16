---
name: lua-lsp
description: Lua language server for Lua scripting, Game dev, and Neovim development in Google Antigravity.
---

# Lua Language Server

Language Server Protocol integration for Google Antigravity. Provides code intelligence, diagnostics, go-to-definition, find-references, and type inspection.

## Supported Extensions
`.lua`

## Prerequisites & Installation
Ensure `lua-language-server` is installed and available on your system PATH:

brew install lua-language-server / winget install sumneko.lua-language-server

## Antigravity Workflow
1. When editing or analyzing files matching .lua, the agent can invoke `lua-language-server` to verify syntax and type soundness.
2. Run language diagnostics via `run_command`:
   ```bash
   lua-language-server --version
   ```
3. Use language intelligence to trace symbol definitions and inspect API boundaries with zero ambiguity.
