---
title: "Parquet Column Pruning Optimizer"
description: "Optimizes Apache Parquet file reads using PyArrow column pruning and predicate pushdown. Analyzes query patterns to recommend row group sizing and dictionary encoding strategies."
slug: "parquet-column-pruning-optimizer"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/parquet-column-pruning-optimizer/"
---

# Parquet Column Pruning Optimizer

Optimizes Apache Parquet file reads using PyArrow column pruning and predicate pushdown. Analyzes query patterns to recommend row group sizing and dictionary encoding strategies.

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
clawhub install parquet-column-pruning-optimizer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Parquet Column Pruning Optimizer reduces data lake query costs by analyzing SQL query patterns against Parquet file metadata to recommend optimal column projection and predicate pushdown strategies. Using PyArrow and the Parquet file footer metadata reader, it maps query column references to Parquet column indices, calculates potential I/O savings from column pruning, and identifies row groups that can be skipped via min/max statistics pushdown. The agent analyzes column cardinality and value distributions to recommend dictionary encoding vs plain encoding per column, optimal row group sizes based on query selectivity patterns, and page-level bloom filter configuration for high-cardinality columns. It supports Parquet files on local disk, S3, GCS, and HDFS via fsspec filesystem abstraction, handles nested schema types (structs, lists, maps), and generates optimized PyArrow read configurations with filters and columns parameters. Includes benchmark reporting comparing optimized vs naive read performance.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/parquet-column-pruning-optimizer/)
