---
name: "Parquet Column Mapper"
description: "Reads and transforms Apache Parquet file metadata and column statistics using PyArrow and the Parquet Thrift specification. Maps column types across Delta Lake, Iceberg, and Hudi table formats."
category: "Data Extraction & Transformation"
framework: "MCP"
verification: listed
source: "https://github.com/ironSource/parquetjs"
tool_ecosystem:
  tool: parquet
  github_stars: 387
  npm_weekly_downloads: 146943
  github_repo: ironSource/parquetjs
  license: MIT
  maintained: false
---
# Parquet Column Mapper

Reads and transforms Apache Parquet file metadata and column statistics using PyArrow and the Parquet Thrift specification. Maps column types across Delta Lake, Iceberg, and Hudi table formats.

## Overview

The Parquet Column Mapper skill uses the PyArrow library to read Apache Parquet file footers, row group metadata, and column chunk statistics without loading full datasets into memory. It extracts min/max values, null counts, distinct counts, and encoding information for each column chunk across row groups. The skill maps Parquet logical and physical types to equivalent types in Delta Lake, Apache Iceberg, and Apache Hudi table formats, identifying type compatibility issues during format migration. Features include partition statistics aggregation from directory-structured datasets, predicate pushdown simulation for query planning analysis, and bloom filter metadata extraction for point lookup optimization. Supports bulk schema comparison across Parquet files in S3, GCS, and ADLS using fsspec-compatible file systems.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill parquet-column-mapper
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill parquet-column-mapper -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill parquet-column-mapper -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill parquet-column-mapper -a codex
```

### OpenClaw

```bash
clawhub install parquet-column-mapper
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/parquet-column-mapper/)
