#!/usr/bin/env node

/**
 * Universal Portable MCP Launcher for Antigravity Plugin
 * Automatically resolves to local workspace package if available,
 * or gracefully runs the published open-agentic-web npm package.
 */

import { spawn } from "node:child_process";
import { existsSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const localMcpPath = resolve(__dirname, "../../../packages/open-agentic-web/bin/mcp-server.mjs");

const args = process.argv.slice(2);

if (existsSync(localMcpPath)) {
  const proc = spawn(process.execPath, [localMcpPath, ...args], {
    stdio: "inherit"
  });
  proc.on("exit", (code) => process.exit(code ?? 0));
} else {
  const npxCmd = process.platform === "win32" ? "npx.cmd" : "npx";
  const proc = spawn(npxCmd, ["-y", "open-agentic-web@latest", "mcp", ...args], {
    stdio: "inherit"
  });
  proc.on("exit", (code) => process.exit(code ?? 0));
}
