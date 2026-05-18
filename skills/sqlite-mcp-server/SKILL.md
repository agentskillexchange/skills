---
name: "SQLite MCP Server"
slug: "sqlite-mcp-server"
description: "Lightweight local database access for agent tasks."
github_stars: 85834
verification: "security_reviewed"
source: "https://github.com/modelcontextprotocol/servers"
author: "Model Context Protocol"
publisher_type: "open_source_collective"
category: "Data Extraction & Transformation"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "modelcontextprotocol/servers"
  github_stars: 85834
---

# SQLite MCP Server

Lightweight local database access for agent tasks.

## Prerequisites

SQLite database file, MCP client/host

## Installation

Use the upstream install or setup path that matches your environment:
- npx -y @modelcontextprotocol/server-memory
- pip install mcp-server-git
- Follow [these](https://docs.astral.sh/uv/getting-started/installation/) instructions to install uv / uvx and [these](https://pip.pypa.io/en/stable/installation/) to install pip.

Requirements and caveats from upstream:
- [Python MCP SDK](https://github.com/modelcontextprotocol/python-sdk)
- **[MCP Plexus](https://github.com/Super-I-Tech/mcp_plexus)**: A secure, **multi-tenant** and Multi-user MCP python server framework built to integrate easily with external services via OAuth 2.1, offering scalable and...
- **[mxcp](https://github.com/raw-labs/mxcp)** (Python) - Open-source framework for building enterprise-grade MCP servers using just YAML, SQL, and Python, with built-in auth, monitoring, ETL and policy enforcement.

Basic usage or getting-started notes:
- The servers in this repository are intended as **reference implementations** to demonstrate MCP features and SDK usage. They are meant to serve as educational examples for developers building their own MCP servers, no...
- **[Fetch](src/fetch)** - Web content fetching and conversion for efficient LLM usage.
- **[mcp.run](https://mcp.run)** - A hosted registry and control plane to install & run secure + portable MCP Servers.

- Source: https://github.com/modelcontextprotocol/servers
- Extracted from upstream docs: https://raw.githubusercontent.com/modelcontextprotocol/servers/HEAD/README.md

## Documentation

- https://github.com/modelcontextprotocol/servers

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sqlite-mcp-server/)
