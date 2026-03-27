---
name: "Pandas DataFrame Pipeline Orchestrator"
description: "Chains pandas DataFrame transformations into reproducible pipelines using pipe() method composition. Handles missing data imputation with fillna() strategies, type coercion with astype(), and memory optimization via category dtypes."
category: "Data Extraction & Transformation"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/pandas-dataframe-pipeline-orchestrator/"
tool_ecosystem:
  tool: pandas
  github_stars: 48239
  github_repo: pandas-dev/pandas
  license: BSD-3-Clause
  maintained: true
---

# Pandas DataFrame Pipeline Orchestrator

Chains pandas DataFrame transformations into reproducible pipelines using pipe() method composition. Handles missing data imputation with fillna() strategies, type coercion with astype(), and memory optimization via category dtypes.

## Overview

The Pandas DataFrame Pipeline Orchestrator builds reproducible data transformation pipelines by composing pandas operations using the `DataFrame.pipe()` method. It chains cleaning, transformation, and validation steps into reusable pipeline functions that maintain data lineage.

Core transformations include missing data handling with configurable `fillna()` strategies (forward fill, interpolation, mean/median imputation), type coercion via `astype()` with error handling modes, and memory optimization by converting object columns to `pd.CategoricalDtype`. The skill profiles DataFrames using `df.memory_usage(deep=True)` to identify optimization targets.

Advanced features include multi-index operations with `set_index()` and `stack()/unstack()`, window functions via `rolling()` and `expanding()`, and custom aggregations using `agg()` with named aggregation syntax. The agent generates data quality reports with completeness percentages, uniqueness checks, and distribution statistics. Supports chunked processing for large files via `pd.read_csv(chunksize=)` with iterator-based pipeline execution. Includes schema validation against pandera DataFrameSchema definitions.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill pandas-dataframe-pipeline-orchestrator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill pandas-dataframe-pipeline-orchestrator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill pandas-dataframe-pipeline-orchestrator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill pandas-dataframe-pipeline-orchestrator -a codex
```

### OpenClaw

```bash
clawhub install pandas-dataframe-pipeline-orchestrator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/pandas-dataframe-pipeline-orchestrator/
