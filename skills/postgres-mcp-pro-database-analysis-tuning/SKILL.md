---
name: "Postgres MCP Pro Server for Database Analysis and Tuning"
description: "Postgres MCP Pro is an open-source MCP server that provides AI agents with PostgreSQL database health analysis, index tuning recommendations, query plan optimization, schema intelligence, and safe SQL execution with configurable access controls."
category: "Developer Tools"
framework: "MCP"
verification: security_reviewed
source: "https://github.com/crystaldba/postgres-mcp"
---
# Postgres MCP Pro Server for Database Analysis and Tuning

Postgres MCP Pro is an open-source MCP server that provides AI agents with PostgreSQL database health analysis, index tuning recommendations, query plan optimization, schema intelligence, and safe SQL execution with configurable access controls.

## Overview

Postgres MCP Pro is an open-source Model Context Protocol server built by Crystal DBA specifically for PostgreSQL database management. With over 2,400 GitHub stars and active releases, it goes far beyond wrapping a database connection — providing AI agents with industrial-strength database health analysis, index tuning, query plan optimization, and safe SQL execution throughout the development and production lifecycle.

The server's database health features analyze index health, connection utilization, buffer cache efficiency, vacuum health, sequence limits, replication lag, and other key metrics. Health checks are adapted from PgHero, identifying tuning opportunities and maintenance needs before they become critical issues. Index tuning explores thousands of possible indexes using industrial-strength algorithms to find the optimal solution for a given workload, either analyzing the entire database workload or specific SQL queries (up to 10 at a time).

Query plan analysis validates and optimizes performance by reviewing EXPLAIN plans and simulating the impact of hypothetical indexes before they're created. Schema intelligence provides context-aware SQL generation based on detailed understanding of the database schema, table relationships, and column types. Safe SQL execution supports configurable access control including read-only mode and safe SQL parsing, making the server usable for both development experimentation and production monitoring.

Postgres MCP Pro supports both STDIO and SSE transports. Installation is available via Docker (docker pull crystaldba/postgres-mcp), pipx, or uv. It requires PostgreSQL access credentials and Python 3.12 or higher (for non-Docker installs). The project is MIT-licensed, published on PyPI as postgres-mcp, and works with Claude Desktop, Cursor, and other MCP-compatible clients. For teams managing PostgreSQL databases, it provides AI agents with the same depth of analysis that experienced DBAs bring to performance tuning.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill postgres-mcp-pro-database-analysis-tuning
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill postgres-mcp-pro-database-analysis-tuning -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill postgres-mcp-pro-database-analysis-tuning -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill postgres-mcp-pro-database-analysis-tuning -a codex
```

### OpenClaw

```bash
clawhub install postgres-mcp-pro-database-analysis-tuning
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgres-mcp-pro-database-analysis-tuning/)
