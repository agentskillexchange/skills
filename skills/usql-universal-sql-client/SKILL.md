---
name: usql Universal Command-Line SQL Client for Multiple Databases
description: usql is a universal command-line interface for SQL databases including
  PostgreSQL, MySQL, SQLite, Oracle, SQL Server, and dozens more. It provides a consistent
  psql-like experience with syntax highlighting, tab completion, and cross-database
  copying.
verification: security_reviewed
source: https://github.com/xo/usql
category:
- Developer Tools
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: xo/usql
  github_stars: 9901
  license: MIT
---
# usql Universal Command-Line SQL Client for Multiple Databases

Overview
usql is a universal command-line interface for working with SQL and NoSQL databases. Inspired by PostgreSQL's psql, usql provides a unified experience for querying PostgreSQL, MySQL, SQLite3, Oracle Database, Microsoft SQL Server, CockroachDB, ClickHouse, Cassandra, and over 50 other database engines — all from a single binary.
Key Features
usql supports backslash commands familiar to psql users (\d for describe, \l for list databases, \dt for tables, \c for connect), variables, backtick execution, and has additional capabilities psql lacks: cross-database copying with \copy, syntax highlighting, context-based tab completion, and terminal graphics output including charts and plots directly in the terminal.
How It Works
usql uses standard database connection URLs to connect to any supported database. For PostgreSQL: usql postgres://user:pass@host/dbname. For MySQL: usql mysql://user:pass@host/dbname. For SQLite: usql file:local.db. Once connected, you get a REPL with full SQL support, query history, and output formatting options including CSV, JSON, and table formats.
Cross-Database Operations
One of usql's standout features is the ability to copy data between different database engines. Using the \copy command, you can transfer tables from PostgreSQL to MySQL, SQLite to Oracle, or any combination of supported databases. This makes usql invaluable for data migration tasks and cross-database ETL workflows.
Installation
Install via Homebrew: brew install xo/xo/usql. Via Go: go install github.com/xo/usql@latest. Via Docker: docker run --rm -it docker.io/usql/usql. Binary releases are available for Linux, macOS, and Windows on GitHub. The tool is written in Go and compiles to a single binary with drivers for all supported databases.
Agent Integration
Agents can use usql as a single tool to query any database without needing separate client CLIs for each database engine. The consistent interface means agents only need to learn one command syntax to work with PostgreSQL, MySQL, SQLite, and dozens of other databases. Combined with JSON output mode, usql output can be directly parsed by agents for data extraction and analysis tasks.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/usql-universal-sql-client/)
