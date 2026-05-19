---
name: "PostgreSQL Query Plan Analyzer"
slug: "postgresql-query-plan-analyzer-2"
description: "Executes EXPLAIN ANALYZE BUFFERS on slow PostgreSQL queries and parses the plan tree for sequential scans, nested loop joins, and sort spills. Integrates with pg_stat_statements for identifying top resource-consuming queries."
github_stars: 13127
verification: "security_reviewed"
source: "https://github.com/brianc/node-postgres"
category: "Developer Tools"
framework: "MCP"
tool_ecosystem:
  github_repo: "brianc/node-postgres"
  github_stars: 13127
  npm_package: "pg"
  npm_weekly_downloads: 23169914
---

# PostgreSQL Query Plan Analyzer

Executes EXPLAIN ANALYZE BUFFERS on slow PostgreSQL queries and parses the plan tree for sequential scans, nested loop joins, and sort spills. Integrates with pg_stat_statements for identifying top resource-consuming queries.

## Installation

Use the upstream install or setup path that matches your environment:
- npm install pg
- From your workspace root run yarn and then yarn lerna bootstrap
- Run yarn test to run all the tests.

Requirements and caveats from upstream:
- # node-postgres
- ![Build Status](https://github.com/brianc/node-postgres/actions/workflows/ci.yml/badge.svg)
- Non-blocking PostgreSQL client for Node.js. Pure JavaScript and optional native libpq bindings.

Basic usage or getting-started notes:
- ## Documentation
- Each package in this repo should have its own readme more focused on how to develop/contribute. For overall documentation on the project and the related modules managed by this repo please see:
- ### Features

- Source: https://github.com/brianc/node-postgres
- Extracted from upstream docs: https://raw.githubusercontent.com/brianc/node-postgres/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-query-plan-analyzer-2/)
