---
name: "Ingestr Cross-Database Data Copier"
description: "Copy data between any databases with a single CLI command using Ingestr. Supports 50+ sources and destinations including PostgreSQL, MySQL, BigQuery, Snowflake, DuckDB, MongoDB, and S3."
category: "Data Extraction & Transformation"
framework: "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/ingestr-cross-database-data-copier/"
tool_ecosystem:
  tool: notion
  github_stars: 5562
  npm_weekly_downloads: 1084242
  github_repo: makenotion/notion-sdk-js
  license: MIT
  maintained: true
---

# Ingestr Cross-Database Data Copier

Copy data between any databases with a single CLI command using Ingestr. Supports 50+ sources and destinations including PostgreSQL, MySQL, BigQuery, Snowflake, DuckDB, MongoDB, and S3.

## Overview

The Ingestr Cross-Database Data Copier skill uses [Ingestr](https://github.com/bruin-data/ingestr), the open-source CLI tool with over 3,400 GitHub stars from Bruin Data, to copy data between databases and data stores with a single command. Ingestr eliminates the need to write custom ETL scripts or configure complex pipeline tools for straightforward data movement tasks.

This skill enables AI agents to move data between 50+ supported sources and destinations. Sources include PostgreSQL, MySQL, SQLite, SQL Server, Oracle, MongoDB, DuckDB, BigQuery, Snowflake, Redshift, Databricks, ClickHouse, Google Sheets, Notion, Shopify, Stripe, GitHub, HubSpot, Slack, and many more. Destinations include all major databases and data warehouses plus local file formats.

The agent invokes Ingestr with a simple command pattern: `ingestr ingest --source-uri 'SOURCE_URI' --source-table 'table_name' --dest-uri 'DEST_URI' --dest-table 'target_table'`. Ingestr handles schema detection, type mapping between different database systems, and incremental loading strategies. It supports full-refresh, append, merge, and delete+insert loading modes.

For incremental ingestion, Ingestr can track state using a cursor column (like an updated_at timestamp or auto-incrementing ID), only fetching rows that have changed since the last run. This makes it practical for ongoing sync jobs, not just one-off copies. The tool also supports SQL-based source queries for extracting specific subsets of data.

Key technical features include automatic type mapping across database systems, connection string-based configuration (no config files needed), progress reporting during transfers, and support for both full and incremental sync strategies. Available on PyPI as `ingestr`, licensed under MIT, and installable via `pip install ingestr` or `brew install ingestr` on macOS.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill ingestr-cross-database-data-copier
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill ingestr-cross-database-data-copier -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill ingestr-cross-database-data-copier -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill ingestr-cross-database-data-copier -a codex
```

### OpenClaw

```bash
clawhub install ingestr-cross-database-data-copier
```

## Source

- Marketplace: https://agentskillexchange.com/skills/ingestr-cross-database-data-copier/
