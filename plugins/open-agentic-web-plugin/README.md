# Open Agentic Web & TripSteward Plugin for Antigravity (AGY)

Official Autonomous AI Agent Plugin for **Google Antigravity (AGY)** and the **Open Agentic Web** specification (Cognizant / Mozilla / MIT NANDA MVP Profile 0.3).

This plugin provides Model Context Protocol (MCP) servers, devtools skills, operating rules, and multi-agent concierge workflows for Antigravity (`agy`), Antigravity IDE, Claude Code, and Cursor.

---

## 📦 What's Included

1. **Antigravity Plugin Manifest (`plugin.json`)**:
   - Declares plugin identity, suggested prompts, and metadata adhering to the Antigravity Customization System.

2. **Operating Rules (`rules/AGENTS.md`)**:
   - Enforces in-browser zero-leakage privacy (RAM/DOM only, 0 bytes on server).
   - Enforces human-in-the-loop confirmation modals for irreversible actions.
   - Enforces WebCrypto ECDSA P-256 cryptographic receipt verification.

3. **Specialized Agent Skills (`skills/`)**:
   - `open-agentic-web-devtools`: Conformance validation, mesh federation auditing, and node scaffolding (`oaw init`).
   - `open-agentic-web-actions`: Guide for authoring safe, schema-validated site actions with WebCrypto ECDSA receipts.
   - `open-agentic-web-concierge`: Step-by-step orchestrator for cross-site hotel booking, flight delay buffer synchronization, and scannable experience pass issuance.

4. **Model Context Protocol (MCP) Server (`mcp_config.json`)**:
   - Zero-dependency JSON-RPC 2.0 stdio server (`open-agentic-web/mcp`).
   - Surfaces all declared website tools (`website_search_rooms`, `website_hold_room`, `website_dispatch_chauffeur`, `website_issue_pass`) as executable MCP tools.
   - Provides built-in auditing tools: `oaw_validate_node`, `oaw_audit_federation`, `oaw_list_actions`, `oaw_generate_a2a`, and `oaw_inspect_node`.

---

## 🚀 Antigravity (AGY) Setup

### Option A: Workspace Discovery (Automatic)
The plugin is registered in `.agents/plugins/open-agentic-web-plugin` and `.agents/plugins.json`. When you start `agy` in this repository, it is **automatically discovered and enabled**.

### Option B: Global Discovery (Machine-Wide)
To enable the plugin across all projects in `agy`:
```bash
ln -sfn /path/to/devpost-Cognizant/plugins/open-agentic-web-plugin ~/.gemini/config/plugins/open-agentic-web-plugin
```

---

## 💻 Other Agent Environments

### Claude Desktop / Claude Code (`claude_desktop_config.json`)
```json
{
  "mcpServers": {
    "open-agentic-web": {
      "command": "node",
      "args": [
        "/path/to/devpost-Cognizant/packages/open-agentic-web/bin/mcp-server.mjs"
      ]
    }
  }
}
```

### Cursor (`.cursor/mcp.json`)
```json
{
  "mcpServers": {
    "open-agentic-web": {
      "command": "node",
      "args": [
        "${workspaceFolder}/packages/open-agentic-web/bin/mcp-server.mjs"
      ]
    }
  }
}
```

---

## 🛠️ Standalone CLI Usage
```bash
# Validate local node or remote URL
npx open-agentic-web validate sites/tripsteward-hub

# Audit cross-site federation mesh
npx open-agentic-web federation sites/tripsteward-hub sites/cityglide-node sites/metropass-node

# Start MCP server manually
npx open-agentic-web mcp sites/tripsteward-hub sites/cityglide-node sites/metropass-node
```
