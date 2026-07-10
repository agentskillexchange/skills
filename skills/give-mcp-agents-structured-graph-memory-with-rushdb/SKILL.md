---
title: "Give MCP agents structured graph memory with RushDB"
description: "Connect RushDB’s MCP server so agents can store, search, update, and traverse persistent structured memory without hand-building a separate vector and graph stack."
verification: "security_reviewed"
source: "https://github.com/rush-db/rushdb"
author: "RushDB"
publisher_type: "organization"
category:
  - "Integrations & Connectors"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "rush-db/rushdb"
  github_stars: 308
  npm_package: "@rushdb/mcp-server"
  npm_weekly_downloads: 1903
---

# Give MCP agents structured graph memory with RushDB

Connect RushDB’s MCP server so agents can store, search, update, and traverse persistent structured memory without hand-building a separate vector and graph stack.

## Prerequisites

RushDB account or self-hosted RushDB API, RushDB API key, Node.js/npx, and an MCP-compatible client such as ChatGPT, Claude.ai, Claude Desktop, Cursor, Windsurf, VS Code, or Gemini CLI

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
For local stdio MCP clients, add a rushdb MCP server entry that runs npx @rushdb/mcp-server and set RUSHDB_API_KEY in the server environment. For hosted MCP clients that support remote connectors, use the documented RushDB remote MCP endpoint and complete OAuth authorization. Use RUSHDB_API_URL only when pointing the server at a self-hosted or staging RushDB API.
```

## Documentation

- https://github.com/rush-db/rushdb/tree/main/packages/mcp-server

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/give-mcp-agents-structured-graph-memory-with-rushdb/)
