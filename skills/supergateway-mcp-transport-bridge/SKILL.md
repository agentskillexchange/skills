---
name: "Supergateway MCP Transport Bridge"
slug: "supergateway-mcp-transport-bridge"
description: "Supergateway enables running MCP stdio-based servers over SSE, WebSockets, or Streamable HTTP with a single command. Essential infrastructure for remote MCP server access, debugging, and connecting clients across network boundaries with Docker and OAuth support."
github_stars: 2538
verification: "security_reviewed"
source: "https://github.com/supercorp-ai/supergateway"
category: "Developer Tools"
framework: "MCP"
tool_ecosystem:
  github_repo: "supercorp-ai/supergateway"
  github_stars: 2538
  npm_package: "supergateway"
  npm_weekly_downloads: 88592
---

# Supergateway MCP Transport Bridge

Supergateway enables running MCP stdio-based servers over SSE, WebSockets, or Streamable HTTP with a single command. Essential infrastructure for remote MCP server access, debugging, and connecting clients across network boundaries with Docker and OAuth support.

## Installation

Use the upstream install or setup path that matches your environment:
- npx -y supergateway --stdio "uvx mcp-server-git"
- npx -y supergateway \
- npx -y supergateway --sse "https://mcp-server-ab71a6b2-cd55-49d0-adba-562bc85956e3.supermachine.app"
- npx -y supergateway --streamableHttp "https://mcp-server.example.com/mcp"

Requirements and caveats from upstream:
- ## Running with Docker
- [supercorp/supergateway](https://hub.docker.com/r/supercorp/supergateway). Also on GHCR: [ghcr.io/supercorp-ai/supergateway](https://github.com/supercorp-ai/supergateway/pkgs/container/supergateway)

Basic usage or getting-started notes:
- ![Supergateway: Run stdio MCP servers over SSE and WS](https://raw.githubusercontent.com/supercorp-ai/supergateway/main/supergateway.png)
- Run Supergateway via npx:
- bash

- Source: https://github.com/supercorp-ai/supergateway
- Extracted from upstream docs: https://raw.githubusercontent.com/supercorp-ai/supergateway/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/supergateway-mcp-transport-bridge/)
