---
title: "Expose FastAPI routes as MCP tools with FastAPI-MCP"
slug: "expose-fastapi-routes-as-mcp-tools-with-fastapi-mcp"
description: "Mount FastAPI-MCP on an existing FastAPI app so agents can call authenticated route-backed MCP tools with preserved schemas."
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with uv add fastapi-mcp or pip install fastapi-mcp, create FastApiMCP(app), then call mcp.mount() or follow the separate deployment documentation.
```

## Documentation

- https://fastapi-mcp.tadata.com/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/expose-fastapi-routes-as-mcp-tools-with-fastapi-mcp/)
