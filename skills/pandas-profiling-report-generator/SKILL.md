---
title: "Pandas Profiling Report Generator"
description: "The Pandas Profiling Report Generator leverages ydata-profiling to create exhaustive exploratory data analysis reports from CSV, Parquet, and database query results. It computes univariate statistics, bivariate correlation matrices (Pearson, Spearman, Kendall, Cramér’s V), and identifies high-cardinality categorical columns that may need encoding strategies.\nMissing value analysis goes beyond simple counts, detecting MCAR/MAR/MNAR patterns using Little’s test and visualizing missingness correlations as heatmaps. Duplicate row detection with configurable subset columns helps identify data quality issues before they propagate downstream.\nThe skill generates interactive HTML reports with collapsible sections, exportable to static PNG charts for documentation. JSON summary output integrates with CI/CD pipelines for automated data quality gates, failing builds when null percentages exceed thresholds or when new columns appear unexpectedly in source schemas. Supports Spark DataFrames via the pandas API on Spark for large-scale profiling."
verification: security_reviewed
source: "https://github.com/pandas-dev/pandas"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "pandas-dev/pandas"
  github_stars: 48498
---

# Pandas Profiling Report Generator

The Pandas Profiling Report Generator leverages ydata-profiling to create exhaustive exploratory data analysis reports from CSV, Parquet, and database query results. It computes univariate statistics, bivariate correlation matrices (Pearson, Spearman, Kendall, Cramér’s V), and identifies high-cardinality categorical columns that may need encoding strategies.
Missing value analysis goes beyond simple counts, detecting MCAR/MAR/MNAR patterns using Little’s test and visualizing missingness correlations as heatmaps. Duplicate row detection with configurable subset columns helps identify data quality issues before they propagate downstream.
The skill generates interactive HTML reports with collapsible sections, exportable to static PNG charts for documentation. JSON summary output integrates with CI/CD pipelines for automated data quality gates, failing builds when null percentages exceed thresholds or when new columns appear unexpectedly in source schemas. Supports Spark DataFrames via the pandas API on Spark for large-scale profiling.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/pandas-profiling-report-generator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/pandas-profiling-report-generator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pandas-profiling-report-generator/)
