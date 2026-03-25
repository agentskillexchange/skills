---
name: "DuckDB SQL Analytics Agent"
description: "Run analytical SQL queries on local files (CSV, Parquet, JSON) using the DuckDB in-process database engine. Enables fast OLAP-style analysis without a server, directly from flat files on disk."
category: "Data Extraction & Transformation"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/duckdb-sql-analytics-agent/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "parquet"  # from ase_tool_match
  github_stars: 387  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 146943  # from ase_npm_downloads
  github_repo: "ironSource/parquetjs"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: false  # from ase_tool_maintained
---

# DuckDB SQL Analytics Agent

Run analytical SQL queries on local files (CSV, Parquet, JSON) using the DuckDB in-process database engine. Enables fast OLAP-style analysis without a server, directly from flat files on disk.

## Overview

The DuckDB SQL Analytics Agent leverages [DuckDB](https://github.com/duckdb/duckdb), the high-performance in-process analytical database system with over 36,000 GitHub stars. DuckDB is designed to execute complex analytical SQL queries extremely fast, operating entirely within the host process without requiring a separate database server.

This skill enables AI agents to perform sophisticated data analysis on local file formats including CSV, Parquet, JSON, and Excel files. DuckDB reads these files directly — no ETL pipeline or data import step is needed. Agents can write standard SQL with DuckDB extensions like window functions, CTEs, lateral joins, and aggregate operations to answer complex data questions.

The skill works by having the agent invoke DuckDB CLI commands or use the Python/Node.js API bindings. The agent can inspect schemas, run exploratory queries, compute aggregations, join datasets across file formats, and export results to new files. DuckDB’s columnar execution engine means even billion-row Parquet datasets process in seconds on a single machine.

Output formats include query results as tables, CSV exports, Parquet outputs, or JSON payloads. Integration points include dbt for transformation workflows, Jupyter notebooks for interactive analysis, and any Python or Node.js environment that supports DuckDB bindings. The MIT-licensed engine supports PostgreSQL wire protocol compatibility, making it a drop-in analytical backend for many existing tools.

Key capabilities: in-process OLAP execution, zero-copy Parquet scanning, cross-format joins (CSV + Parquet + JSON), window functions and advanced aggregations, export to multiple formats, and PostgreSQL compatibility mode.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill duckdb-sql-analytics-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill duckdb-sql-analytics-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill duckdb-sql-analytics-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill duckdb-sql-analytics-agent -a codex
```

### OpenClaw

```bash
clawhub install duckdb-sql-analytics-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/duckdb-sql-analytics-agent/
