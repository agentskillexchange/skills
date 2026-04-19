---
title: "FastMCP Python MCP Server and Client Framework"
description: "FastMCP is the standard framework for building and consuming Model Context Protocol (MCP) applications in Python. Created by Prefect and now downloaded over a million times per day, FastMCP has become the dominant way to build MCP servers across all programming languages — some version of FastMCP powers roughly 70% of MCP servers in production. The framework is built around three pillars. Servers let developers wrap ordinary Python functions into MCP-compliant tools, resources, and prompts. When you decorate a function with @mcp.tool , FastMCP automatically generates the JSON schema, handles input validation, and produces documentation — all from your type hints and docstrings. Clients connect to any MCP server with full protocol support, handling transport negotiation, authentication, and connection lifecycle automatically. Apps give tools interactive UIs rendered directly inside the conversation, enabling richer agent-user interaction. FastMCP supports both STDIO and SSE transports out of the box, making it usable in local development and remote deployment scenarios. It integrates with FastAPI and OpenAPI specifications, allowing developers to expose existing REST APIs as MCP tools with minimal code changes. Server composition and proxying enable building complex multi-server architectures where one FastMCP server routes requests to many downstream servers. Installation is straightforward via pip or uv ( uv pip install fastmcp ). The project provides comprehensive documentation at gofastmcp.com, including an llms.txt file for easy consumption by AI coding assistants. FastMCP 2.0 expanded significantly on the original 1.0 (which was incorporated into the official MCP Python SDK in 2024) by adding client capabilities, server proxying, OpenAPI integration, and advanced composition patterns. Free hosting for FastMCP servers is available through Prefect Horizon."
source: "https://github.com/PrefectHQ/fastmcp"
verification: "security_reviewed"
category:
  - "Developer Tools"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "PrefectHQ/fastmcp"
  github_stars: 24192
---

# FastMCP Python MCP Server and Client Framework

FastMCP is the standard framework for building and consuming Model Context Protocol (MCP) applications in Python. Created by Prefect and now downloaded over a million times per day, FastMCP has become the dominant way to build MCP servers across all programming languages — some version of FastMCP powers roughly 70% of MCP servers in production. The framework is built around three pillars. Servers let developers wrap ordinary Python functions into MCP-compliant tools, resources, and prompts. When you decorate a function with @mcp.tool , FastMCP automatically generates the JSON schema, handles input validation, and produces documentation — all from your type hints and docstrings. Clients connect to any MCP server with full protocol support, handling transport negotiation, authentication, and connection lifecycle automatically. Apps give tools interactive UIs rendered directly inside the conversation, enabling richer agent-user interaction. FastMCP supports both STDIO and SSE transports out of the box, making it usable in local development and remote deployment scenarios. It integrates with FastAPI and OpenAPI specifications, allowing developers to expose existing REST APIs as MCP tools with minimal code changes. Server composition and proxying enable building complex multi-server architectures where one FastMCP server routes requests to many downstream servers. Installation is straightforward via pip or uv ( uv pip install fastmcp ). The project provides comprehensive documentation at gofastmcp.com, including an llms.txt file for easy consumption by AI coding assistants. FastMCP 2.0 expanded significantly on the original 1.0 (which was incorporated into the official MCP Python SDK in 2024) by adding client capabilities, server proxying, OpenAPI integration, and advanced composition patterns. Free hosting for FastMCP servers is available through Prefect Horizon.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/fastmcp-python-mcp-server-client-framework/)
