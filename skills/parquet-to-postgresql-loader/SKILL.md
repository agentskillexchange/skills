---
title: "Parquet to PostgreSQL Loader"
description: "Reads Apache Parquet files using PyArrow and bulk-loads them into PostgreSQL via psycopg2 COPY protocol. Handles schema mapping, partitioned datasets, and incremental upserts with conflict resolution."
verification: listed
source: "https://agentskillexchange.com/skills/parquet-to-postgresql-loader/"
category:
  - "Data Extraction & Transformation"
framework:
  - "Claude Agents"
---

# Parquet to PostgreSQL Loader

The Parquet to PostgreSQL Loader skill enables high-performance ingestion of Apache Parquet files into PostgreSQL databases. Built on PyArrow for Parquet reading and psycopg2 for database interaction, it leverages the COPY protocol for maximum throughput rather than row-by-row INSERT statements. The skill automatically maps Parquet schema types to PostgreSQL column types, handling complex conversions like nested structs to JSONB, timestamps with timezone awareness, and decimal precision preservation. For partitioned Parquet datasets (common in data lake architectures), it discovers and processes all partition files while preserving partition column values. Incremental loading is supported through configurable upsert strategies using PostgreSQL ON CONFLICT clauses — choose between UPDATE, IGNORE, or custom merge logic. The loader creates target tables automatically when they do not exist, with proper indexes on partition and primary key columns. Progress reporting, checkpointing for resumable loads, and dry-run mode for schema verification round out the feature set. Compatible with Parquet files from Spark, Athena, BigQuery exports, and DuckDB.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/parquet-to-postgresql-loader
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/parquet-to-postgresql-loader` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/parquet-to-postgresql-loader/)
