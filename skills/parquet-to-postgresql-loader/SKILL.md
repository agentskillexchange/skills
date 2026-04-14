---
title: "Parquet to PostgreSQL Loader"
description: "Reads Apache Parquet files using PyArrow and bulk-loads them into PostgreSQL via psycopg2 COPY protocol. Handles schema mapping, partitioned datasets, and incremental upserts with conflict resolution."
verification: listed
source: "https://agentskillexchange.com/skills/parquet-to-postgresql-loader/"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Claude Agents"
---

# Parquet to PostgreSQL Loader

The Parquet to PostgreSQL Loader skill enables high-performance ingestion of Apache Parquet files into PostgreSQL databases. Built on PyArrow for Parquet reading and psycopg2 for database interaction, it leverages the COPY protocol for maximum throughput rather than row-by-row INSERT statements. The skill automatically maps Parquet schema types to PostgreSQL column types, handling complex conversions like nested structs to JSONB, timestamps with timezone awareness, and decimal precision preservation. For partitioned Parquet datasets (common in data lake architectures), it discovers and processes all partition files while preserving partition column values. Incremental loading is supported through configurable upsert strategies using PostgreSQL ON CONFLICT clauses — choose between UPDATE, IGNORE, or custom merge logic. The loader creates target tables automatically when they do not exist, with proper indexes on partition and primary key columns. Progress reporting, checkpointing for resumable loads, and dry-run mode for schema verification round out the feature set. Compatible with Parquet files from Spark, Athena, BigQuery exports, and DuckDB.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/parquet-to-postgresql-loader/)
