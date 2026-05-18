---
name: "DuckDB SQL Analytics Agent"
slug: "duckdb-sql-analytics-agent"
description: "Run analytical SQL queries on local files (CSV, Parquet, JSON) using the DuckDB in-process database engine. Enables fast OLAP-style analysis without a server, directly from flat files on disk."
github_stars: 37119
verification: "security_reviewed"
source: "https://github.com/duckdb/duckdb"
category: "Data Extraction & Transformation"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "duckdb/duckdb"
  github_stars: 37119
---

# DuckDB SQL Analytics Agent

Run analytical SQL queries on local files (CSV, Parquet, JSON) using the DuckDB in-process database engine. Enables fast OLAP-style analysis without a server, directly from flat files on disk.

## Installation

Use the upstream install or setup path that matches your environment:
- For development, DuckDB requires [CMake](https://cmake.org), Python 3 and a C++17 compliant compiler. In the root directory, run make to compile the sources. For development, use make debug to build a non-optimized de...

Requirements and caveats from upstream:
- DuckDB is available as a [standalone CLI application](https://duckdb.org/docs/current/clients/cli/overview) and has clients for [Python](https://duckdb.org/docs/current/clients/python/overview), [R](https://duckdb.org...

Basic usage or getting-started notes:
- If you want to install DuckDB, please see [our installation page](https://duckdb.org/docs/installation/) for instructions.
- ## Data Import
- For CSV files and Parquet files, data import is as simple as referencing the file in the FROM clause:

- Source: https://github.com/duckdb/duckdb
- Extracted from upstream docs: https://raw.githubusercontent.com/duckdb/duckdb/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/duckdb-sql-analytics-agent/)
