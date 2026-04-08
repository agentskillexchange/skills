---
title: Parquet to PostgreSQL Loader
description: The Parquet to PostgreSQL Loader skill enables high-performance ingestion
  of Apache Parquet files into PostgreSQL databases. Built on PyArrow for Parquet
  reading and psycopg2 for database interaction, it leverages the COPY protocol for
  maximum throughput rather than row-by-row INSERT statements. The skill automatically
  maps Parquet schema types to PostgreSQL column types, handling complex conversions
  like nested structs to JSONB, timestamps with timezone awareness, and decimal precision
  preservation. For partitioned Parquet datasets (common in data lake architectures),
  it discovers and processes all partition files while preserving partition column
  values. Incremental loading is supported through configurable upsert strategies
  using PostgreSQL ON CONFLICT clauses — choose between UPDATE, IGNORE, or custom
  merge logic. The loader creates target tables automatically when they do not exist,
  with proper indexes on partition and primary key columns. Progress reporting, checkpointing
  for resumable loads, and dry-run mode for schema verification round out the feature
  set. Compatible with Parquet files from Spark, Athena, BigQuery exports, and DuckDB.
verification: listed
source: https://agentskillexchange.com/skills/parquet-to-postgresql-loader/
category:
- Data Extraction &amp; Transformation
framework:
- Claude Agents
---

# Parquet to PostgreSQL Loader

The Parquet to PostgreSQL Loader skill enables high-performance ingestion of Apache Parquet files into PostgreSQL databases. Built on PyArrow for Parquet reading and psycopg2 for database interaction, it leverages the COPY protocol for maximum throughput rather than row-by-row INSERT statements. The skill automatically maps Parquet schema types to PostgreSQL column types, handling complex conversions like nested structs to JSONB, timestamps with timezone awareness, and decimal precision preservation. For partitioned Parquet datasets (common in data lake architectures), it discovers and processes all partition files while preserving partition column values. Incremental loading is supported through configurable upsert strategies using PostgreSQL ON CONFLICT clauses — choose between UPDATE, IGNORE, or custom merge logic. The loader creates target tables automatically when they do not exist, with proper indexes on partition and primary key columns. Progress reporting, checkpointing for resumable loads, and dry-run mode for schema verification round out the feature set. Compatible with Parquet files from Spark, Athena, BigQuery exports, and DuckDB.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/parquet-to-postgresql-loader/)
