---
title: Pandas Profiling Report Generator
description: The Pandas Profiling Report Generator leverages ydata-profiling to create
  exhaustive exploratory data analysis reports from CSV, Parquet, and database query
  results. It computes univariate statistics, bivariate correlation matrices (Pearson,
  Spearman, Kendall, Cramér’s V), and identifies high-cardinality categorical columns
  that may need encoding strategies. Missing value analysis goes beyond simple counts,
  detecting MCAR/MAR/MNAR patterns using Little’s test and visualizing missingness
  correlations as heatmaps. Duplicate row detection with configurable subset columns
  helps identify data quality issues before they propagate downstream. The skill generates
  interactive HTML reports with collapsible sections, exportable to static PNG charts
  for documentation. JSON summary output integrates with CI/CD pipelines for automated
  data quality gates, failing builds when null percentages exceed thresholds or when
  new columns appear unexpectedly in source schemas. Supports Spark DataFrames via
  the pandas API on Spark for large-scale profiling.
verification: security_reviewed
source: https://agentskillexchange.com/skills/pandas-profiling-report-generator/
category:
- Data Extraction &amp; Transformation
framework:
- Codex
---

# Pandas Profiling Report Generator

The Pandas Profiling Report Generator leverages ydata-profiling to create exhaustive exploratory data analysis reports from CSV, Parquet, and database query results. It computes univariate statistics, bivariate correlation matrices (Pearson, Spearman, Kendall, Cramér’s V), and identifies high-cardinality categorical columns that may need encoding strategies. Missing value analysis goes beyond simple counts, detecting MCAR/MAR/MNAR patterns using Little’s test and visualizing missingness correlations as heatmaps. Duplicate row detection with configurable subset columns helps identify data quality issues before they propagate downstream. The skill generates interactive HTML reports with collapsible sections, exportable to static PNG charts for documentation. JSON summary output integrates with CI/CD pipelines for automated data quality gates, failing builds when null percentages exceed thresholds or when new columns appear unexpectedly in source schemas. Supports Spark DataFrames via the pandas API on Spark for large-scale profiling.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pandas-profiling-report-generator/)
