---
name: "Turn an MCP, OpenAPI, or GraphQL endpoint into a disposable CLI for shell automation"
slug: "turn-mcp-openapi-or-graphql-endpoint-into-disposable-cli-for-shell-automation"
description: "Generate a shell-ready CLI from an MCP server, OpenAPI spec, or GraphQL endpoint so an agent can discover commands and call tools immediately without hand-written wrappers."
github_stars: 1940
verification: "listed"
source: "https://github.com/knowsuchagency/mcp2cli"
author: "Knowsuch Agency"
publisher_type: "company"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "knowsuchagency/mcp2cli"
  github_stars: 1940
---

# Turn an MCP, OpenAPI, or GraphQL endpoint into a disposable CLI for shell automation

Generate a shell-ready CLI from an MCP server, OpenAPI spec, or GraphQL endpoint so an agent can discover commands and call tools immediately without hand-written wrappers.

## Prerequisites

Python with uv or uvx, network access to the target MCP/OpenAPI/GraphQL endpoint, and any required auth headers or OAuth credentials for that endpoint.

## Installation

Use the upstream install or setup path that matches your environment:
- uv tool install mcp2cli
- npx skills add knowsuchagency/mcp2cli --skill mcp2cli
- uv sync --extra test
- uv run pytest tests/ -v

Requirements and caveats from upstream:
- APIs that require OAuth are supported out of the box — across MCP, OpenAPI, and GraphQL modes.
- mcp2cli --mcp-stdio "node server.js" --env API_KEY=sk-... --env DEBUG=1 \

Basic usage or getting-started notes:
- bash
- # Run directly without installing
- uvx mcp2cli --help

- Source: https://github.com/knowsuchagency/mcp2cli
- Extracted from upstream docs: https://raw.githubusercontent.com/knowsuchagency/mcp2cli/HEAD/README.md

## Documentation

- https://github.com/knowsuchagency/mcp2cli

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/turn-mcp-openapi-or-graphql-endpoint-into-disposable-cli-for-shell-automation/)
