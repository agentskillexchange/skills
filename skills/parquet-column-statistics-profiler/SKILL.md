---
title: "Parquet Column Statistics Profiler"
description: "Profiles Apache Parquet files using pyarrow metadata APIs to extract column statistics, row group distributions, and encoding efficiency metrics without reading full datasets."
slug: "parquet-column-statistics-profiler"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/parquet-column-statistics-profiler/"
---

# Parquet Column Statistics Profiler

Profiles Apache Parquet files using pyarrow metadata APIs to extract column statistics, row group distributions, and encoding efficiency metrics without reading full datasets.

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
clawhub install parquet-column-statistics-profiler
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Parquet Column Statistics Profiler skill performs lightweight metadata-only analysis of Apache Parquet files to extract comprehensive column statistics and storage efficiency metrics. Using pyarrow’s ParquetFile metadata API, it reads file footers and row group statistics without loading actual data into memory.
For each column, the skill extracts min/max values, null counts, distinct value estimates from Bloom filters, and compression ratios across encodings (PLAIN, DICTIONARY, RLE, DELTA_BINARY_PACKED). It identifies columns with poor dictionary encoding efficiency (high cardinality vs. dictionary page size) and recommends encoding strategy changes.
Row group analysis reveals data distribution skew, optimal row group sizing for your query patterns, and predicate pushdown effectiveness estimates. The skill can compare statistics across partitioned datasets to identify data quality issues like NULL spikes, value range drift, or partition skew that impacts query performance.
Output includes formatted profiling reports with histograms, a storage efficiency scorecard, and actionable recommendations for Spark/Trino query optimization. Supports Parquet files on local filesystem, S3 (via fsspec), GCS, and ADLS.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/parquet-column-statistics-profiler/)
