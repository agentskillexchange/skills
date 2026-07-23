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

Install Bdash from the official website or GitHub Releases.

For development MCP setup from a cloned repository, upstream documents running yarn mcp:install and then yarn mcp:build.

For Claude Code, add the MCP server to .claude/settings.json or a project-level MCP settings file with command node and args pointing to src/mcp/dist/server.js. For the bundled macOS app, point args to /Applications/Bdash.app/Contents/Resources/mcp/server.js.

- Source: https://github.com/bdash-app/bdash
- Extracted from upstream docs: https://raw.githubusercontent.com/bdash-app/bdash/HEAD/README.md

## Documentation

- https://github.com/bdash-app/bdash

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/let-agents-draft-and-manage-bdash-sql-queries-through-mcp/)
