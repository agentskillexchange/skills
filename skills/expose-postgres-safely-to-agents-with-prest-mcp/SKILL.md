---
name: "Expose Postgres safely to agents with pREST MCP"
slug: "expose-postgres-safely-to-agents-with-prest-mcp"
description: "Run pREST in front of existing Postgres databases to provide instant REST APIs and a read-only MCP endpoint with auth, ACL, custom SQL routes, and multi-database support."
github_stars: 4596
verification: "security_reviewed"
source: "https://github.com/prest/prest"
author: "pREST"
publisher_type: "organization"
category: "Data Extraction & Transformation"
framework: "MCP"
tool_ecosystem:
  github_repo: "prest/prest"
  github_stars: 4596
---

# Expose Postgres safely to agents with pREST MCP

Run pREST in front of existing Postgres databases to provide instant REST APIs and a read-only MCP endpoint with auth, ACL, custom SQL routes, and multi-database support.

## Prerequisites

pRESTd; PostgreSQL 9.5+; database connection configuration; optional Docker, Homebrew, or Go install path; MCP-capable AI client

## Installation

Use the upstream install or setup path that matches your environment:
- make test-unit
- make test-integration-postgres
- make test-integration-timescaledb
- docker compose -f integration/postgres/docker-compose.yml up -d --wait \

Requirements and caveats from upstream:
- | Get pREST (Docker, Homebrew, Go) | [Get pREST](https://docs.prestd.com/get-prest) |
- Run integration suites inside Docker (no local Postgres required):
- Or with Docker Compose:

Basic usage or getting-started notes:
- http
- GET /{database}/{schema}/{table}
- See [Configuring pREST](https://docs.prestd.com/get-started/configuring-prest) for auth, ACL, custom queries, and MCP.

- Source: https://github.com/prest/prest
- Extracted from upstream docs: https://raw.githubusercontent.com/prest/prest/HEAD/README.md

## Documentation

- https://docs.prestd.com/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/expose-postgres-safely-to-agents-with-prest-mcp/)
