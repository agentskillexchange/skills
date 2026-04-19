---
title: "Postgres MCP Pro Server for Database Analysis and Tuning"
description: "Postgres MCP Pro is an open-source Model Context Protocol server built by Crystal DBA specifically for PostgreSQL database management. With over 2,400 GitHub stars and active releases, it goes far beyond wrapping a database connection — providing AI agents with industrial-strength database health analysis, index tuning, query plan optimization, and safe SQL execution throughout the development and production lifecycle. The server&#8217;s database health features analyze index health, connection utilization, buffer cache efficiency, vacuum health, sequence limits, replication lag, and other key metrics. Health checks are adapted from PgHero, identifying tuning opportunities and maintenance needs before they become critical issues. Index tuning explores thousands of possible indexes using industrial-strength algorithms to find the optimal solution for a given workload, either analyzing the entire database workload or specific SQL queries (up to 10 at a time). Query plan analysis validates and optimizes performance by reviewing EXPLAIN plans and simulating the impact of hypothetical indexes before they&#8217;re created. Schema intelligence provides context-aware SQL generation based on detailed understanding of the database schema, table relationships, and column types. Safe SQL execution supports configurable access control including read-only mode and safe SQL parsing, making the server usable for both development experimentation and production monitoring. Postgres MCP Pro supports both STDIO and SSE transports. Installation is available via Docker ( docker pull crystaldba/postgres-mcp ), pipx, or uv. It requires PostgreSQL access credentials and Python 3.12 or higher (for non-Docker installs). The project is MIT-licensed, published on PyPI as postgres-mcp , and works with Claude Desktop, Cursor, and other MCP-compatible clients. For teams managing PostgreSQL databases, it provides AI agents with the same depth of analysis that experienced DBAs bring to performance tuning."
source: "https://github.com/crystaldba/postgres-mcp"
verification: "security_reviewed"
category:
  - "Developer Tools"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "crystaldba/postgres-mcp"
  github_stars: 2464
---

# Postgres MCP Pro Server for Database Analysis and Tuning

Postgres MCP Pro is an open-source Model Context Protocol server built by Crystal DBA specifically for PostgreSQL database management. With over 2,400 GitHub stars and active releases, it goes far beyond wrapping a database connection — providing AI agents with industrial-strength database health analysis, index tuning, query plan optimization, and safe SQL execution throughout the development and production lifecycle. The server&#8217;s database health features analyze index health, connection utilization, buffer cache efficiency, vacuum health, sequence limits, replication lag, and other key metrics. Health checks are adapted from PgHero, identifying tuning opportunities and maintenance needs before they become critical issues. Index tuning explores thousands of possible indexes using industrial-strength algorithms to find the optimal solution for a given workload, either analyzing the entire database workload or specific SQL queries (up to 10 at a time). Query plan analysis validates and optimizes performance by reviewing EXPLAIN plans and simulating the impact of hypothetical indexes before they&#8217;re created. Schema intelligence provides context-aware SQL generation based on detailed understanding of the database schema, table relationships, and column types. Safe SQL execution supports configurable access control including read-only mode and safe SQL parsing, making the server usable for both development experimentation and production monitoring. Postgres MCP Pro supports both STDIO and SSE transports. Installation is available via Docker ( docker pull crystaldba/postgres-mcp ), pipx, or uv. It requires PostgreSQL access credentials and Python 3.12 or higher (for non-Docker installs). The project is MIT-licensed, published on PyPI as postgres-mcp , and works with Claude Desktop, Cursor, and other MCP-compatible clients. For teams managing PostgreSQL databases, it provides AI agents with the same depth of analysis that experienced DBAs bring to performance tuning.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/postgres-mcp-pro-database-analysis-tuning/)
