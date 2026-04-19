---
title: "Pandas Profiling Report Generator"
description: "The Pandas Profiling Report Generator leverages ydata-profiling to create exhaustive exploratory data analysis reports from CSV, Parquet, and database query results. It computes univariate statistics, bivariate correlation matrices (Pearson, Spearman, Kendall, Cramér&#8217;s V), and identifies high-cardinality categorical columns that may need encoding strategies. Missing value analysis goes beyond simple counts, detecting MCAR/MAR/MNAR patterns using Little&#8217;s test and visualizing missingness correlations as heatmaps. Duplicate row detection with configurable subset columns helps identify data quality issues before they propagate downstream. The skill generates interactive HTML reports with collapsible sections, exportable to static PNG charts for documentation. JSON summary output integrates with CI/CD pipelines for automated data quality gates, failing builds when null percentages exceed thresholds or when new columns appear unexpectedly in source schemas. Supports Spark DataFrames via the pandas API on Spark for large-scale profiling."
source: "https://github.com/pandas-dev/pandas"
verification: "security_reviewed"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "pandas-dev/pandas"
  github_stars: 48498
---

# Pandas Profiling Report Generator

The Pandas Profiling Report Generator leverages ydata-profiling to create exhaustive exploratory data analysis reports from CSV, Parquet, and database query results. It computes univariate statistics, bivariate correlation matrices (Pearson, Spearman, Kendall, Cramér&#8217;s V), and identifies high-cardinality categorical columns that may need encoding strategies. Missing value analysis goes beyond simple counts, detecting MCAR/MAR/MNAR patterns using Little&#8217;s test and visualizing missingness correlations as heatmaps. Duplicate row detection with configurable subset columns helps identify data quality issues before they propagate downstream. The skill generates interactive HTML reports with collapsible sections, exportable to static PNG charts for documentation. JSON summary output integrates with CI/CD pipelines for automated data quality gates, failing builds when null percentages exceed thresholds or when new columns appear unexpectedly in source schemas. Supports Spark DataFrames via the pandas API on Spark for large-scale profiling.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pandas-profiling-report-generator/)
