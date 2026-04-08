---
title: Parquet Column Mapper
description: The Parquet Column Mapper skill uses the PyArrow library to read Apache
  Parquet file footers, row group metadata, and column chunk statistics without loading
  full datasets into memory. It extracts min/max values, null counts, distinct counts,
  and encoding information for each column chunk across row groups. The skill maps
  Parquet logical and physical types to equivalent types in Delta Lake, Apache Iceberg,
  and Apache Hudi table formats, identifying type compatibility issues during format
  migration. Features include partition statistics aggregation from directory-structured
  datasets, predicate pushdown simulation for query planning analysis, and bloom filter
  metadata extraction for point lookup optimization. Supports bulk schema comparison
  across Parquet files in S3, GCS, and ADLS using fsspec-compatible file systems.
verification: listed
source: https://agentskillexchange.com/skills/parquet-column-mapper/
category:
- Data Extraction &amp; Transformation
framework:
- MCP
---

# Parquet Column Mapper

The Parquet Column Mapper skill uses the PyArrow library to read Apache Parquet file footers, row group metadata, and column chunk statistics without loading full datasets into memory. It extracts min/max values, null counts, distinct counts, and encoding information for each column chunk across row groups. The skill maps Parquet logical and physical types to equivalent types in Delta Lake, Apache Iceberg, and Apache Hudi table formats, identifying type compatibility issues during format migration. Features include partition statistics aggregation from directory-structured datasets, predicate pushdown simulation for query planning analysis, and bloom filter metadata extraction for point lookup optimization. Supports bulk schema comparison across Parquet files in S3, GCS, and ADLS using fsspec-compatible file systems.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/parquet-column-mapper/)
