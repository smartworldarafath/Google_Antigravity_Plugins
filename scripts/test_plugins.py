"""
Automated Test & Validation Suite for Google Antigravity Plugins.
Validates 100% compliance across all plugins, skills, agents, rules,
manifests, and configurations against Antigravity specifications.
"""

import os
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
PLUGINS_DIR = os.path.join(ROOT_DIR, 'plugins')
MARKETPLACE_JSON = os.path.join(ROOT_DIR, 'marketplace.json')
PLUGINS_JSON = os.path.join(ROOT_DIR, 'plugins.json')

def test_all():
    print("=" * 60)
    print("Running Google Antigravity Plugin Validation Suite")
    print("=" * 60)

    total_plugins = 0
    passed_plugins = 0
    total_skills = 0
    total_agents = 0
    total_rules = 0
    total_mcps = 0
    total_hooks = 0
    errors = []

    # 1. Test Marketplace and Plugins Catalogs
    if not os.path.exists(MARKETPLACE_JSON):
        errors.append("marketplace.json missing at repository root")
    else:
        try:
            with open(MARKETPLACE_JSON, 'r', encoding='utf-8') as f:
                mp_data = json.load(f)
            assert 'plugins' in mp_data and len(mp_data['plugins']) > 0
            print(f"✓ marketplace.json valid: {len(mp_data['plugins'])} catalogued plugins")
        except Exception as e:
            errors.append(f"marketplace.json parsing error: {e}")

    if not os.path.exists(PLUGINS_JSON):
        errors.append("plugins.json missing at repository root")
    else:
        try:
            with open(PLUGINS_JSON, 'r', encoding='utf-8') as f:
                pj_data = json.load(f)
            assert 'plugins' in pj_data and len(pj_data['plugins']) > 0
            print(f"✓ plugins.json valid: {len(pj_data['plugins'])} entries")
        except Exception as e:
            errors.append(f"plugins.json parsing error: {e}")

    # 2. Iterate each plugin in plugins/
    plugins = sorted([p for p in os.listdir(PLUGINS_DIR) if os.path.isdir(os.path.join(PLUGINS_DIR, p))])
    total_plugins = len(plugins)

    for p in plugins:
        p_path = os.path.join(PLUGINS_DIR, p)
        plugin_errors = []

        # Validate plugin.json
        pj_path = os.path.join(p_path, 'plugin.json')
        if not os.path.exists(pj_path):
            plugin_errors.append("Missing plugin.json")
        else:
            try:
                with open(pj_path, 'r', encoding='utf-8') as f:
                    pj = json.load(f)
                if not pj.get('name'):
                    plugin_errors.append("plugin.json missing 'name'")
                if not pj.get('description'):
                    plugin_errors.append("plugin.json missing 'description'")
                if not pj.get('suggestedPrompts') or len(pj.get('suggestedPrompts', [])) == 0:
                    plugin_errors.append("plugin.json missing 'suggestedPrompts'")
                
                # Check forbidden fields
                for forbidden in ['author', 'homepage']:
                    if forbidden in pj:
                        plugin_errors.append(f"plugin.json has unsupported top-level field: '{forbidden}'")

                # Validate logo
                logo_rel = pj.get('logo', 'assets/logo.svg')
                logo_abs = os.path.join(p_path, logo_rel)
                if not os.path.exists(logo_abs):
                    plugin_errors.append(f"Referenced logo does not exist: {logo_rel}")

            except Exception as e:
                plugin_errors.append(f"Failed to parse plugin.json: {e}")

        # Validate README.md
        readme_path = os.path.join(p_path, 'README.md')
        if not os.path.exists(readme_path) or os.path.getsize(readme_path) == 0:
            plugin_errors.append("Missing or empty README.md")

        # Validate rules/AGENTS.md
        rules_path = os.path.join(p_path, 'rules', 'AGENTS.md')
        if os.path.exists(rules_path):
            total_rules += 1
            if os.path.getsize(rules_path) == 0:
                plugin_errors.append("Empty rules/AGENTS.md")

        # Validate mcp_config.json if present
        mcp_path = os.path.join(p_path, 'mcp_config.json')
        if os.path.exists(mcp_path):
            total_mcps += 1
            try:
                with open(mcp_path, 'r', encoding='utf-8') as f:
                    mcp = json.load(f)
                if 'mcpServers' not in mcp or not isinstance(mcp['mcpServers'], dict):
                    plugin_errors.append("mcp_config.json missing valid 'mcpServers' object")
            except Exception as e:
                plugin_errors.append(f"Invalid mcp_config.json: {e}")

        # Validate hooks.json if present
        hooks_path = os.path.join(p_path, 'hooks.json')
        if os.path.exists(hooks_path):
            total_hooks += 1
            try:
                with open(hooks_path, 'r', encoding='utf-8') as f:
                    hk = json.load(f)
                if not isinstance(hk, dict) or len(hk) == 0:
                    plugin_errors.append("hooks.json must be a non-empty object mapping hook names to events")
            except Exception as e:
                plugin_errors.append(f"Invalid hooks.json: {e}")

        # Validate skills
        skills_dir = os.path.join(p_path, 'skills')
        if os.path.exists(skills_dir):
            for sk in os.listdir(skills_dir):
                sk_path = os.path.join(skills_dir, sk)
                if os.path.isdir(sk_path):
                    total_skills += 1
                    sk_file = os.path.join(sk_path, 'SKILL.md')
                    if not os.path.exists(sk_file):
                        plugin_errors.append(f"Skill '{sk}' missing SKILL.md")
                    else:
                        with open(sk_file, 'r', encoding='utf-8', errors='ignore') as f:
                            sk_content = f.read()
                        if not sk_content.startswith('---'):
                            plugin_errors.append(f"Skill '{sk}/SKILL.md' missing YAML frontmatter")
                        else:
                            parts = sk_content.split('---', 2)
                            if len(parts) < 3:
                                plugin_errors.append(f"Skill '{sk}/SKILL.md' malformed YAML frontmatter")
                            else:
                                fm = parts[1]
                                if 'name:' not in fm:
                                    plugin_errors.append(f"Skill '{sk}/SKILL.md' frontmatter missing 'name'")
                                if 'description:' not in fm:
                                    plugin_errors.append(f"Skill '{sk}/SKILL.md' frontmatter missing 'description'")

        # Validate agents
        agents_dir = os.path.join(p_path, 'agents')
        if os.path.exists(agents_dir):
            for ag in os.listdir(agents_dir):
                if ag.endswith('.md'):
                    total_agents += 1
                    ag_file = os.path.join(agents_dir, ag)
                    with open(ag_file, 'r', encoding='utf-8', errors='ignore') as f:
                        ag_content = f.read()
                    if not ag_content.startswith('---'):
                        plugin_errors.append(f"Agent '{ag}' missing YAML frontmatter")
                    else:
                        parts = ag_content.split('---', 2)
                        if len(parts) < 3:
                            plugin_errors.append(f"Agent '{ag}' malformed YAML frontmatter")
                        else:
                            fm = parts[1]
                            if 'name:' not in fm:
                                plugin_errors.append(f"Agent '{ag}' missing 'name' in frontmatter")
                            if 'description:' not in fm:
                                plugin_errors.append(f"Agent '{ag}' missing 'description' in frontmatter")

        if plugin_errors:
            errors.append(f"[{p}] " + "; ".join(plugin_errors))
        else:
            passed_plugins += 1

    print("\n--- Summary of Verification ---")
    print(f"Total Plugins Tested : {total_plugins}")
    print(f"Passed Plugins       : {passed_plugins}")
    print(f"Total Skills Checked : {total_skills}")
    print(f"Total Agents Checked : {total_agents}")
    print(f"Total Rules Checked  : {total_rules}")
    print(f"Total MCPs Configured: {total_mcps}")
    print(f"Total Hooks Configured: {total_hooks}")
    
    if errors:
        print(f"\n❌ FAILED: {len(errors)} errors found:")
        for err in errors[:30]:
            print("  - " + err)
        if len(errors) > 30:
            print(f"  ... and {len(errors) - 30} more errors")
        sys.exit(1)
    else:
        print("\n✅ 100% PASSED: All plugins and configurations strictly conform to Antigravity standards!")
        sys.exit(0)

if __name__ == '__main__':
    test_all()
