---
name: Ingestr Cross-Database Data Copier
description: Copy data between any databases with a single CLI command using Ingestr.
  Supports 50+ sources and destinations including PostgreSQL, MySQL, BigQuery, Snowflake,
  DuckDB, MongoDB, and S3.
verification: security_reviewed
source: https://github.com/bruin-data/ingestr
category:
- Data Extraction &amp; Transformation
- Integrations &amp; Connectors
framework:
- Claude Code
- OpenClaw
tool_ecosystem:
  github_repo: bruin-data/ingestr
  github_stars: 3442
---
# Ingestr Cross-Database Data Copier

The Ingestr Cross-Database Data Copier skill uses Ingestr, the open-source CLI tool with over 3,400 GitHub stars from Bruin Data, to copy data between databases and data stores with a single command. Ingestr eliminates the need to write custom ETL scripts or configure complex pipeline tools for straightforward data movement tasks.
This skill enables AI agents to move data between 50+ supported sources and destinations. Sources include PostgreSQL, MySQL, SQLite, SQL Server, Oracle, MongoDB, DuckDB, BigQuery, Snowflake, Redshift, Databricks, ClickHouse, Google Sheets, Notion, Shopify, Stripe, GitHub, HubSpot, Slack, and many more. Destinations include all major databases and data warehouses plus local file formats.
The agent invokes Ingestr with a simple command pattern: ingestr ingest --source-uri 'SOURCE_URI' --source-table 'table_name' --dest-uri 'DEST_URI' --dest-table 'target_table'. Ingestr handles schema detection, type mapping between different database systems, and incremental loading strategies. It supports full-refresh, append, merge, and delete+insert loading modes.
For incremental ingestion, Ingestr can track state using a cursor column (like an updated_at timestamp or auto-incrementing ID), only fetching rows that have changed since the last run. This makes it practical for ongoing sync jobs, not just one-off copies. The tool also supports SQL-based source queries for extracting specific subsets of data.
Key technical features include automatic type mapping across database systems, connection string-based configuration (no config files needed), progress reporting during transfers, and support for both full and incremental sync strategies. Available on PyPI as ingestr, licensed under MIT, and installable via pip install ingestr or brew install ingestr on macOS.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ingestr-cross-database-data-copier/)
