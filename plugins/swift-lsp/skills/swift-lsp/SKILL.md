---
name: swift-lsp
description: SourceKit-LSP language server for Swift and Apple platform development in Google Antigravity.
---

# Swift Language Server (SourceKit-LSP)

Language Server Protocol integration for Google Antigravity. Provides code intelligence, diagnostics, go-to-definition, find-references, and type inspection.

## Supported Extensions
`.swift`

## Prerequisites & Installation
Ensure `sourcekit-lsp` is installed and available on your system PATH:

Included with Xcode on macOS, or via swift.org toolchains on Linux.

## Antigravity Workflow
1. When editing or analyzing files matching .swift, the agent can invoke `sourcekit-lsp` to verify syntax and type soundness.
2. Run language diagnostics via `run_command`:
   ```bash
   sourcekit-lsp --version
   ```
3. Use language intelligence to trace symbol definitions and inspect API boundaries with zero ambiguity.
