---
title: "Install one MCP server across Claude Code, Cursor, Codex, and VS Code without manual config edits"
description: "This skill is for the repetitive setup work around MCP adoption. An agent can install a remote MCP URL or local package into the right config files for supported clients, add required headers or environment variables, list what is already installed, remove stale entries, and synchronize server naming across tools. It is most useful when onboarding a server to several clients at once, standardizing team setup, or cleaning up drift between project and global configs. The boundary is tight enough to be skill-shaped: the job is MCP configuration rollout and synchronization across agent clients. It is not a registry platform card, not an MCP server listing, and not a generic developer-tools bundle. Invoke it when the pain is manual config editing and config drift across clients, not when you need to build or host the server itself."
source: "https://github.com/neondatabase/add-mcp"
verification: "security_reviewed"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "neondatabase/add-mcp"
  github_stars: 151
  npm_package: "add-mcp"
  npm_weekly_downloads: 307229
---

# Install one MCP server across Claude Code, Cursor, Codex, and VS Code without manual config edits

This skill is for the repetitive setup work around MCP adoption. An agent can install a remote MCP URL or local package into the right config files for supported clients, add required headers or environment variables, list what is already installed, remove stale entries, and synchronize server naming across tools. It is most useful when onboarding a server to several clients at once, standardizing team setup, or cleaning up drift between project and global configs. The boundary is tight enough to be skill-shaped: the job is MCP configuration rollout and synchronization across agent clients. It is not a registry platform card, not an MCP server listing, and not a generic developer-tools bundle. Invoke it when the pain is manual config editing and config drift across clients, not when you need to build or host the server itself.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/install-one-mcp-server-across-claude-code-cursor-codex-and-vs-code-without-manual-config-edits/)
