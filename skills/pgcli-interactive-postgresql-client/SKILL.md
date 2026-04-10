---
name: pgcli Interactive PostgreSQL Client with Autocompletion
description: pgcli is an interactive PostgreSQL CLI with context-aware autocompletion,
  syntax highlighting, and multi-line query editing. Part of the dbcli project with
  13k+ GitHub stars, it makes database exploration and query writing dramatically
  more productive.
verification: security_reviewed
source: https://github.com/dbcli/pgcli
category:
- Developer Tools
framework:
- OpenClaw
tool_ecosystem:
  github_repo: dbcli/pgcli
  github_stars: 13092
---
# pgcli Interactive PostgreSQL Client with Autocompletion

pgcli is a command-line interface for PostgreSQL that provides intelligent autocompletion and syntax highlighting. With over 13,000 GitHub stars, a BSD-3 license, and active maintenance, it is the most popular enhanced PostgreSQL CLI tool available. It is part of the dbcli project, which also produces mycli for MySQL and litecli for SQLite.
The autocompletion engine is context-aware. When you type SELECT and press tab, pgcli suggests column names from the tables in your FROM clause. It completes table names, column names, functions, keywords, and even table aliases based on the query context. This dramatically speeds up query writing and reduces typos, especially when working with databases that have hundreds of tables and columns.
Syntax highlighting makes complex queries easier to read directly in the terminal. SQL keywords, strings, numbers, and identifiers are colored distinctly. Multi-line editing is supported, so you can write and edit complex queries comfortably without reaching for a separate editor. Query history is persistent across sessions and searchable.
pgcli supports all standard PostgreSQL connection methods including TCP, Unix sockets, and connection URIs. It handles SSL connections, multiple databases, and can output results in various formats including CSV, TSV, and formatted tables. Special commands like \dt for listing tables, \d+ for describing table structures, and \e for opening queries in an external editor are all supported.
For AI agents that interact with PostgreSQL databases, pgcli provides a more informative and interactive interface than the default psql client. An agent can use it to explore database schemas with autocompletion, inspect table structures, run diagnostic queries, and export results. The tool installs via pip install pgcli or brew install pgcli and requires no additional configuration beyond a database connection string.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pgcli-interactive-postgresql-client/)
