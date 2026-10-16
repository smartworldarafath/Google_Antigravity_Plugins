---
name: swarm-coordination
description: Coordinate parallel multi-agent swarms with zero collision
---

# JCode Swarm Coordination

Coordinate multiple autonomous coding subagents running in parallel on a single repository.

## Swarm Orchestration Principles
1. **Collision Avoidance**: Ensure subagents work on disjoint file sets or branches (`Workspace: branch`).
2. **Inter-agent Messaging**: Pass concise status summaries and contracts between subagents using `send_message`.
3. **Root vs Worker Separation**: Keep high-level strategic reasoning in the coordinator agent, and delegate file edits and tests to lightweight worker agents.
4. **Context Pruning**: Never pass complete file dumps between agents; pass targeted diffs and line ranges.
