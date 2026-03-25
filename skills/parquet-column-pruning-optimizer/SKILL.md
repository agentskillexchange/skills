---
name: "Parquet Column Pruning Optimizer"
description: "Optimizes Apache Parquet file reads using PyArrow column pruning and predicate pushdown. Analyzes query patterns to recommend row group sizing and dictionary encoding strategies."
category: "Data Extraction & Transformation"
framework: "Custom Agents"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/parquet-column-pruning-optimizer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "parquet"  # from ase_tool_match
  github_stars: 387  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 146943  # from ase_npm_downloads
  github_repo: "ironSource/parquetjs"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: false  # from ase_tool_maintained
---

# Parquet Column Pruning Optimizer

Optimizes Apache Parquet file reads using PyArrow column pruning and predicate pushdown. Analyzes query patterns to recommend row group sizing and dictionary encoding strategies.

## Overview

The Parquet Column Pruning Optimizer reduces data lake query costs by analyzing SQL query patterns against Parquet file metadata to recommend optimal column projection and predicate pushdown strategies. Using PyArrow and the Parquet file footer metadata reader, it maps query column references to Parquet column indices, calculates potential I/O savings from column pruning, and identifies row groups that can be skipped via min/max statistics pushdown. The agent analyzes column cardinality and value distributions to recommend dictionary encoding vs plain encoding per column, optimal row group sizes based on query selectivity patterns, and page-level bloom filter configuration for high-cardinality columns. It supports Parquet files on local disk, S3, GCS, and HDFS via fsspec filesystem abstraction, handles nested schema types (structs, lists, maps), and generates optimized PyArrow read configurations with filters and columns parameters. Includes benchmark reporting comparing optimized vs naive read performance.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill parquet-column-pruning-optimizer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill parquet-column-pruning-optimizer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill parquet-column-pruning-optimizer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill parquet-column-pruning-optimizer -a codex
```

### OpenClaw

```bash
clawhub install parquet-column-pruning-optimizer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/parquet-column-pruning-optimizer/
