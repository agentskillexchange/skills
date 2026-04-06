---
name: DuckDB SQL Analytics Agent
description: Run analytical SQL queries on local files (CSV, Parquet, JSON) using
  the DuckDB in-process database engine. Enables fast OLAP-style analysis without
  a server, directly from flat files on disk.
category: "Data Extraction &amp; Transformation"
framework: Claude Code, OpenClaw
verification: security_reviewed
source: "https://github.com/duckdb/duckdb"
tool_ecosystem:
  github_repo: "https://github.com/duckdb/duckdb"
  github_stars: 37119
---
# DuckDB SQL Analytics Agent

Run analytical SQL queries on local files (CSV, Parquet, JSON) using the DuckDB in-process database engine. Enables fast OLAP-style analysis without a server, directly from flat files on disk.

The DuckDB SQL Analytics Agent leverages DuckDB, the high-performance in-process analytical database system with over 36,000 GitHub stars. DuckDB is designed to execute complex analytical SQL queries extremely fast, operating entirely within the host process without requiring a separate database server.

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

- [GitHub](https://github.com/duckdb/duckdb)
