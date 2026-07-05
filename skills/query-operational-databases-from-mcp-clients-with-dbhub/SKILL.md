---
name: "Query operational databases from MCP clients with DBHub"
slug: "query-operational-databases-from-mcp-clients-with-dbhub"
description: "Use DBHub to expose guarded, token-efficient database inspection and SQL tools to MCP clients across Postgres, MySQL, SQL Server, MariaDB, and SQLite."
github_stars: 3102
verification: "security_reviewed"
source: "https://github.com/bytebase/dbhub"
author: "Bytebase"
publisher_type: "open_source_vendor"
category: "Data Extraction & Transformation"
framework: "MCP"
tool_ecosystem:
  github_repo: "bytebase/dbhub"
  github_stars: 3102
  npm_package: "@bytebase/dbhub"
  npm_weekly_downloads: 78816
---

# Query operational databases from MCP clients with DBHub

Use DBHub to expose guarded, token-efficient database inspection and SQL tools to MCP clients across Postgres, MySQL, SQL Server, MariaDB, and SQLite.

## Prerequisites

Node.js 22.5 or newer or Docker, database DSN/configuration, MCP-compatible client

## Installation

Use the upstream install or setup path that matches your environment:
- docker run --rm --init \
- npx @bytebase/dbhub@latest --transport http --port 8080 --dsn "postgres://user:password@localhost:5432/dbname?sslmode=disable"
- npx @bytebase/dbhub@latest --transport http --port 8080 --demo
- npx @bytebase/dbhub@latest --transport http --host 127.0.0.1 --port 8080 --demo

Requirements and caveats from upstream:
- **Docker:**
- **NPM:** (requires Node.js >= 22.5.0)
- Requires Node.js >= 22.5.0 (DBHub uses the built-in node:sqlite module).

Basic usage or getting-started notes:
- DBHub includes a [built-in web interface](https://dbhub.ai/workbench/overview) for interacting with your database tools. It provides a visual way to execute queries, run custom tools, and view request traces without r...
- See the full [Installation Guide](https://dbhub.ai/installation) for detailed instructions.
- --name dbhub \

- Source: https://github.com/bytebase/dbhub
- Extracted from upstream docs: https://raw.githubusercontent.com/bytebase/dbhub/HEAD/README.md

## Documentation

- https://dbhub.ai

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/query-operational-databases-from-mcp-clients-with-dbhub/)
