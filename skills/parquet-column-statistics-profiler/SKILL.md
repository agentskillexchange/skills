---
title: "Parquet Column Statistics Profiler"
description: "Profiles Apache Parquet files using pyarrow metadata APIs to extract column statistics, row group distributions, and encoding efficiency metrics without reading full datasets."
verification: "security_reviewed"
source: "https://github.com/ironSource/parquetjs"
category:
  - "Data Extraction & Transformation"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "ironsource/parquetjs"
  github_stars: 387
  npm_package: "parquetjs"
  npm_weekly_downloads: 170660
---

# Parquet Column Statistics Profiler

The Parquet Column Statistics Profiler skill performs lightweight metadata-only analysis of Apache Parquet files to extract comprehensive column statistics and storage efficiency metrics. Using pyarrow’s ParquetFile metadata API, it reads file footers and row group statistics without loading actual data into memory. For each column, the skill extracts min/max values, null counts, distinct value estimates from Bloom filters, and compression ratios across encodings (PLAIN, DICTIONARY, RLE, DELTA_BINARY_PACKED). It identifies columns with poor dictionary encoding efficiency (high cardinality vs. dictionary page size) and recommends encoding strategy changes. Row group analysis reveals data distribution skew, optimal row group sizing for your query patterns, and predicate pushdown effectiveness estimates. The skill can compare statistics across partitioned datasets to identify data quality issues like NULL spikes, value range drift, or partition skew that impacts query performance. Output includes formatted profiling reports with histograms, a storage efficiency scorecard, and actionable recommendations for Spark/Trino query optimization. Supports Parquet files on local filesystem, S3 (via fsspec), GCS, and ADLS.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/parquet-column-statistics-profiler/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/parquet-column-statistics-profiler
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/parquet-column-statistics-profiler`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/parquet-column-statistics-profiler/)
