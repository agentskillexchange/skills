---
title: "pgcli Interactive PostgreSQL Client with Autocompletion"
description: "pgcli is an interactive PostgreSQL CLI with context-aware autocompletion, syntax highlighting, and multi-line query editing. Part of the dbcli project with 13k+ GitHub stars, it makes database exploration and query writing dramatically more productive."
slug: "pgcli-interactive-postgresql-client"
category:
  - "Developer Tools"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://github.com/dbcli/pgcli"
tool_ecosystem:
  github_repo: "dbcli/pgcli"
  github_stars: 13092
---

# pgcli Interactive PostgreSQL Client with Autocompletion

pgcli is an interactive PostgreSQL CLI with context-aware autocompletion, syntax highlighting, and multi-line query editing. Part of the dbcli project with 13k+ GitHub stars, it makes database exploration and query writing dramatically more productive.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install pgcli-interactive-postgresql-client
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

pgcli is a command-line interface for PostgreSQL that provides intelligent autocompletion and syntax highlighting. With over 13,000 GitHub stars, a BSD-3 license, and active maintenance, it is the most popular enhanced PostgreSQL CLI tool available. It is part of the dbcli project, which also produces mycli for MySQL and litecli for SQLite.
The autocompletion engine is context-aware. When you type SELECT and press tab, pgcli suggests column names from the tables in your FROM clause. It completes table names, column names, functions, keywords, and even table aliases based on the query context. This dramatically speeds up query writing and reduces typos, especially when working with databases that have hundreds of tables and columns.
Syntax highlighting makes complex queries easier to read directly in the terminal. SQL keywords, strings, numbers, and identifiers are colored distinctly. Multi-line editing is supported, so you can write and edit complex queries comfortably without reaching for a separate editor. Query history is persistent across sessions and searchable.
pgcli supports all standard PostgreSQL connection methods including TCP, Unix sockets, and connection URIs. It handles SSL connections, multiple databases, and can output results in various formats including CSV, TSV, and formatted tables. Special commands like \dt for listing tables, \d+ for describing table structures, and \e for opening queries in an external editor are all supported.
For AI agents that interact with PostgreSQL databases, pgcli provides a more informative and interactive interface than the default psql client. An agent can use it to explore database schemas with autocompletion, inspect table structures, run diagnostic queries, and export results. The tool installs via pip install pgcli or brew install pgcli and requires no additional configuration beyond a database connection string.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pgcli-interactive-postgresql-client/)
