---
name: Pandas DataFrame Pipeline Orchestrator
description: Chains pandas DataFrame transformations into reproducible pipelines using
  pipe() method composition. Handles missing data imputation with fillna() strategies,
  type coercion with astype(), and memory optimization via category dtypes.
verification: security_reviewed
source: https://agentskillexchange.com/skills/pandas-dataframe-pipeline-orchestrator/
category:
- Data Extraction &amp; Transformation
framework:
- ChatGPT Agents
---
# Pandas DataFrame Pipeline Orchestrator

The Pandas DataFrame Pipeline Orchestrator builds reproducible data transformation pipelines by composing pandas operations using the DataFrame.pipe() method. It chains cleaning, transformation, and validation steps into reusable pipeline functions that maintain data lineage.
Core transformations include missing data handling with configurable fillna() strategies (forward fill, interpolation, mean/median imputation), type coercion via astype() with error handling modes, and memory optimization by converting object columns to pd.CategoricalDtype. The skill profiles DataFrames using df.memory_usage(deep=True) to identify optimization targets.
Advanced features include multi-index operations with set_index() and stack()/unstack(), window functions via rolling() and expanding(), and custom aggregations using agg() with named aggregation syntax. The agent generates data quality reports with completeness percentages, uniqueness checks, and distribution statistics. Supports chunked processing for large files via pd.read_csv(chunksize=) with iterator-based pipeline execution. Includes schema validation against pandera DataFrameSchema definitions.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pandas-dataframe-pipeline-orchestrator/)
