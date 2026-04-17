---
title: "pgcli Interactive PostgreSQL Client with Autocompletion"
description: "pgcli is a command-line interface for PostgreSQL that provides intelligent autocompletion and syntax highlighting. With over 13,000 GitHub stars, a BSD-3 license, and active maintenance, it is the most popular enhanced PostgreSQL CLI tool available. It is part of the dbcli project, which also produces mycli for MySQL and litecli for SQLite.\nThe autocompletion engine is context-aware. When you type SELECT and press tab, pgcli suggests column names from the tables in your FROM clause. It completes table names, column names, functions, keywords, and even table aliases based on the query context. This dramatically speeds up query writing and reduces typos, especially when working with databases that have hundreds of tables and columns.\nSyntax highlighting makes complex queries easier to read directly in the terminal. SQL keywords, strings, numbers, and identifiers are colored distinctly. Multi-line editing is supported, so you can write and edit complex queries comfortably without reaching for a separate editor. Query history is persistent across sessions and searchable.\npgcli supports all standard PostgreSQL connection methods including TCP, Unix sockets, and connection URIs. It handles SSL connections, multiple databases, and can output results in various formats including CSV, TSV, and formatted tables. Special commands like \\dt for listing tables, \\d+ for describing table structures, and \\e for opening queries in an external editor are all supported.\nFor AI agents that interact with PostgreSQL databases, pgcli provides a more informative and interactive interface than the default psql client. An agent can use it to explore database schemas with autocompletion, inspect table structures, run diagnostic queries, and export results. The tool installs via pip install pgcli or brew install pgcli and requires no additional configuration beyond a database connection string."
verification: security_reviewed
source: "https://github.com/dbcli/pgcli"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "dbcli/pgcli"
  github_stars: 13092
---

# pgcli Interactive PostgreSQL Client with Autocompletion

pgcli is a command-line interface for PostgreSQL that provides intelligent autocompletion and syntax highlighting. With over 13,000 GitHub stars, a BSD-3 license, and active maintenance, it is the most popular enhanced PostgreSQL CLI tool available. It is part of the dbcli project, which also produces mycli for MySQL and litecli for SQLite.
The autocompletion engine is context-aware. When you type SELECT and press tab, pgcli suggests column names from the tables in your FROM clause. It completes table names, column names, functions, keywords, and even table aliases based on the query context. This dramatically speeds up query writing and reduces typos, especially when working with databases that have hundreds of tables and columns.
Syntax highlighting makes complex queries easier to read directly in the terminal. SQL keywords, strings, numbers, and identifiers are colored distinctly. Multi-line editing is supported, so you can write and edit complex queries comfortably without reaching for a separate editor. Query history is persistent across sessions and searchable.
pgcli supports all standard PostgreSQL connection methods including TCP, Unix sockets, and connection URIs. It handles SSL connections, multiple databases, and can output results in various formats including CSV, TSV, and formatted tables. Special commands like \dt for listing tables, \d+ for describing table structures, and \e for opening queries in an external editor are all supported.
For AI agents that interact with PostgreSQL databases, pgcli provides a more informative and interactive interface than the default psql client. An agent can use it to explore database schemas with autocompletion, inspect table structures, run diagnostic queries, and export results. The tool installs via pip install pgcli or brew install pgcli and requires no additional configuration beyond a database connection string.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/pgcli-interactive-postgresql-client
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/pgcli-interactive-postgresql-client` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pgcli-interactive-postgresql-client/)
