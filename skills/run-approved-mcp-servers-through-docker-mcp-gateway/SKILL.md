---
title: "Run approved MCP servers through Docker MCP Gateway"
slug: "run-approved-mcp-servers-through-docker-mcp-gateway"
description: "Use Docker MCP Gateway to run MCP servers in isolated containers, centralize profiles, secrets, tools, and client connections."
github_stars: 1374
verification: "security_reviewed"
source: "https://github.com/docker/mcp-gateway"
author: "Docker"
publisher_type: "organization"
category: "Integrations & Connectors"
framework: "MCP"
tool_ecosystem:
  github_repo: "docker/mcp-gateway"
  github_stars: 1374
---

# Run approved MCP servers through Docker MCP Gateway

Use Docker MCP Gateway to run MCP servers in isolated containers, centralize profiles, secrets, tools, and client connections.

## Prerequisites

Docker Desktop 4.59+ with MCP Toolkit or Docker CLI plugin, Docker daemon, MCP server catalog/profile

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Use the docker mcp CLI plugin included with recent Docker Desktop MCP Toolkit builds, or clone https://github.com/docker/mcp-gateway, run make docker-mcp, then use docker mcp gateway/profile/catalog/client commands as documented.
```

## Documentation

- https://github.com/docker/mcp-gateway

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-approved-mcp-servers-through-docker-mcp-gateway/)
