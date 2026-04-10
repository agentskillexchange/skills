---
title: "Pandas DataFrame Pipeline Orchestrator"
description: "Chains pandas DataFrame transformations into reproducible pipelines using pipe() method composition. Handles missing data imputation with fillna() strategies, type coercion with astype(), and memory optimization via category dtypes."
slug: "pandas-dataframe-pipeline-orchestrator"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/pandas-dataframe-pipeline-orchestrator/"
---

# Pandas DataFrame Pipeline Orchestrator

Chains pandas DataFrame transformations into reproducible pipelines using pipe() method composition. Handles missing data imputation with fillna() strategies, type coercion with astype(), and memory optimization via category dtypes.

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
clawhub install pandas-dataframe-pipeline-orchestrator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Pandas DataFrame Pipeline Orchestrator builds reproducible data transformation pipelines by composing pandas operations using the DataFrame.pipe() method. It chains cleaning, transformation, and validation steps into reusable pipeline functions that maintain data lineage.
Core transformations include missing data handling with configurable fillna() strategies (forward fill, interpolation, mean/median imputation), type coercion via astype() with error handling modes, and memory optimization by converting object columns to pd.CategoricalDtype. The skill profiles DataFrames using df.memory_usage(deep=True) to identify optimization targets.
Advanced features include multi-index operations with set_index() and stack()/unstack(), window functions via rolling() and expanding(), and custom aggregations using agg() with named aggregation syntax. The agent generates data quality reports with completeness percentages, uniqueness checks, and distribution statistics. Supports chunked processing for large files via pd.read_csv(chunksize=) with iterator-based pipeline execution. Includes schema validation against pandera DataFrameSchema definitions.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pandas-dataframe-pipeline-orchestrator/)
