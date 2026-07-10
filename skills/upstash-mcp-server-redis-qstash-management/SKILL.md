---
name: "Upstash MCP Server for Redis and QStash Management"
slug: "upstash-mcp-server-redis-qstash-management"
description: "An official MCP server from Upstash that lets AI agents manage Redis databases, QStash message queues, and Vector stores through natural language. Supports database creation, key operations, backups, and throughput analytics via the Model Context Protocol."
github_stars: 52
verification: "security_reviewed"
source: "https://github.com/upstash/mcp-server"
author: "upstash"
category: "Integrations & Connectors"
framework: "MCP"
tool_ecosystem:
  github_repo: "upstash/mcp-server"
  github_stars: 52
  npm_package: "@upstash/mcp-server"
  npm_weekly_downloads: 432
---

# Upstash MCP Server for Redis and QStash Management

An official MCP server from Upstash that lets AI agents manage Redis databases, QStash message queues, and Vector stores through natural language. Supports database creation, key operations, backups, and throughput analytics via the Model Context Protocol.

## Installation

Use the upstream install or setup path that matches your environment:
- npx -y @upstash/mcp-server@latest --email YOUR_EMAIL --api-key YOUR_API_KEY

Requirements and caveats from upstream:
- The server sends anonymous diagnostic info to Upstash with each request: the MCP server SDK version, your runtime version (Node, Bun, etc.), and basic platform info (OS and architecture). **No account data, tool argum...

Basic usage or getting-started notes:
- You'll need your Upstash account email and an API key — create one at [Upstash Console → Account → API Keys](https://console.upstash.com/account/api).
- The Upstash MCP server works with any MCP-compatible client. If your client isn't listed below, check its documentation for how to add a stdio MCP server, then point it at the base command:
- bash

- Source: https://github.com/upstash/mcp-server
- Extracted from upstream docs: https://raw.githubusercontent.com/upstash/mcp-server/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/upstash-mcp-server-redis-qstash-management/)
