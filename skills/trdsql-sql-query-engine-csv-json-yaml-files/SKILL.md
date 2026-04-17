---
title: "trdsql SQL Query Engine for CSV JSON and YAML Files"
description: "What is trdsql?\ntrdsql is a command-line tool written in Go that lets you run SQL queries against structured data files without loading them into a database first. Created by Noboru Saito, it has over 2,100 GitHub stars, is licensed under MIT, and provides pre-built binaries for Linux, macOS, and Windows. It is installable via Homebrew, MacPorts, FreeBSD ports, and Go install.\nHow It Works\ntrdsql treats files as SQL tables. You reference a filename in your SQL query, and trdsql automatically detects the format (CSV, JSON, LTSV, YAML, or TBLN) and loads it into an embedded SQLite database for query execution. The key differentiator from similar tools like q or textql is that trdsql supports PostgreSQL and MySQL syntax through optional database driver connections, allowing you to use the full power of these SQL dialects including their built-in functions.\nYou can query from stdin, local files, compressed files (gzip, bzip2, zstd, lz4, xz), and even join data across multiple files or between files and actual database tables. Input format detection is automatic but can be overridden with flags. JSON input supports jq-style path expressions for nested data. The tool handles files where column counts vary across rows and supports both header-based and positional column references.\nOutput Formats\ntrdsql outputs query results in CSV, LTSV, JSON, JSONL (NDJSON), YAML, TBLN, Markdown tables, ASCII tables, raw text, and vertical format. Output can be compressed and written to files. Format guessing by output filename extension is supported. This makes trdsql a Swiss Army knife for data transformation between formats — query JSON, output CSV, or vice versa.\nIntegration Points\ntrdsql works well in shell pipelines, accepting input from stdin and outputting to stdout. It can connect to PostgreSQL and MySQL databases, making it possible to join CSV data with live database tables in a single query. Configuration files allow persistent database connection settings. As a Go library, it can be embedded in other applications for programmatic SQL-on-files functionality."
verification: security_reviewed
source: "https://github.com/noborus/trdsql"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "noborus/trdsql"
  github_stars: 2154
---

# trdsql SQL Query Engine for CSV JSON and YAML Files

What is trdsql?
trdsql is a command-line tool written in Go that lets you run SQL queries against structured data files without loading them into a database first. Created by Noboru Saito, it has over 2,100 GitHub stars, is licensed under MIT, and provides pre-built binaries for Linux, macOS, and Windows. It is installable via Homebrew, MacPorts, FreeBSD ports, and Go install.
How It Works
trdsql treats files as SQL tables. You reference a filename in your SQL query, and trdsql automatically detects the format (CSV, JSON, LTSV, YAML, or TBLN) and loads it into an embedded SQLite database for query execution. The key differentiator from similar tools like q or textql is that trdsql supports PostgreSQL and MySQL syntax through optional database driver connections, allowing you to use the full power of these SQL dialects including their built-in functions.
You can query from stdin, local files, compressed files (gzip, bzip2, zstd, lz4, xz), and even join data across multiple files or between files and actual database tables. Input format detection is automatic but can be overridden with flags. JSON input supports jq-style path expressions for nested data. The tool handles files where column counts vary across rows and supports both header-based and positional column references.
Output Formats
trdsql outputs query results in CSV, LTSV, JSON, JSONL (NDJSON), YAML, TBLN, Markdown tables, ASCII tables, raw text, and vertical format. Output can be compressed and written to files. Format guessing by output filename extension is supported. This makes trdsql a Swiss Army knife for data transformation between formats — query JSON, output CSV, or vice versa.
Integration Points
trdsql works well in shell pipelines, accepting input from stdin and outputting to stdout. It can connect to PostgreSQL and MySQL databases, making it possible to join CSV data with live database tables in a single query. Configuration files allow persistent database connection settings. As a Go library, it can be embedded in other applications for programmatic SQL-on-files functionality.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/trdsql-sql-query-engine-csv-json-yaml-files
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/trdsql-sql-query-engine-csv-json-yaml-files` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/trdsql-sql-query-engine-csv-json-yaml-files/)
