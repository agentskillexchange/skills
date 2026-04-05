---
name: "Parquet Column Statistics Profiler"
description: "Profiles Apache Parquet files using pyarrow metadata APIs to extract column statistics, row group distributions, and encoding efficiency metrics without reading full datasets."
category: "Data Extraction &amp; Transformation"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/parquet-column-statistics-profiler/"
---
# Parquet Column Statistics Profiler

Profiles Apache Parquet files using pyarrow metadata APIs to extract column statistics, row group distributions, and encoding efficiency metrics without reading full datasets.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill parquet-column-statistics-profiler
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill parquet-column-statistics-profiler -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill parquet-column-statistics-profiler -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill parquet-column-statistics-profiler -a codex
```

### OpenClaw

```bash
clawhub install parquet-column-statistics-profiler
```

## Details

The Parquet Column Statistics Profiler skill performs lightweight metadata-only analysis of Apache Parquet files to extract comprehensive column statistics and storage efficiency metrics. Using pyarrow’s ParquetFile metadata API, it reads file footers and row group statistics without loading actual data into memory.

For each column, the skill extracts min/max values, null counts, distinct value estimates from Bloom filters, and compression ratios across encodings (PLAIN, DICTIONARY, RLE, DELTA_BINARY_PACKED). It identifies columns with poor dictionary encoding efficiency (high cardinality vs. dictionary page size) and recommends encoding strategy changes.

Row group analysis reveals data distribution skew, optimal row group sizing for your query patterns, and predicate pushdown effectiveness estimates. The skill can compare statistics across partitioned datasets to identify data quality issues like NULL spikes, value range drift, or partition skew that impacts query performance.

Output includes formatted profiling reports with histograms, a storage efficiency scorecard, and actionable recommendations for Spark/Trino query optimization. Supports Parquet files on local filesystem, S3 (via fsspec), GCS, and ADLS.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/parquet-column-statistics-profiler/)
