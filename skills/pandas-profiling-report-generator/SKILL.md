---
title: "Pandas Profiling Report Generator"
description: "Generates comprehensive data quality reports using ydata-profiling (formerly pandas-profiling) with correlation analysis, missing value patterns, and cardinality detection. Exports interactive HTML dashboards and JSON summaries."
slug: "pandas-profiling-report-generator"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/pandas-profiling-report-generator/"
---

# Pandas Profiling Report Generator

Generates comprehensive data quality reports using ydata-profiling (formerly pandas-profiling) with correlation analysis, missing value patterns, and cardinality detection. Exports interactive HTML dashboards and JSON summaries.

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
clawhub install pandas-profiling-report-generator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Pandas Profiling Report Generator leverages ydata-profiling to create exhaustive exploratory data analysis reports from CSV, Parquet, and database query results. It computes univariate statistics, bivariate correlation matrices (Pearson, Spearman, Kendall, Cramér’s V), and identifies high-cardinality categorical columns that may need encoding strategies.
Missing value analysis goes beyond simple counts, detecting MCAR/MAR/MNAR patterns using Little’s test and visualizing missingness correlations as heatmaps. Duplicate row detection with configurable subset columns helps identify data quality issues before they propagate downstream.
The skill generates interactive HTML reports with collapsible sections, exportable to static PNG charts for documentation. JSON summary output integrates with CI/CD pipelines for automated data quality gates, failing builds when null percentages exceed thresholds or when new columns appear unexpectedly in source schemas. Supports Spark DataFrames via the pandas API on Spark for large-scale profiling.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pandas-profiling-report-generator/)
