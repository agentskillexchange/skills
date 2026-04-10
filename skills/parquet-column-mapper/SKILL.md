---
name: Parquet Column Mapper
description: Reads and transforms Apache Parquet file metadata and column statistics
  using PyArrow and the Parquet Thrift specification. Maps column types across Delta
  Lake, Iceberg, and Hudi table formats.
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

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/parquet-column-mapper/)
