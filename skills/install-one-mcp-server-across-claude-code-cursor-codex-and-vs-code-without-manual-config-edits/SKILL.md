---
title: "Install one MCP server across Claude Code, Cursor, Codex, and VS Code without manual config edits"
description: "This skill is for the repetitive setup work around MCP adoption. An agent can install a remote MCP URL or local package into the right config files for supported clients, add required headers or environment variables, list what is already installed, remove stale entries, and synchronize server naming across tools. It is most useful when onboarding a server to several clients at once, standardizing team setup, or cleaning up drift between project and global configs.\nThe boundary is tight enough to be skill-shaped: the job is MCP configuration rollout and synchronization across agent clients. It is not a registry platform card, not an MCP server listing, and not a generic developer-tools bundle. Invoke it when the pain is manual config editing and config drift across clients, not when you need to build or host the server itself."
verification: security_reviewed
source: "https://github.com/neondatabase/add-mcp"
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

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/install-one-mcp-server-across-claude-code-cursor-codex-and-vs-code-without-manual-config-edits
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/install-one-mcp-server-across-claude-code-cursor-codex-and-vs-code-without-manual-config-edits` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/install-one-mcp-server-across-claude-code-cursor-codex-and-vs-code-without-manual-config-edits/)
