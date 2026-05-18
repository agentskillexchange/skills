---
name: "Run approved MCP servers through Docker MCP Gateway"
slug: "run-approved-mcp-servers-through-docker-mcp-gateway"
description: "Use Docker MCP Gateway to run MCP servers in isolated containers, centralize profiles, secrets, tools, and client connections."
github_stars: 1374
verification: "listed"
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

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/docker/mcp-gateway.git
- make docker-mcp
- docker mcp --help
- docker mcp feature enable profiles

Requirements and caveats from upstream:
- # Docker MCP Plugin and Docker MCP Gateway
- ![build](https://github.com/docker/mcp-gateway/actions/workflows/ci.yml/badge.svg)
- The [MCP Toolkit](https://docs.docker.com/ai/mcp-catalog-and-toolkit/toolkit/), in Docker Desktop, allows

Basic usage or getting-started notes:
- <div align="left">
- <img src="./img/enable_toolkit.png" width="400"/>
- </div>

- Source: https://github.com/docker/mcp-gateway
- Extracted from upstream docs: https://raw.githubusercontent.com/docker/mcp-gateway/HEAD/README.md

## Documentation

- https://github.com/docker/mcp-gateway

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-approved-mcp-servers-through-docker-mcp-gateway/)
