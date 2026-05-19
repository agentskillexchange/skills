---
name: "Install one MCP server across Claude Code, Cursor, Codex, and VS Code without manual config edits"
slug: "install-one-mcp-server-across-claude-code-cursor-codex-and-vs-code-without-manual-config-edits"
description: "Use add-mcp when an agent needs to roll out, list, remove, or synchronize MCP server configs across multiple coding clients instead of hand-editing each config file separately."
github_stars: 151
verification: "security_reviewed"
source: "https://github.com/neondatabase/add-mcp"
author: "Neon"
publisher_type: "company"
category: "Developer Tools"
framework: "Multi-Framework"
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

Use the upstream install or setup path that matches your environment:
- npx add-mcp url | package name [options]
- npx add-mcp https://mcp.context7.com/mcp
- npx add-mcp find vercel
- npx add-mcp https://mcp.example.com/mcp

Requirements and caveats from upstream:
- # Node.js script
- add-mcp supports all three transport types: HTTP, SSE, and stdio. Some agents require type option to be set to specify the transport type. You can use the --type or --transport option to specify the transport type:

Basic usage or getting-started notes:
- bash
- Example installing the Context7 remote MCP server:
- You can add env variables and arguments (stdio) and headers (remote) to the server config using the --env, --args and --header options.

- Source: https://github.com/neondatabase/add-mcp
- Extracted from upstream docs: https://raw.githubusercontent.com/neondatabase/add-mcp/HEAD/README.md

## Documentation

- https://github.com/neondatabase/add-mcp

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/install-one-mcp-server-across-claude-code-cursor-codex-and-vs-code-without-manual-config-edits/)
