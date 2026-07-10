---
title: "Query Postgres databases through read-only MCP workflows with PGMCP"
description: "Connect an MCP-compatible assistant to an existing PostgreSQL database for safe natural-language querying, schema-aware SQL, and streamed results."
verification: "security_reviewed"
source: "https://github.com/subnetmarco/pgmcp"
author: "subnetmarco"
publisher_type: "individual"
category:
  - "Data Extraction & Transformation"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "subnetmarco/pgmcp"
  github_stars: 529
---

# Query Postgres databases through read-only MCP workflows with PGMCP

Connect an MCP-compatible assistant to an existing PostgreSQL database for safe natural-language querying, schema-aware SQL, and streamed results.

## Prerequisites

PostgreSQL, DATABASE_URL, optional OpenAI API key, MCP-compatible client

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Download a release binary or build with go build -o pgmcp-server ./server, set DATABASE_URL for the target PostgreSQL database, optionally set OPENAI_API_KEY, then run ./pgmcp-server and connect it from an MCP-compatible client.
```

## Documentation

- https://github.com/subnetmarco/pgmcp

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/query-postgres-databases-through-read-only-mcp-workflows-with-pgmcp/)
