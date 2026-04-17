---
title: "FastMCP Python MCP Server and Client Framework"
description: "FastMCP is the standard Python framework for building Model Context Protocol servers, clients, and applications. It provides automatic schema generation, transport negotiation, and protocol lifecycle management, letting developers wrap Python functions into MCP-compliant tools with minimal boilerplate."
verification: security_reviewed
source: "https://github.com/PrefectHQ/fastmcp"
category:
  - "Developer Tools"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "PrefectHQ/fastmcp"
  github_stars: 24192
---

# FastMCP Python MCP Server and Client Framework

FastMCP is the standard framework for building and consuming Model Context Protocol (MCP) applications in Python. Created by Prefect and now downloaded over a million times per day, FastMCP has become the dominant way to build MCP servers across all programming languages — some version of FastMCP powers roughly 70% of MCP servers in production.

The framework is built around three pillars. Servers let developers wrap ordinary Python functions into MCP-compliant tools, resources, and prompts. When you decorate a function with @mcp.tool, FastMCP automatically generates the JSON schema, handles input validation, and produces documentation — all from your type hints and docstrings. Clients connect to any MCP server with full protocol support, handling transport negotiation, authentication, and connection lifecycle automatically. Apps give tools interactive UIs rendered directly inside the conversation, enabling richer agent-user interaction.

FastMCP supports both STDIO and SSE transports out of the box, making it usable in local development and remote deployment scenarios. It integrates with FastAPI and OpenAPI specifications, allowing developers to expose existing REST APIs as MCP tools with minimal code changes. Server composition and proxying enable building complex multi-server architectures where one FastMCP server routes requests to many downstream servers.

Installation is straightforward via pip or uv (uv pip install fastmcp). The project provides comprehensive documentation at gofastmcp.com, including an llms.txt file for easy consumption by AI coding assistants. FastMCP 2.0 expanded significantly on the original 1.0 (which was incorporated into the official MCP Python SDK in 2024) by adding client capabilities, server proxying, OpenAPI integration, and advanced composition patterns. Free hosting for FastMCP servers is available through Prefect Horizon.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/fastmcp-python-mcp-server-client-framework
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/fastmcp-python-mcp-server-client-framework` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/fastmcp-python-mcp-server-client-framework/)
