---
title: "Install one MCP server across Claude Code, Cursor, Codex, and VS Code without manual config edits"
description: "Use add-mcp when an agent needs to roll out, list, remove, or synchronize MCP server configs across multiple coding clients instead of hand-editing each config file separately."
verification: "security_reviewed"
source: "https://github.com/neondatabase/add-mcp"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "neondatabase/add-mcp"
  github_stars: 151
  ase_npm_package: "add-mcp"
  npm_weekly_downloads: 307229
---

# Install one MCP server across Claude Code, Cursor, Codex, and VS Code without manual config edits

This skill is for the repetitive setup work around MCP adoption. An agent can install a remote MCP URL or local package into the right config files for supported clients, add required headers or environment variables, list what is already installed, remove stale entries, and synchronize server naming across tools. It is most useful when onboarding a server to several clients at once, standardizing team setup, or cleaning up drift between project and global configs.


The boundary is tight enough to be skill-shaped: the job is MCP configuration rollout and synchronization across agent clients. It is not a registry platform card, not an MCP server listing, and not a generic developer-tools bundle. Invoke it when the pain is manual config editing and config drift across clients, not when you need to build or host the server itself.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/install-one-mcp-server-across-claude-code-cursor-codex-and-vs-code-without-manual-config-edits/)
