---
title: "Run approved MCP servers through Docker MCP Gateway"
description: "Use Docker MCP Gateway to run MCP servers in isolated containers, centralize profiles, secrets, tools, and client connections."
verification: "listed"
source: "https://github.com/docker/mcp-gateway"
category:
  - "Integrations & Connectors"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "docker/mcp-gateway"
  github_stars: 1374
---

# Run approved MCP servers through Docker MCP Gateway

Use this skill when an agent/operator needs a controlled MCP operations layer rather than direct per-client server wiring. The workflow is: pull or define MCP server catalog/profile entries, run servers with Docker isolation, enable only the needed tools, manage secrets or OAuth, connect one or more clients to the gateway, and inspect or call tools through the gateway.

Invoke it instead of using Docker or MCP servers normally when the concern is operational control: consistent MCP profiles across clients, container isolation, restricted tool exposure, secret handling, and repeatable gateway startup for agent workflows.

Scope boundary: this is not a general Docker CLI skill and not a generic MCP catalog listing. Keep it to MCP server lifecycle, profile/catalog management, gateway execution, client connection, and tool/secret controls for agent access.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/run-approved-mcp-servers-through-docker-mcp-gateway/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/run-approved-mcp-servers-through-docker-mcp-gateway
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/run-approved-mcp-servers-through-docker-mcp-gateway`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-approved-mcp-servers-through-docker-mcp-gateway/)
