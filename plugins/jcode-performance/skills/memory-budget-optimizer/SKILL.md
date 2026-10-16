---
name: memory-budget-optimizer
description: Optimize agent context window and memory consumption
---

# Agent Memory & Budget Optimizer

Techniques for keeping Antigravity agents running fast, with minimal RAM and token consumption.

## Optimization Strategies
- **Selective File Viewing**: Use `view_file` with `StartLine` and `EndLine` to read only the relevant function or block rather than whole 10,000-line files.
- **Incremental Tool Chaining**: Avoid giant tool responses that blow up the context window.
- **Cache Warmth Awareness**: Structure iterative queries so common prefix prompts hit KV cache.
