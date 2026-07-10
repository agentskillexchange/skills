---
title: "Query operational databases from MCP clients with DBHub"
description: "Use DBHub to expose guarded, token-efficient database inspection and SQL tools to MCP clients across Postgres, MySQL, SQL Server, MariaDB, and SQLite."
verification: "security_reviewed"
source: "https://github.com/bytebase/dbhub"
author: "Bytebase"
publisher_type: "open_source_vendor"
category:
  - "Data Extraction & Transformation"
framework:
  - "MCP"
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Run with npx @bytebase/dbhub@latest --transport http --port 8080 --dsn or use the documented Docker image; configure read-only mode, row limits, timeouts, SSH/SSL, and custom tools as appropriate before exposing it to an MCP client.
```

## Documentation

- https://dbhub.ai

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/query-operational-databases-from-mcp-clients-with-dbhub/)
