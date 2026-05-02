---
title: "Parquet Column Mapper"
description: "Reads and transforms Apache Parquet file metadata and column statistics using PyArrow and the Parquet Thrift specification. Maps column types across Delta Lake, Iceberg, and Hudi table formats."
verification: "listed"
source: "https://github.com/ironSource/parquetjs"
category:
  - "Data Extraction & Transformation"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "ironsource/parquetjs"
  github_stars: 387
  npm_package: "parquetjs"
  npm_weekly_downloads: 170660
---

# Parquet Column Mapper

The Parquet Column Mapper skill uses the PyArrow library to read Apache Parquet file footers, row group metadata, and column chunk statistics without loading full datasets into memory. It extracts min/max values, null counts, distinct counts, and encoding information for each column chunk across row groups. The skill maps Parquet logical and physical types to equivalent types in Delta Lake, Apache Iceberg, and Apache Hudi table formats, identifying type compatibility issues during format migration. Features include partition statistics aggregation from directory-structured datasets, predicate pushdown simulation for query planning analysis, and bloom filter metadata extraction for point lookup optimization. Supports bulk schema comparison across Parquet files in S3, GCS, and ADLS using fsspec-compatible file systems.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/parquet-column-mapper/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/parquet-column-mapper
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/parquet-column-mapper`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/parquet-column-mapper/)
