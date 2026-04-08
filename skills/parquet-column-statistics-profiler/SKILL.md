---
title: Parquet Column Statistics Profiler
description: The Parquet Column Statistics Profiler skill performs lightweight metadata-only
  analysis of Apache Parquet files to extract comprehensive column statistics and
  storage efficiency metrics. Using pyarrow’s ParquetFile metadata API, it reads file
  footers and row group statistics without loading actual data into memory. For each
  column, the skill extracts min/max values, null counts, distinct value estimates
  from Bloom filters, and compression ratios across encodings (PLAIN, DICTIONARY,
  RLE, DELTA_BINARY_PACKED). It identifies columns with poor dictionary encoding efficiency
  (high cardinality vs. dictionary page size) and recommends encoding strategy changes.
  Row group analysis reveals data distribution skew, optimal row group sizing for
  your query patterns, and predicate pushdown effectiveness estimates. The skill can
  compare statistics across partitioned datasets to identify data quality issues like
  NULL spikes, value range drift, or partition skew that impacts query performance.
  Output includes formatted profiling reports with histograms, a storage efficiency
  scorecard, and actionable recommendations for Spark/Trino query optimization. Supports
  Parquet files on local filesystem, S3 (via fsspec), GCS, and ADLS.
verification: security_reviewed
source: https://agentskillexchange.com/skills/parquet-column-statistics-profiler/
category:
- Data Extraction &amp; Transformation
framework:
- ChatGPT Agents
---

# Parquet Column Statistics Profiler

The Parquet Column Statistics Profiler skill performs lightweight metadata-only analysis of Apache Parquet files to extract comprehensive column statistics and storage efficiency metrics. Using pyarrow’s ParquetFile metadata API, it reads file footers and row group statistics without loading actual data into memory. For each column, the skill extracts min/max values, null counts, distinct value estimates from Bloom filters, and compression ratios across encodings (PLAIN, DICTIONARY, RLE, DELTA_BINARY_PACKED). It identifies columns with poor dictionary encoding efficiency (high cardinality vs. dictionary page size) and recommends encoding strategy changes. Row group analysis reveals data distribution skew, optimal row group sizing for your query patterns, and predicate pushdown effectiveness estimates. The skill can compare statistics across partitioned datasets to identify data quality issues like NULL spikes, value range drift, or partition skew that impacts query performance. Output includes formatted profiling reports with histograms, a storage efficiency scorecard, and actionable recommendations for Spark/Trino query optimization. Supports Parquet files on local filesystem, S3 (via fsspec), GCS, and ADLS.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/parquet-column-statistics-profiler/)
