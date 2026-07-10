---
name: "Query ClickHouse analytics safely from MCP clients"
slug: "query-clickhouse-analytics-safely-from-mcp-clients"
description: "Use ClickHouse's official MCP server when an assistant needs schema-aware, reviewable analytics access to ClickHouse through bounded tools instead of ad hoc database credentials."
github_stars: 801
verification: "security_reviewed"
source: "https://github.com/ClickHouse/mcp-clickhouse"
author: "ClickHouse"
publisher_type: "official_open_source"
category: "Data Extraction & Transformation"
framework: "MCP"
tool_ecosystem:
  github_repo: "ClickHouse/mcp-clickhouse"
  github_stars: 801
---

# Query ClickHouse analytics safely from MCP clients

Use ClickHouse's official MCP server when an assistant needs schema-aware, reviewable analytics access to ClickHouse through bounded tools instead of ad hoc database credentials.

## Prerequisites

Python runtime or package runner, mcp-clickhouse package, ClickHouse credentials, MCP-capable client

## Installation

Use the upstream install or setup path that matches your environment:
- In test-services directory run docker compose up -d to start the ClickHouse cluster.
- Run uv sync to install the dependencies. To install uv follow the instructions [here](https://docs.astral.sh/uv/). Then do source .venv/bin/activate.
- uv sync --all-extras --dev # install dev dependencies
- uv run ruff check . # run linting

Requirements and caveats from upstream:
- Requires the optional chdb extra: pip install 'mcp-clickhouse[chdb]'
- When using HTTP or SSE transport, authentication is **required by default**. The stdio transport (default) does not require authentication as it only communicates via standard input/output.
- "--python",

Basic usage or getting-started notes:
- Queries run in read-only mode by default (CLICKHOUSE_ALLOW_WRITE_ACCESS=false), but writes can be enabled explicitly if needed.
- Example:
- Example (Azure Entra):

- Source: https://github.com/ClickHouse/mcp-clickhouse
- Extracted from upstream docs: https://raw.githubusercontent.com/ClickHouse/mcp-clickhouse/HEAD/README.md

## Documentation

- https://github.com/ClickHouse/mcp-clickhouse

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/query-clickhouse-analytics-safely-from-mcp-clients/)
