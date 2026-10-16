<div align="center">

# 🚀 Google Antigravity Official Plugins Directory

**The official-grade directory of plugins, skills, agents, rules, hooks, and MCP servers natively ported and optimized for Google Antigravity.**

[![Antigravity 2.0 Compatible](https://img.shields.io/badge/Antigravity-2.0%2B%20Compatible-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://antigravity.google.com)
[![Plugins Count](https://img.shields.io/badge/Plugins-54%20Verified-34A853?style=for-the-badge)](./plugins)
[![Skills Count](https://img.shields.io/badge/Skills-77%2B%20Active-FBBC05?style=for-the-badge)](./plugins)
[![Subagents Count](https://img.shields.io/badge/Subagents-36%20Specialized-EA4335?style=for-the-badge)](./plugins)
[![Tests Passed](https://img.shields.io/badge/Validation-100%25%20Passed-blueviolet?style=for-the-badge)](./scripts/test_plugins.py)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](./LICENSE)

<br/>

[Plugin Catalog](#-plugin-catalog) • [Architecture](#-antigravity-plugin-architecture) • [Quick Start & Installation](#-quick-start--installation) • [Automated Testing](#-automated-testing--validation) • [Contributing](#-contributing)

</div>

---

## 🌟 Overview

**`Google_Antigravity_Plugins`** is a curated, production-grade directory containing **54 verified plugins** natively built and optimized for **Google Antigravity**.

This repository ports and enhances the full catalog of Anthropic's official plugins directory (`claude-plugins-official`), translating every single line, configuration, agent, skill, and hook to strict **Google Antigravity Customization System Specifications**.

### 💎 Key Highlights

- **100% Direct Parity**: All 40 internal plugins and 14 external plugins fully transpiled into native Antigravity bundles.
- **Antigravity Tooling & Runtime**: Legacy `CLAUDE.md`, `Bash`, `Edit`, and `Task` tools have been cleanly adapted into native Antigravity primitives: `AGENTS.md`, `GEMINI.md`, `run_command`, `replace_file_content`, `write_to_file`, `view_file`, `invoke_subagent`, and `call_mcp_tool`.
- **Full Architecture Support**: Complete integration of Antigravity manifests (`plugin.json`), on-demand progressive disclosure skills (`skills/*/SKILL.md`), multi-model subagents (`agents/*.md`), lifecycle hooks (`hooks.json`), rules (`rules/AGENTS.md`), and Model Context Protocol servers (`mcp_config.json`).
- **One-Command Installation**: Built-in CLI installer (`scripts/install.py`) to install plugins into workspace (`.agents/plugins/`) or machine-global (`~/.gemini/config/plugins/`) locations.
- **100% Automated Test Coverage**: Every plugin passes rigorous schema, YAML frontmatter, path resolution, and syntax validation.

---

## 📦 Antigravity Plugin Architecture

Every plugin in this repository adheres strictly to the official Antigravity folder hierarchy:

```text
plugins/<plugin_name>/
├── plugin.json         # Required: Antigravity manifest (name, displayName, description, version, logo, suggestedPrompts)
├── README.md           # User documentation and usage examples
├── mcp_config.json     # Optional: Model Context Protocol servers exposed by the plugin
├── hooks.json          # Optional: PreToolUse, PostToolUse, and Stop lifecycle hooks
├── rules/
│   └── AGENTS.md       # Consolidated rules active whenever the plugin is enabled
├── skills/
│   └── <skill_name>/
│       └── SKILL.md    # Progressive disclosure on-demand skills with YAML frontmatter
└── agents/
    └── <agent_name>.md # Specialized subagent definitions (model: inherit | flash | pro)
```

---

## 📑 Plugin Catalog

<details open>
<summary><b>1. Development & Workflow (12 Plugins)</b></summary>

| Plugin | Version | Capabilities | Description |
| :--- | :---: | :---: | :--- |
| **[`feature-dev`](./plugins/feature-dev)** | 1.0.0 | 7 Skills, 3 Agents | Guided 7-phase feature development with architecture exploration and code review. |
| **[`code-modernization`](./plugins/code-modernization)** | 1.0.0 | 13 Skills, 8 Agents, Hooks | Enterprise legacy migration, rule extraction, and modernization verification. |
| **[`code-simplifier`](./plugins/code-simplifier)** | 1.0.0 | 1 Agent | Reduces cognitive complexity, simplifies control flow, and eliminates redundant abstractions. |
| **[`commit-commands`](./plugins/commit-commands)** | 1.0.0 | 3 Skills | Smart git commit creation, PR generation, and cleanup of dead tracking branches. |
| **[`antigravity-plugin-dev`](./plugins/antigravity-plugin-dev)** | 1.0.0 | 7 Skills, 3 Agents | The definitive Antigravity Plugin & Skill authoring, testing, and validation kit. |
| **[`skill-creator`](./plugins/skill-creator)** | 1.0.0 | 1 Skill, 3 Agents, Scripts | Benchmarking, evaluation generator, and packaging suite for Antigravity skills. |
| **[`agent-sdk-dev`](./plugins/agent-sdk-dev)** | 1.0.0 | 1 Skill, 2 Agents | Google Antigravity & Gemini Agent SDK application scaffolding and verification. |
| **[`antigravity-setup`](./plugins/antigravity-setup)** | 1.0.0 | 1 Skill | Codebase analyzer that recommends tailored Antigravity hooks, skills, and subagents. |
| **[`antigravity-rules-management`](./plugins/antigravity-rules-management)** | 1.0.0 | 2 Skills | Audit, optimize, and maintain `AGENTS.md` and `GEMINI.md` project context files. |
| **[`hookify`](./plugins/hookify)** | 1.0.0 | 4 Skills, 1 Agent, Hooks | Declarative lifecycle hook creation and behavioral guardrails for tool execution. |
| **[`cwc-makers`](./plugins/cwc-makers)** | 1.0.0 | 3 Skills | Hardware hacking, Cardputer buddy, and M5Stack onboarding. |
| **[`example-plugin`](./plugins/example-plugin)** | 1.0.0 | 2 Skills, MCP | Canonical template demonstrating skills, MCP tools, rules, and hooks. |

</details>

<details open>
<summary><b>2. Code Review & Security (4 Plugins)</b></summary>

| Plugin | Version | Capabilities | Description |
| :--- | :---: | :---: | :--- |
| **[`code-review`](./plugins/code-review)** | 1.0.0 | 1 Skill | Automated PR code review using parallel Flash and Pro subagents with confidence scoring. |
| **[`pr-review-toolkit`](./plugins/pr-review-toolkit)** | 1.0.0 | 1 Skill, 6 Agents | Elite PR review team: silent failure hunter, type design analyzer, test analyzer. |
| **[`security-guidance`](./plugins/security-guidance)** | 2.0.14 | Hooks, Tests | PreToolUse security auditing, sensitive file gating, and credential leak prevention. |
| **[`antigravity-security`](./plugins/antigravity-security)** | 0.12.0 | 1 Skill, 8 Agents, Hooks | In-depth SAST vulnerability scanner, CWE classifier, and automated patch verifier. |

</details>

<details open>
<summary><b>3. Language Server Protocol (LSP) Intelligence (12 Plugins)</b></summary>

| Plugin | Version | Language / Engine | Supported File Extensions |
| :--- | :---: | :--- | :--- |
| **[`clangd-lsp`](./plugins/clangd-lsp)** | 1.0.0 | C / C++ (`clangd`) | `.c`, `.h`, `.cpp`, `.cc`, `.cxx`, `.hpp`, `.hxx` |
| **[`csharp-lsp`](./plugins/csharp-lsp)** | 1.0.0 | C# (`csharp-ls`) | `.cs` |
| **[`gopls-lsp`](./plugins/gopls-lsp)** | 1.0.0 | Go (`gopls`) | `.go` |
| **[`jdtls-lsp`](./plugins/jdtls-lsp)** | 1.0.0 | Java (`jdtls`) | `.java` |
| **[`kotlin-lsp`](./plugins/kotlin-lsp)** | 1.0.0 | Kotlin (`kotlin-lsp`) | `.kt`, `.kts` |
| **[`lua-lsp`](./plugins/lua-lsp)** | 1.0.0 | Lua (`lua-language-server`) | `.lua` |
| **[`php-lsp`](./plugins/php-lsp)** | 1.0.0 | PHP (`intelephense`) | `.php` |
| **[`pyright-lsp`](./plugins/pyright-lsp)** | 1.0.0 | Python (`pyright`) | `.py`, `.pyi` |
| **[`ruby-lsp`](./plugins/ruby-lsp)** | 1.0.0 | Ruby (`ruby-lsp`) | `.rb`, `.rake`, `.gemspec`, `.ru`, `.erb` |
| **[`rust-analyzer-lsp`](./plugins/rust-analyzer-lsp)** | 1.0.0 | Rust (`rust-analyzer`) | `.rs` |
| **[`swift-lsp`](./plugins/swift-lsp)** | 1.0.0 | Swift (`sourcekit-lsp`) | `.swift` |
| **[`typescript-lsp`](./plugins/typescript-lsp)** | 1.0.0 | TypeScript / JavaScript | `.ts`, `.tsx`, `.js`, `.jsx`, `.mts`, `.cts`, `.mjs`, `.cjs` |

</details>

<details open>
<summary><b>4. MCP Servers & Cloud Integrations (14 Plugins)</b></summary>

| Plugin | Version | Provider / Type | Description |
| :--- | :---: | :--- | :--- |
| **[`github`](./plugins/github)** | 1.0.0 | HTTP MCP | Official GitHub integration for issue management, PRs, and branch workflows. |
| **[`gitlab`](./plugins/gitlab)** | 1.0.0 | HTTP MCP | GitLab DevOps integration for MRs, issues, pipelines, and repository management. |
| **[`playwright`](./plugins/playwright)** | 1.0.0 | Stdio MCP | Headless browser automation, web scraping, and UI testing via `@playwright/mcp`. |
| **[`firebase`](./plugins/firebase)** | 1.0.0 | Stdio MCP | Google Firebase tools: Firestore, Cloud Functions, and Firebase Auth. |
| **[`terraform`](./plugins/terraform)** | 1.0.0 | Docker MCP | Infrastructure-as-code automation using HashiCorp Terraform MCP server. |
| **[`linear`](./plugins/linear)** | 1.0.0 | HTTP MCP | Linear issue tracking, sprint planning, and roadmap management. |
| **[`asana`](./plugins/asana)** | 1.0.0 | Stdio Tooling | Asana task and project management integration. |
| **[`context7`](./plugins/context7)** | 1.0.0 | HTTP MCP | Live documentation lookup and library API search via Context7. |
| **[`serena`](./plugins/serena)** | 1.0.0 | Stdio MCP | Semantic code search and indexing server (`serena`). |
| **[`laravel-boost`](./plugins/laravel-boost)** | 1.0.0 | Stdio MCP | Laravel Artisan CLI and ecosystem development accelerator. |
| **[`mcp-server-dev`](./plugins/mcp-server-dev)** | 1.0.0 | 3 Skills | Complete developer guide for designing, authoring, and testing MCP servers. |
| **[`mcp-tunnels`](./plugins/mcp-tunnels)** | 1.0.0 | 1 Skill | Secure tunneling for private MCP servers through Docker and SSH. |
| **[`discord`](./plugins/discord)** | 0.0.4 | TypeScript / Bun | Discord messaging bridge and bot automation channel. |
| **[`telegram`](./plugins/telegram)** | 0.0.7 | TypeScript / Bun | Telegram bot and chat integration bridge. |
| **[`imessage`](./plugins/imessage)** | 0.2.0 | TypeScript / Bun | macOS Apple Messages integration channel. |
| **[`fakechat`](./plugins/fakechat)** | 0.0.1 | TypeScript / Bun | Localhost mock chat testbench for UI testing. |

</details>

<details open>
<summary><b>5. Design, Mathematical Reasoning & Analytics (12 Plugins)</b></summary>

| Plugin | Version | Capabilities | Description |
| :--- | :---: | :---: | :--- |
| **[`frontend-design`](./plugins/frontend-design)** | 1.0.0 | 1 Skill | Intentional, opinionated UI/UX design: typography, color theory, layout geometry. |
| **[`project-artifact`](./plugins/project-artifact)** | 1.0.0 | 1 Skill, HTML | Opinionated, executive-ready HTML/SVG visual artifact generator for Antigravity. |
| **[`playground`](./plugins/playground)** | 1.0.0 | 1 Skill, 6 Templates | Interactive scratchpad for code maps, concept maps, and design experiments. |
| **[`math-olympiad`](./plugins/math-olympiad)** | 1.0.0 | 1 Skill, References | Advanced competitive mathematics (IMO, Putnam, USAMO) problem solving. |
| **[`math-proof`](./plugins/math-proof)** | 1.0.0 | 2 Skills, 3 Agents | Formal verification, Lean/Coq proof engineering, and siege mode problem solving. |
| **[`session-report`](./plugins/session-report)** | 1.0.0 | 1 Skill, JS/HTML | Generates visual HTML timelines and reports of agent sessions. |
| **[`receipts`](./plugins/receipts)** | 1.0.0 | 1 Skill, JS/PNG | Transcript telemetry mining and session action accounting. |
| **[`ralph-loop`](./plugins/ralph-loop)** | 1.0.0 | 3 Skills, Hooks | Autonomous iterative task execution loop with stop gatehooks. |
| **[`explanatory-output-style`](./plugins/explanatory-output-style)** | 1.0.0 | Hooks | Educational output formatting injecting conceptual explanations into agent answers. |
| **[`learning-output-style`](./plugins/learning-output-style)** | 1.0.0 | Hooks | Socratic output formatting prompting the user for active learning contributions. |

</details>

---

## 🚀 Quick Start & Installation

### Option 1: Using the Included Installer CLI (Recommended)

Clone the repository and run `scripts/install.py`:

```bash
git clone https://github.com/smartworldarafath/Google_Antigravity_Plugins.git
cd Google_Antigravity_Plugins

# List all 54 available plugins
python scripts/install.py --list

# Install a specific plugin to the current project (.agents/plugins/)
python scripts/install.py feature-dev

# Install a specific plugin globally (~/.gemini/config/plugins/)
python scripts/install.py code-review --scope global

# Install ALL 54 plugins at once
python scripts/install.py --all --scope global
```

### Option 2: Manual Installation

To install any plugin manually, simply copy its directory from `plugins/<plugin_name>` into your target Antigravity customizations directory:

- **Workspace-scoped** (checked into project VCS):
  ```bash
  mkdir -p .agents/plugins
  cp -r plugins/feature-dev .agents/plugins/
  ```

- **Global-scoped** (available in all projects on this machine):
  ```bash
  mkdir -p ~/.gemini/config/plugins
  cp -r plugins/feature-dev ~/.gemini/config/plugins/
  ```

*Note: Antigravity automatically discovers new plugin directories upon session start. Restart or launch a new turn after installing.*

---

## 🧪 Automated Testing & Validation

Every plugin, skill, agent, rule, hook, and manifest in this repository is strictly validated by an automated test suite:

```bash
python scripts/test_plugins.py
```

### Verification Criteria
- [x] Every plugin has a valid `plugin.json` adhering to the Antigravity Customization Specification.
- [x] Zero unsupported top-level fields (e.g. `author`, `homepage` omitted from `plugin.json` to prevent loader drops).
- [x] Every skill has a compliant `SKILL.md` with valid YAML frontmatter (`name`, `description`).
- [x] Every agent has a compliant `agents/<agent>.md` with valid frontmatter (`name`, `description`, `model`).
- [x] All `mcp_config.json` files implement valid `mcpServers` object schemas.
- [x] All `hooks.json` files implement Antigravity event structures (`PreToolUse`, `PostToolUse`, `Stop`).
- [x] Master `marketplace.json` and `plugins.json` catalog all 54 plugins.

---

## 🤝 Contributing

Contributions, enhancements, and new Antigravity plugins are warmly welcome!

1. Fork the repository.
2. Create your plugin directory under `plugins/<plugin-name>/`.
3. Add `plugin.json`, `README.md`, `rules/AGENTS.md`, and your `skills/`.
4. Run `python scripts/test_plugins.py` to ensure 100% compliance.
5. Submit a Pull Request.

---

## 📄 License

Distributed under the [MIT License](./LICENSE). Copyright (c) 2026 smartworldarafath.
