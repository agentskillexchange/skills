---
title: "Install one MCP server across Claude Code, Cursor, Codex, and VS Code without manual config edits"
description: "Use add-mcp when an agent needs to roll out, list, remove, or synchronize MCP server configs across multiple coding clients instead of hand-editing each config file separately."
verification: "security_reviewed"
source: "https://github.com/neondatabase/add-mcp"
author: "Neon"
publisher_type: "company"
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

Use add-mcp when an agent needs to roll out, list, remove, or synchronize MCP server configs across multiple coding clients instead of hand-editing each config file separately.

## Prerequisites

Node.js and npx; one or more supported coding clients such as Claude Code, Codex, Cursor, OpenCode, or VS Code; any required server URLs, auth headers, env vars, or package names.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Run npx add-mcp to install an MCP server into detected project configs, or add -g for global config files. Use flags like -a to target specific clients, --header for remote auth, --env for local stdio servers, find to search registries, and sync to unify names and installations across clients.
```

## Documentation

- https://github.com/neondatabase/add-mcp

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/install-one-mcp-server-across-claude-code-cursor-codex-and-vs-code-without-manual-config-edits/)
