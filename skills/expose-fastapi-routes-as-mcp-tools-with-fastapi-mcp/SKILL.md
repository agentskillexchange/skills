---
title: "Expose FastAPI routes as MCP tools with FastAPI-MCP"
description: "Mount FastAPI-MCP on an existing FastAPI app so agents can call authenticated route-backed MCP tools with preserved schemas."
verification: "listed"
source: "https://github.com/tadata-org/fastapi_mcp"
category:
  - "Integrations & Connectors"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "tadata-org/fastapi_mcp"
  github_stars: 11836
---

# Expose FastAPI routes as MCP tools with FastAPI-MCP

Use this skill when an agent/operator needs to make an existing FastAPI service available as MCP tools without hand-writing wrappers for every endpoint. The workflow is: install FastAPI-MCP, attach it to the FastAPI app, preserve request/response schemas and existing FastAPI auth dependencies, mount or separately deploy the MCP server, then connect an MCP client to the generated tool surface.

Invoke it instead of using the API normally when an agent needs schema-aware, authenticated tool access to internal FastAPI endpoints through MCP, especially for repeated operational or integration workflows.

Scope boundary: this is not a generic FastAPI or OpenAPI converter entry. Keep it to exposing existing FastAPI routes as MCP tools, preserving auth/schema semantics, and validating the resulting MCP endpoint for agent use.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/expose-fastapi-routes-as-mcp-tools-with-fastapi-mcp/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/expose-fastapi-routes-as-mcp-tools-with-fastapi-mcp
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/expose-fastapi-routes-as-mcp-tools-with-fastapi-mcp`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/expose-fastapi-routes-as-mcp-tools-with-fastapi-mcp/)
