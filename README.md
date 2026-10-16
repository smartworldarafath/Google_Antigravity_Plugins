<div align="center">

# 🚀 Google Antigravity Plugins (Official & Community Ecosystem)

**The premier, production-grade plugins, skills, agents, rules, hooks, and MCP servers repository built natively for Google Antigravity.**

[![Antigravity 2.0 Compatible](https://img.shields.io/badge/Antigravity-2.0%2B%20Compatible-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://antigravity.google.com)
[![Plugins Count](https://img.shields.io/badge/Plugins-60%20Verified-34A853?style=for-the-badge)](./plugins)
[![Skills Count](https://img.shields.io/badge/Skills-177%2B%20Active-FBBC05?style=for-the-badge)](./plugins)
[![Subagents Count](https://img.shields.io/badge/Subagents-36%20Specialized-EA4335?style=for-the-badge)](./plugins)
[![Tests Passed](https://img.shields.io/badge/Validation-100%25%20Passed-blueviolet?style=for-the-badge)](./scripts/test_plugins.py)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](./LICENSE)

<br/>

[Catalog](#-plugin-catalog) • [Architecture](#-antigravity-plugin-architecture) • [Quick Start](#-quick-start--installation) • [Reference Integrations](#-reference-skills--frameworks) • [Testing](#-automated-testing--validation) • [Contributing](#-contributing)

</div>

---

## 🌟 Overview

**`Google_Antigravity_Plugins`** is a curated, comprehensive collection of 60 first-class plugins meticulously ported, enhanced, and verified for **Google Antigravity**.

Originally conceived in the Claude Code ecosystem, this repository provides a **100% complete, native transpilation and expansion for Google Antigravity**. Every single plugin strictly implements the **Antigravity Customization System Specification** — packaging skills, agents, rules, hooks, and MCP servers into clean, deployable bundles.

### 💎 Key Highlights

- **100% Parity with Official Catalog**: All 40 internal plugins and 14 external plugins from Anthropic's official directory fully ported to Antigravity.
- **Deep Reference Integrations**: Supercharged with industry-leading AI engineering and research skills:
  - 🔍 **`reverse-engineer-anything` (REA)**: Full binary, JS/Electron, APK, WASM, and firmware reversing with MCP.
  - ⚡ **`jcode-performance`**: Ultra-low-memory swarm coordination and context budgeting (8x–37x less RAM).
  - 🛡️ **`open-code-review` (OCR)**: Alibaba's enterprise multi-language line-level code review engine with rule docs for 15+ languages.
  - 🎯 **`reverse-skill`**: Automated skill extraction, radare2 automation, and security pentesting playbooks.
  - 👥 **`engineering-team`**: Full engineering squad workflows (`playwright-pro`, `self-improving-agent`, `a11y-audit`, `google-workspace-cli`).
  - 🧠 **`deep-engineering`**: Elite software craftsmanship (`karpathy-coder`, `zero-hallucination-coder`, `chaos-engineering`, `code-tour`, `slo-architect`).
- **Zero Incompatible Tools**: Clean conversion of legacy `CLAUDE.md`, `Bash`, `Edit`, `Task` to native Antigravity primitives: `AGENTS.md`, `GEMINI.md`, `run_command`, `replace_file_content`, `write_to_file`, `view_file`, `invoke_subagent`, and `call_mcp_tool`.
- **One-Command Installation**: CLI tool to install plugins into workspace (`.agents/plugins/`) or global (`~/.gemini/config/plugins/`) scopes.

---

## 📦 Antigravity Plugin Architecture

Each plugin in this repository strictly adheres to the official Antigravity folder layout:

```text
plugins/<plugin_name>/
├── plugin.json         # Required: Manifest (name, displayName, description, version, logo, suggestedPrompts)
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
<summary><b>1. Development & Engineering (15 Plugins)</b></summary>

| Plugin | Version | Capabilities | Description |
| :--- | :---: | :---: | :--- |
| **[`feature-dev`](./plugins/feature-dev)** | 1.0.0 | 7 Skills, 3 Agents | Guided 7-phase feature development with architecture exploration and code review. |
| **[`code-modernization`](./plugins/code-modernization)** | 1.0.0 | 13 Skills, 8 Agents, Hooks | Enterprise legacy migration, rule extraction, and modernization verification. |
| **[`code-simplifier`](./plugins/code-simplifier)** | 1.0.0 | 1 Agent | Reduces cognitive complexity, simplifies control flow, and eliminates redundant abstractions. |
| **[`commit-commands`](./plugins/commit-commands)** | 1.0.0 | 3 Skills | Smart git commit creation, PR generation, and cleanup of dead tracking branches. |
| **[`deep-engineering`](./plugins/deep-engineering)** | 1.0.0 | 43 Skills, Rules | Karpathy first-principles coder, zero-hallucination validation, and chaos engineering. |
| **[`engineering-team`](./plugins/engineering-team)** | 1.0.0 | 6 Skills, Rules | Playwright E2E testing, self-improving agent loops, and WCAG accessibility audits. |
| **[`jcode-performance`](./plugins/jcode-performance)** | 1.0.0 | 2 Skills, Rules | High-efficiency coding agent runtime, swarm coordination, and context budgeting. |
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
<summary><b>2. Code Review & Quality (5 Plugins)</b></summary>

| Plugin | Version | Capabilities | Description |
| :--- | :---: | :---: | :--- |
| **[`code-review`](./plugins/code-review)** | 1.0.0 | 1 Skill | Automated PR code review using parallel Flash and Pro subagents with confidence scoring. |
| **[`pr-review-toolkit`](./plugins/pr-review-toolkit)** | 1.0.0 | 1 Skill, 6 Agents | Elite PR review team: silent failure hunter, type design analyzer, test analyzer. |
| **[`open-code-review`](./plugins/open-code-review)** | 1.0.0 | 2 Skills, Rule Docs | Alibaba's enterprise AI review engine with specialized rules for 15+ languages. |
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
<summary><b>4. Security & Reverse Engineering (2 Plugins)</b></summary>

| Plugin | Version | Capabilities | Description |
| :--- | :---: | :---: | :--- |
| **[`reverse-engineer-anything`](./plugins/reverse-engineer-anything)** | 1.0.0 | 4 Skills, MCP | Comprehensive binary, JS/Electron, APK, WASM, EVM, SQLite, and network reversing. |
| **[`reverse-skill`](./plugins/reverse-skill)** | 1.0.0 | 40+ Skills, Scripts | Protocol analysis, radare2, thick-client security, firmware, and supply-chain auditing. |

</details>

<details open>
<summary><b>5. MCP Servers & Cloud Integrations (14 Plugins)</b></summary>

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
<summary><b>6. Mathematical Reasoning, Design & Analytics (12 Plugins)</b></summary>

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

# List all 60 available plugins
python scripts/install.py --list

# Install a specific plugin to the current project (.agents/plugins/)
python scripts/install.py feature-dev

# Install a specific plugin globally (~/.gemini/config/plugins/)
python scripts/install.py code-review --scope global

# Install ALL 60 plugins at once
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

## 🔍 Reference Skills & Frameworks

This repository incorporates and synthesizes patterns from world-class agentic repositories:

1. **[morluto/rea](https://github.com/morluto/rea)**: Integrated into `plugins/reverse-engineer-anything` — the definitive reverse-engineering MCP toolchain.
2. **[1jehuang/jcode](https://github.com/1jehuang/jcode)**: Integrated into `plugins/jcode-performance` — memory budgeting and multi-agent swarm orchestration.
3. **[alibaba/open-code-review](https://github.com/alibaba/open-code-review)**: Integrated into `plugins/open-code-review` — enterprise multi-language line-level code review engine.
4. **[zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill)**: Integrated into `plugins/reverse-skill` — automated skill extraction and penetration testing playbooks.
5. **[alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)**:
   - `engineering-team`: Integrated into `plugins/engineering-team` (Playwright Pro, Self-Improving Agent, WCAG A11y, Google Workspace CLI).
   - `engineering`: Integrated into `plugins/deep-engineering` (Karpathy Coder, Zero Hallucination, Chaos Engineering, SLO Architect).

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
- [x] Master `marketplace.json` and `plugins.json` catalog all 60 plugins.

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
