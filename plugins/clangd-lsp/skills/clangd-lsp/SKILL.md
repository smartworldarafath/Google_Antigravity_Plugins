---
name: clangd-lsp
description: C/C++ language server (clangd) integration for Google Antigravity, providing AST diagnostics, code intelligence, and formatting.
---

# C/C++ Language Server (Clangd)

Language Server Protocol integration for Google Antigravity. Provides code intelligence, diagnostics, go-to-definition, find-references, and type inspection.

## Supported Extensions
`.c`, `.h`, `.cpp`, `.cc`, `.cxx`, `.hpp`, `.hxx`, `.C`, `.H`

## Prerequisites & Installation
Ensure `clangd` is installed and available on your system PATH:

macOS: `brew install llvm` | Linux: `sudo apt install clangd` | Windows: `winget install LLVM.LLVM`

## Antigravity Workflow
1. When editing or analyzing files matching .c, .h, .cpp, .cc, .cxx, .hpp, .hxx, .C, .H, the agent can invoke `clangd` to verify syntax and type soundness.
2. Run language diagnostics via `run_command`:
   ```bash
   clangd --version
   ```
3. Use language intelligence to trace symbol definitions and inspect API boundaries with zero ambiguity.
