---
name: "Build authenticated MCP tools and servers with Arcade MCP"
slug: "build-authenticated-mcp-tools-and-servers-with-arcade-mcp"
description: "Use Arcade MCP to create custom MCP servers and tools with OAuth-aware authorization, evals, and deployment paths for agent tool-calling workflows."
github_stars: 895
verification: "security_reviewed"
source: "https://github.com/ArcadeAI/arcade-mcp"
author: "ArcadeAI"
publisher_type: "company"
category: "Integrations & Connectors"
framework: "MCP"
tool_ecosystem:
  github_repo: "ArcadeAI/arcade-mcp"
  github_stars: 895
---

# Build authenticated MCP tools and servers with Arcade MCP

Use Arcade MCP to create custom MCP servers and tools with OAuth-aware authorization, evals, and deployment paths for agent tool-calling workflows.

## Prerequisites

Python, arcade-mcp, an MCP-compatible client, optional Arcade Cloud account for hosted auth and deployment

## Installation

Use the upstream install or setup path that matches your environment:
- uv tool install arcade-mcp
- uv run server.py # stdio (default), for Claude Desktop and CLI tools
- uv run server.py http # HTTP+SSE, for Cursor and VS Code; docs at http://127.0.0.1:8000/docs
- git clone https://github.com/ArcadeAI/arcade-mcp.git

Requirements and caveats from upstream:
- [![Python Version](https://img.shields.io/pypi/pyversions/arcade-mcp)](https://pypi.org/project/arcade-mcp/)
- **Open-source Python framework for building MCP servers and tools.**
- arcade-mcp is the Python framework for building [Model Context Protocol](https://modelcontextprotocol.io) servers and the tools that run inside them. It powers the 7,500+ prebuilt tools across 81 MCP servers at [Arcad...

Basic usage or getting-started notes:
- The secrets (OAuth tokens, API keys, etc) are securely injected by Arcade into your tool call at runtime, so that your tool can authorize requests to upstream APIs, for example. **The client and the LLM never see the...
- bash
- ### Scaffold a new server

- Source: https://github.com/ArcadeAI/arcade-mcp
- Extracted from upstream docs: https://raw.githubusercontent.com/ArcadeAI/arcade-mcp/HEAD/README.md

## Documentation

- https://docs.arcade.dev

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/build-authenticated-mcp-tools-and-servers-with-arcade-mcp/)
