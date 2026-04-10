---
title: "Parquet to PostgreSQL Loader"
description: "Reads Apache Parquet files using PyArrow and bulk-loads them into PostgreSQL via psycopg2 COPY protocol. Handles schema mapping, partitioned datasets, and incremental upserts with conflict resolution."
slug: "parquet-to-postgresql-loader"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Claude Agents"
verification: "listed"
source: "https://agentskillexchange.com/skills/parquet-to-postgresql-loader/"
---

# Parquet to PostgreSQL Loader

Reads Apache Parquet files using PyArrow and bulk-loads them into PostgreSQL via psycopg2 COPY protocol. Handles schema mapping, partitioned datasets, and incremental upserts with conflict resolution.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install parquet-to-postgresql-loader
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Parquet to PostgreSQL Loader skill enables high-performance ingestion of Apache Parquet files into PostgreSQL databases. Built on PyArrow for Parquet reading and psycopg2 for database interaction, it leverages the COPY protocol for maximum throughput rather than row-by-row INSERT statements. The skill automatically maps Parquet schema types to PostgreSQL column types, handling complex conversions like nested structs to JSONB, timestamps with timezone awareness, and decimal precision preservation. For partitioned Parquet datasets (common in data lake architectures), it discovers and processes all partition files while preserving partition column values. Incremental loading is supported through configurable upsert strategies using PostgreSQL ON CONFLICT clauses — choose between UPDATE, IGNORE, or custom merge logic. The loader creates target tables automatically when they do not exist, with proper indexes on partition and primary key columns. Progress reporting, checkpointing for resumable loads, and dry-run mode for schema verification round out the feature set. Compatible with Parquet files from Spark, Athena, BigQuery exports, and DuckDB.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/parquet-to-postgresql-loader/)
