---
title: "Parquet Column Pruning Optimizer"
description: "Optimizes Apache Parquet file reads using PyArrow column pruning and predicate pushdown. Analyzes query patterns to recommend row group sizing and dictionary encoding strategies."
verification: "security_reviewed"
source: "https://github.com/ironSource/parquetjs"
category:
  - "Data Extraction & Transformation"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "ironsource/parquetjs"
  github_stars: 387
  npm_package: "parquetjs"
  npm_weekly_downloads: 170660
---

# Parquet Column Pruning Optimizer

The Parquet Column Pruning Optimizer reduces data lake query costs by analyzing SQL query patterns against Parquet file metadata to recommend optimal column projection and predicate pushdown strategies. Using PyArrow and the Parquet file footer metadata reader, it maps query column references to Parquet column indices, calculates potential I/O savings from column pruning, and identifies row groups that can be skipped via min/max statistics pushdown. The agent analyzes column cardinality and value distributions to recommend dictionary encoding vs plain encoding per column, optimal row group sizes based on query selectivity patterns, and page-level bloom filter configuration for high-cardinality columns. It supports Parquet files on local disk, S3, GCS, and HDFS via fsspec filesystem abstraction, handles nested schema types (structs, lists, maps), and generates optimized PyArrow read configurations with filters and columns parameters. Includes benchmark reporting comparing optimized vs naive read performance.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/parquet-column-pruning-optimizer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/parquet-column-pruning-optimizer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/parquet-column-pruning-optimizer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/parquet-column-pruning-optimizer/)
