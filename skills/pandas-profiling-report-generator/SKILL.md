---
name: "Pandas Profiling Report Generator"
description: "Generates comprehensive data quality reports using ydata-profiling (formerly pandas-profiling) with correlation analysis, missing value patterns, and cardinality detection. Exports interactive HTML dashboards and JSON summaries."
category: "Data Extraction & Transformation"
framework: "Codex"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/pandas-profiling-report-generator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "pandas"  # from ase_tool_match
  github_stars: 48224  # from ase_github_stars (integer, not string)
  github_repo: "pandas-dev/pandas"  # from ase_github_repo
  license: "BSD-3-Clause"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Pandas Profiling Report Generator

Generates comprehensive data quality reports using ydata-profiling (formerly pandas-profiling) with correlation analysis, missing value patterns, and cardinality detection. Exports interactive HTML dashboards and JSON summaries.

## Overview

The Pandas Profiling Report Generator leverages ydata-profiling to create exhaustive exploratory data analysis reports from CSV, Parquet, and database query results. It computes univariate statistics, bivariate correlation matrices (Pearson, Spearman, Kendall, Cramér’s V), and identifies high-cardinality categorical columns that may need encoding strategies.

Missing value analysis goes beyond simple counts, detecting MCAR/MAR/MNAR patterns using Little’s test and visualizing missingness correlations as heatmaps. Duplicate row detection with configurable subset columns helps identify data quality issues before they propagate downstream.

The skill generates interactive HTML reports with collapsible sections, exportable to static PNG charts for documentation. JSON summary output integrates with CI/CD pipelines for automated data quality gates, failing builds when null percentages exceed thresholds or when new columns appear unexpectedly in source schemas. Supports Spark DataFrames via the pandas API on Spark for large-scale profiling.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill pandas-profiling-report-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill pandas-profiling-report-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill pandas-profiling-report-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill pandas-profiling-report-generator -a codex
```

### OpenClaw

```bash
clawhub install pandas-profiling-report-generator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/pandas-profiling-report-generator/
