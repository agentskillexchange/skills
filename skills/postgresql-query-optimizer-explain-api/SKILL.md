---
name: "PostgreSQL Query Optimizer Agent"
slug: "postgresql-query-optimizer-explain-api"
description: "Optimizes PostgreSQL queries using EXPLAIN ANALYZE output parsing with pg_stat_statements extension data. Suggests index creation via HypoPG hypothetical index simulator and validates query plans against pg_hint_plan directives."
github_stars: 13127
verification: "listed"
source: "https://github.com/brianc/node-postgres"
category: "Developer Tools"
framework: "OpenClaw"
tool_ecosystem:
  github_repo: "brianc/node-postgres"
  github_stars: 13127
  npm_package: "pg"
  npm_weekly_downloads: 23169914
---

# PostgreSQL Query Optimizer Agent

Optimizes PostgreSQL queries using EXPLAIN ANALYZE output parsing with pg_stat_statements extension data. Suggests index creation via HypoPG hypothetical index simulator and validates query plans against pg_hint_plan directives.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgresql-query-optimizer-explain-api/)
