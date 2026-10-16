"""
Google Antigravity Plugins Installer CLI
Enables one-command installation of any or all plugins into workspace or global Antigravity configurations.
"""

import os
import sys
import shutil
import json
import argparse

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
PLUGINS_DIR = os.path.join(ROOT_DIR, 'plugins')
GLOBAL_CONFIG_DIR = os.path.expanduser(os.path.join('~', '.gemini', 'config', 'plugins'))
WORKSPACE_CONFIG_DIR = os.path.join(os.getcwd(), '.agents', 'plugins')

def list_plugins():
    mp_file = os.path.join(ROOT_DIR, 'marketplace.json')
    if not os.path.exists(mp_file):
        print("Marketplace catalog not found.")
        return
    with open(mp_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"\nAvailable Google Antigravity Plugins ({len(data['plugins'])} total):\n")
    print(f"{'Plugin Name':<32} | {'Version':<8} | {'Description'}")
    print("-" * 80)
    for p in data['plugins']:
        desc = p['description'][:65] + '...' if len(p['description']) > 65 else p['description']
        print(f"{p['name']:<32} | {p['version']:<8} | {desc}")
    print("\nInstall with: python scripts/install.py <plugin-name> [--scope global|project]")

def install_plugin(name: str, scope: str = 'project'):
    src_plugin = os.path.join(PLUGINS_DIR, name)
    if not os.path.exists(src_plugin):
        print(f"Error: Plugin '{name}' does not exist in {PLUGINS_DIR}")
        return False
        
    dest_base = GLOBAL_CONFIG_DIR if scope == 'global' else WORKSPACE_CONFIG_DIR
    os.makedirs(dest_base, exist_ok=True)
    dest_plugin = os.path.join(dest_base, name)
    
    if os.path.exists(dest_plugin):
        shutil.rmtree(dest_plugin)
    shutil.copytree(src_plugin, dest_plugin)
    print(f"✓ Installed '{name}' into {dest_plugin}")
    return True

def install_all(scope: str = 'project'):
    plugins = [p for p in os.listdir(PLUGINS_DIR) if os.path.isdir(os.path.join(PLUGINS_DIR, p))]
    print(f"Installing all {len(plugins)} plugins to scope: {scope}...")
    success = 0
    for p in plugins:
        if install_plugin(p, scope):
            success += 1
    print(f"\n✓ Successfully installed {success}/{len(plugins)} plugins!")
    print(f"Destination: {GLOBAL_CONFIG_DIR if scope == 'global' else WORKSPACE_CONFIG_DIR}")
    print("Restart your Antigravity session to discover new plugins.")

def main():
    parser = argparse.ArgumentParser(description="Google Antigravity Plugins Installer")
    parser.add_argument('plugin', nargs='?', help='Name of plugin to install (or omit to list/use flags)')
    parser.add_argument('--all', action='store_true', help='Install all 60 plugins')
    parser.add_argument('--list', action='store_true', help='List all available plugins')
    parser.add_argument('--scope', choices=['project', 'global'], default='project', help='Install scope (default: project)')

    args = parser.parse_args()

    if args.list or (not args.plugin and not args.all):
        list_plugins()
    elif args.all:
        install_all(args.scope)
    elif args.plugin:
        install_plugin(args.plugin, args.scope)

if __name__ == '__main__':
    main()
