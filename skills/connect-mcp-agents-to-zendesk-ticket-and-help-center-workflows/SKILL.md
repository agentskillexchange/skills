---
name: "Connect MCP agents to Zendesk ticket and Help Center workflows"
slug: "connect-mcp-agents-to-zendesk-ticket-and-help-center-workflows"
description: "Expose Zendesk tickets, comments, and Help Center context to MCP-capable agents for supervised support workflow preparation."
github_stars: 95
verification: "listed"
source: "https://github.com/reminia/zendesk-mcp-server"
author: "reminia"
publisher_type: "open_source"
category: "Integrations & Connectors"
framework: "MCP"
tool_ecosystem:
  github_repo: "reminia/zendesk-mcp-server"
  github_stars: 95
---

# Connect MCP agents to Zendesk ticket and Help Center workflows

Expose Zendesk tickets, comments, and Help Center context to MCP-capable agents for supervised support workflow preparation.

## Prerequisites

Zendesk account/API credentials, MCP client, Node.js or runtime required by the repository

## Installation

Use the upstream install or setup path that matches your environment:
- docker build -t zendesk-mcp-server .
- docker run --rm --env-file /path/to/.env zendesk-mcp-server

Requirements and caveats from upstream:
- ### Docker
- "command": "/usr/local/bin/docker",

Basic usage or getting-started notes:
- build: uv venv && uv pip install -e . or uv build in short.
- setup zendesk credentials in .env file, refer to [.env.example](.env.example).
- configure in Claude desktop:

- Source: https://github.com/reminia/zendesk-mcp-server
- Extracted from upstream docs: https://raw.githubusercontent.com/reminia/zendesk-mcp-server/HEAD/README.md

## Documentation

- https://github.com/reminia/zendesk-mcp-server

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/connect-mcp-agents-to-zendesk-ticket-and-help-center-workflows/)
