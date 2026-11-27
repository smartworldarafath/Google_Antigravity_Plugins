---
name: open-agentic-web-devtools
description: Validate, inspect, scaffold, and test Open Agentic Web nodes adhering to the Cognizant / Mozilla / MIT NANDA MVP Profile 0.3 specification. Use when auditing agent-manifest.json, *.network.json, links.json, action bridges, or generating Agent-to-Agent (A2A) agent cards.
---

# Open Agentic Web DevTools Skill

This skill equips autonomous AI coding agents with the official toolset, best practices, and CLI commands for building and auditing Open Agentic Web nodes.

## Core Specification & Standards (MVP Profile 0.3)

Every conforming Open Agentic Web node requires:
1. `agent-manifest.json`: Top-level manifest declaring networks, front agents, and `actions.agentTools`.
2. `*.network.json`: Declarative Neuro SAN multi-agent graph with strictly separated router and front agent instructions.
3. `bridge/action-bridge.html` or `site-actions.js`: Sandboxed iframe receiver or top-level action registry conforming to the `nsdeploy-actions-v1` protocol.
4. `links.json` (on Hub nodes): Dynamic peer mesh mapping with CORS enabled (`Access-Control-Allow-Origin: *`).

## Essential CLI Commands (`oaw` / `open-agentic-web`)

Run via `npx open-agentic-web` or `node packages/open-agentic-web/bin/cli.mjs`:

### 1. Validate Nodes (Local Directory or Live Remote URL)
```bash
npx open-agentic-web validate sites/tripsteward-hub sites/cityglide-node --json
```
- Validates manifest schema, declarative graph integrity, parameter specifications, and action registrations.
- For remote URLs, audits HTTP CORS headers and `X-Frame-Options` frameability.

### 2. Audit Cross-Site Federation Mesh
```bash
npx open-agentic-web federation sites/tripsteward-hub sites/cityglide-node sites/metropass-node
```
- Verifies dynamic peer link resolution, manifest accessibility across domains, and multi-agent routing.

### 3. Test Action Bridge Handshake Contract
```bash
npx open-agentic-web test-bridge sites/tripsteward-hub
```
- Probes iframe action bridge, tests `catalog` message receiver contracts, and verifies declared tool schemas.

### 4. Generate Standard Agent-to-Agent (A2A) Card
```bash
npx open-agentic-web a2a sites/tripsteward-hub --out .well-known/agent.json
```
- Generates standard Linux Foundation / Google Agent-to-Agent (A2A) `agent.json` card with parameter schemas.

### 5. Scaffold a New Conforming Node
```bash
npx open-agentic-web init my-dining-node --name "tablebespoke_dining"
```
- Creates ready-to-run node directory with manifest, network graph, site actions, and HTML playground.

### 6. Start Local Dev Server with Playground
```bash
npx open-agentic-web dev sites/cityglide-node --port 8081
```
- Serves static node with CORS headers and opens interactive tool-testing sandbox at `/playground`.

## MCP Tools Integration

When running under an MCP-enabled agent host (Cursor, Claude Desktop, Antigravity):
- Call `oaw_validate_node({ pathOrUrl: "..." })` to immediately check compliance.
- Call `oaw_audit_federation({ hubPath: "...", peerPaths: [...] })` to verify mesh health.
- Call `oaw_list_actions()` to view all available action tools with their effect tags (`read`, `irreversible`, `undoable`).
