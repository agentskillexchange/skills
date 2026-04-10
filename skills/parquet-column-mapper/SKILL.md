---
title: "Parquet Column Mapper"
description: "Reads and transforms Apache Parquet file metadata and column statistics using PyArrow and the Parquet Thrift specification. Maps column types across Delta Lake, Iceberg, and Hudi table formats."
slug: "parquet-column-mapper"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "MCP"
verification: "listed"
source: "https://agentskillexchange.com/skills/parquet-column-mapper/"
---

# Parquet Column Mapper

Reads and transforms Apache Parquet file metadata and column statistics using PyArrow and the Parquet Thrift specification. Maps column types across Delta Lake, Iceberg, and Hudi table formats.

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
clawhub install parquet-column-mapper
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Parquet Column Mapper skill uses the PyArrow library to read Apache Parquet file footers, row group metadata, and column chunk statistics without loading full datasets into memory. It extracts min/max values, null counts, distinct counts, and encoding information for each column chunk across row groups. The skill maps Parquet logical and physical types to equivalent types in Delta Lake, Apache Iceberg, and Apache Hudi table formats, identifying type compatibility issues during format migration. Features include partition statistics aggregation from directory-structured datasets, predicate pushdown simulation for query planning analysis, and bloom filter metadata extraction for point lookup optimization. Supports bulk schema comparison across Parquet files in S3, GCS, and ADLS using fsspec-compatible file systems.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/parquet-column-mapper/)
