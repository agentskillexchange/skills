---
title: "Inspect and debug MCP servers visually before connecting them to agents"
description: "Use MCP Inspector when you need to launch an MCP server, inspect its tools and resources, exercise calls manually, and troubleshoot transport or schema issues before putting that server in front of real agents."
verification: "listed"
source: "https://github.com/modelcontextprotocol/inspector"
author: "Model Context Protocol"
publisher_type: "organization"
category:
  - "Developer Tools"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "modelcontextprotocol/inspector"
  github_stars: 9431
  npm_package: "@modelcontextprotocol/inspector"
  npm_weekly_downloads: 635249
---

# Inspect and debug MCP servers visually before connecting them to agents

Use MCP Inspector when you need to launch an MCP server, inspect its tools and resources, exercise calls manually, and troubleshoot transport or schema issues before putting that server in front of real agents.

## Prerequisites

Node.js or Docker, MCP Inspector, and a target MCP server command or endpoint to inspect

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Run `npx @modelcontextprotocol/inspector` to open the local inspector UI, then launch your target MCP server through the inspector by passing its command, arguments, and optional environment variables, or use the published Docker image if preferred.
```

## Documentation

- https://modelcontextprotocol.io

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/inspect-and-debug-mcp-servers-visually-before-connecting-them-to-agents/)
