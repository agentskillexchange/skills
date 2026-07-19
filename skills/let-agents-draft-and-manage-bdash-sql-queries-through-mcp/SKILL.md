---
name: "Let agents draft and manage Bdash SQL queries through MCP"
slug: "let-agents-draft-and-manage-bdash-sql-queries-through-mcp"
description: "Connect Bdash's SQL workspace to MCP clients so an agent can list configured data sources and write SQL into the active query editor for supervised analysis."
github_stars: 1516
verification: "security_reviewed"
source: "https://github.com/bdash-app/bdash"
author: "bdash-app"
publisher_type: "organization"
category: "Data Extraction & Transformation"
framework: "MCP"
tool_ecosystem:
  github_repo: "bdash-app/bdash"
  github_stars: 1516
---

# Let agents draft and manage Bdash SQL queries through MCP

Connect Bdash's SQL workspace to MCP clients so an agent can list configured data sources and write SQL into the active query editor for supervised analysis.

## Prerequisites

Bdash desktop app, bundled Bdash MCP server, Node.js, Claude Code or another MCP-compatible client

## Installation

Use the upstream install or setup path that matches your environment:
- yarn mcp:install
- yarn mcp:build
- $ yarn
- $ yarn watch

Requirements and caveats from upstream:
- "command": "node",
- Publishing a release also triggers the website deployment workflow in bdash-app/bdash-app.github.io, so the download version on the website is updated from the latest release. This requires a GitHub App installed on t...

Basic usage or getting-started notes:
- Add to your Claude Code MCP settings (.claude/settings.json or project-level):
- {
- "mcpServers": {

- Source: https://github.com/bdash-app/bdash
- Extracted from upstream docs: https://raw.githubusercontent.com/bdash-app/bdash/HEAD/README.md

## Documentation

- https://github.com/bdash-app/bdash

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/let-agents-draft-and-manage-bdash-sql-queries-through-mcp/)
