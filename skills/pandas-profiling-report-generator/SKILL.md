---
title: "Pandas Profiling Report Generator"
description: "Generates comprehensive data quality reports using ydata-profiling (formerly pandas-profiling) with correlation analysis, missing value patterns, and cardinality detection. Exports interactive HTML dashboards and JSON summaries."
verification: "security_reviewed"
source: "https://github.com/pandas-dev/pandas"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "pandas-dev/pandas"
  github_stars: 48498
  license: "BSD-3-Clause"
---

# Pandas Profiling Report Generator

The Pandas Profiling Report Generator leverages ydata-profiling to create exhaustive exploratory data analysis reports from CSV, Parquet, and database query results. It computes univariate statistics, bivariate correlation matrices (Pearson, Spearman, Kendall, Cramér’s V), and identifies high-cardinality categorical columns that may need encoding strategies.

Missing value analysis goes beyond simple counts, detecting MCAR/MAR/MNAR patterns using Little’s test and visualizing missingness correlations as heatmaps. Duplicate row detection with configurable subset columns helps identify data quality issues before they propagate downstream.

The skill generates interactive HTML reports with collapsible sections, exportable to static PNG charts for documentation. JSON summary output integrates with CI/CD pipelines for automated data quality gates, failing builds when null percentages exceed thresholds or when new columns appear unexpectedly in source schemas. Supports Spark DataFrames via the pandas API on Spark for large-scale profiling.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pandas-profiling-report-generator/)
