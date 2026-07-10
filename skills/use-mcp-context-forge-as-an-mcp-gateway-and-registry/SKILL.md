---
name: "Use MCP Context Forge as an MCP gateway and registry"
slug: "use-mcp-context-forge-as-an-mcp-gateway-and-registry"
description: "Put a governed gateway in front of MCP, A2A, REST, and gRPC tools so agent calls can be discovered, routed, observed, and controlled."
github_stars: 3812
verification: "security_reviewed"
source: "https://github.com/IBM/mcp-context-forge"
author: "IBM"
publisher_type: "organization"
category: "Integrations & Connectors"
framework: "MCP"
tool_ecosystem:
  github_repo: "IBM/mcp-context-forge"
  github_stars: 3812
---

# Use MCP Context Forge as an MCP gateway and registry

Put a governed gateway in front of MCP, A2A, REST, and gRPC tools so agent calls can be discovered, routed, observed, and controlled.

## Prerequisites

Python 3.11+, Docker optional, MCP-compatible clients, optional PostgreSQL or Redis for production-style deployment

## Installation

Use the upstream install or setup path that matches your environment:
- pip install --upgrade pip
- pip install mcp-contextforge-gateway
- uv venv
- uv pip install mcp-contextforge-gateway

Requirements and caveats from upstream:
- [![Build Python Package](https://github.com/IBM/mcp-context-forge/actions/workflows/python-package.yml/badge.svg)](https://github.com/IBM/mcp-context-forge/actions/workflows/python-package.yml)&nbsp;
- [![Async](https://img.shields.io/badge/async-await-green.svg)](https://docs.python.org/3/library/asyncio.html)
- [![Docker Image](https://img.shields.io/badge/docker-ghcr.io%2Fibm%2Fmcp--context--forge-blue)](https://github.com/ibm/mcp-context-forge/pkgs/container/mcp-context-forge)&nbsp;

Basic usage or getting-started notes:
- **LLM-specific metrics**: Token usage, costs, model performance
- BASIC_AUTH_PASSWORD=pass \
- MCPGATEWAY_UI_ENABLED=true \

- Source: https://github.com/IBM/mcp-context-forge
- Extracted from upstream docs: https://raw.githubusercontent.com/IBM/mcp-context-forge/HEAD/README.md

## Documentation

- https://ibm.github.io/mcp-context-forge

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/use-mcp-context-forge-as-an-mcp-gateway-and-registry/)
