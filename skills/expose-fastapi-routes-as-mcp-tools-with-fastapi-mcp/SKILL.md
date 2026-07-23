---
name: "Expose FastAPI routes as MCP tools with FastAPI-MCP"
slug: "expose-fastapi-routes-as-mcp-tools-with-fastapi-mcp"
description: "Mount FastAPI-MCP on an existing FastAPI app so agents can call authenticated route-backed MCP tools with preserved schemas."
github_stars: 11836
verification: "security_reviewed"
source: "https://github.com/tadata-org/fastapi_mcp"
author: "Tadata"
publisher_type: "organization"
category: "Integrations & Connectors"
framework: "MCP"
tool_ecosystem:
  github_repo: "tadata-org/fastapi_mcp"
  github_stars: 11836
---

# Expose FastAPI routes as MCP tools with FastAPI-MCP

Mount FastAPI-MCP on an existing FastAPI app so agents can call authenticated route-backed MCP tools with preserved schemas.

## Prerequisites

Python 3.10+, FastAPI application, fastapi-mcp package, MCP-capable client

## Installation

Install with uv, as recommended upstream:

- uv add fastapi-mcp

Alternatively, install with pip:

- pip install fastapi-mcp

After mounting FastAPI-MCP in your app, the generated MCP server is available at your app base URL plus /mcp.

- Source: https://github.com/tadata-org/fastapi_mcp
- Extracted from upstream docs: https://raw.githubusercontent.com/tadata-org/fastapi_mcp/HEAD/README.md

## Documentation

- https://fastapi-mcp.tadata.com/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/expose-fastapi-routes-as-mcp-tools-with-fastapi-mcp/)
