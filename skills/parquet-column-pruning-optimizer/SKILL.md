---
name: "Parquet Column Pruning Optimizer"
description: "Optimizes Apache Parquet file reads using PyArrow column pruning and predicate pushdown. Analyzes query patterns to recommend row group sizing and dictionary encoding strategies."
category: "Data Extraction &amp; Transformation"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/ironsource/parquetjs"
tool_ecosystem:
  tool: parquet
  github_repo: ironsource/parquetjs
  github_stars: 387
  license: MIT
  maintained: false
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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/parquet-column-pruning-optimizer/)
