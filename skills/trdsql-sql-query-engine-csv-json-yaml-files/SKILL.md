---
title: "trdsql SQL Query Engine for CSV JSON and YAML Files"
description: "trdsql is a CLI tool that executes SQL queries directly on CSV, LTSV, JSON, YAML, and TBLN files. It supports PostgreSQL and MySQL syntax, can join data across multiple files and databases, and outputs results in various formats including JSON, Markdown, and vertical display."
verification: security_reviewed
source: "https://github.com/noborus/trdsql"
category:
  - "Data Extraction &amp; Transformation"
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/trdsql-sql-query-engine-csv-json-yaml-files/)
