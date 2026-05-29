---
name: "Query Postgres databases through read-only MCP workflows with PGMCP"
slug: "query-postgres-databases-through-read-only-mcp-workflows-with-pgmcp"
description: "Connect an MCP-compatible assistant to an existing PostgreSQL database for safe natural-language querying, schema-aware SQL, and streamed results."
github_stars: 529
verification: "security_reviewed"
source: "https://github.com/subnetmarco/pgmcp"
author: "subnetmarco"
publisher_type: "individual"
category: "Data Extraction & Transformation"
framework: "MCP"
tool_ecosystem:
  github_repo: "subnetmarco/pgmcp"
  github_stars: 529
---

# Query Postgres databases through read-only MCP workflows with PGMCP

Connect an MCP-compatible assistant to an existing PostgreSQL database for safe natural-language querying, schema-aware SQL, and streamed results.

## Prerequisites

PostgreSQL, DATABASE_URL, optional OpenAI API key, MCP-compatible client

## Installation

Use the upstream install or setup path that matches your environment:
- brew tap subnetmarco/homebrew-tap
- brew install pgmcp
- docker run -e DATABASE_URL="postgres://user:pass@host:5432/db" \

Requirements and caveats from upstream:
- ### Docker/Kubernetes
- # Docker
- # Integration tests (requires PostgreSQL)

Basic usage or getting-started notes:
- PGMCP connects to **your existing PostgreSQL database** and makes it accessible to AI assistants through natural language queries.
- PostgreSQL database (existing database with your schema)
- OpenAI API key (optional, for AI-powered SQL generation)

- Source: https://github.com/subnetmarco/pgmcp
- Extracted from upstream docs: https://raw.githubusercontent.com/subnetmarco/pgmcp/HEAD/README.md

## Documentation

- https://github.com/subnetmarco/pgmcp

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/query-postgres-databases-through-read-only-mcp-workflows-with-pgmcp/)
