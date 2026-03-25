---
name: "Parquet to PostgreSQL Loader"
description: "Reads Apache Parquet files using PyArrow and bulk-loads them into PostgreSQL via psycopg2 COPY protocol. Handles schema mapping, partitioned datasets, and incremental upserts with conflict resolution."
category: "Data Extraction & Transformation"
framework: "Claude Agents"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/parquet-to-postgresql-loader/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "parquet"  # from ase_tool_match
  github_stars: 387  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 146943  # from ase_npm_downloads
  github_repo: "ironSource/parquetjs"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: false  # from ase_tool_maintained
---

# Parquet to PostgreSQL Loader

Reads Apache Parquet files using PyArrow and bulk-loads them into PostgreSQL via psycopg2 COPY protocol. Handles schema mapping, partitioned datasets, and incremental upserts with conflict resolution.

## Overview

The Parquet to PostgreSQL Loader skill enables high-performance ingestion of Apache Parquet files into PostgreSQL databases. Built on PyArrow for Parquet reading and psycopg2 for database interaction, it leverages the COPY protocol for maximum throughput rather than row-by-row INSERT statements. The skill automatically maps Parquet schema types to PostgreSQL column types, handling complex conversions like nested structs to JSONB, timestamps with timezone awareness, and decimal precision preservation. For partitioned Parquet datasets (common in data lake architectures), it discovers and processes all partition files while preserving partition column values. Incremental loading is supported through configurable upsert strategies using PostgreSQL ON CONFLICT clauses — choose between UPDATE, IGNORE, or custom merge logic. The loader creates target tables automatically when they do not exist, with proper indexes on partition and primary key columns. Progress reporting, checkpointing for resumable loads, and dry-run mode for schema verification round out the feature set. Compatible with Parquet files from Spark, Athena, BigQuery exports, and DuckDB.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill parquet-to-postgresql-loader
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill parquet-to-postgresql-loader -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill parquet-to-postgresql-loader -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill parquet-to-postgresql-loader -a codex
```

### OpenClaw

```bash
clawhub install parquet-to-postgresql-loader
```

## Source

- Marketplace: https://agentskillexchange.com/skills/parquet-to-postgresql-loader/
