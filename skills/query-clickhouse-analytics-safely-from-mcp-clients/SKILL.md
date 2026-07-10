---
title: "Query ClickHouse analytics safely from MCP clients"
description: "Use ClickHouse’s official MCP server when an assistant needs schema-aware, reviewable analytics access to ClickHouse through bounded tools instead of ad hoc database credentials."
verification: "security_reviewed"
source: "https://github.com/ClickHouse/mcp-clickhouse"
author: "ClickHouse"
publisher_type: "official_open_source"
category:
  - "Data Extraction & Transformation"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "ClickHouse/mcp-clickhouse"
  github_stars: 801
---

# Query ClickHouse analytics safely from MCP clients

Use ClickHouse’s official MCP server when an assistant needs schema-aware, reviewable analytics access to ClickHouse through bounded tools instead of ad hoc database credentials.

## Prerequisites

Python runtime or package runner, mcp-clickhouse package, ClickHouse credentials, MCP-capable client

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install the official mcp-clickhouse package, configure ClickHouse connection environment variables, keep write access disabled by default, and register the server with the intended MCP client.
```

## Documentation

- https://github.com/ClickHouse/mcp-clickhouse

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/query-clickhouse-analytics-safely-from-mcp-clients/)
