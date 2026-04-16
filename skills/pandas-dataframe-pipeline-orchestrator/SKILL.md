---
title: "Pandas DataFrame Pipeline Orchestrator"
description: "Chains pandas DataFrame transformations into reproducible pipelines using pipe() method composition. Handles missing data imputation with fillna() strategies, type coercion with astype(), and memory optimization via category dtypes."
verification: "security_reviewed"
source: "https://github.com/pandas-dev/pandas"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "pandas-dev/pandas"
  github_stars: 48498
  license: "BSD-3-Clause"
---

# Pandas DataFrame Pipeline Orchestrator

The Pandas DataFrame Pipeline Orchestrator builds reproducible data transformation pipelines by composing pandas operations using the DataFrame.pipe() method. It chains cleaning, transformation, and validation steps into reusable pipeline functions that maintain data lineage.

Core transformations include missing data handling with configurable fillna() strategies (forward fill, interpolation, mean/median imputation), type coercion via astype() with error handling modes, and memory optimization by converting object columns to pd.CategoricalDtype. The skill profiles DataFrames using df.memory_usage(deep=True) to identify optimization targets.

Advanced features include multi-index operations with set_index() and stack()/unstack(), window functions via rolling() and expanding(), and custom aggregations using agg() with named aggregation syntax. The agent generates data quality reports with completeness percentages, uniqueness checks, and distribution statistics. Supports chunked processing for large files via pd.read_csv(chunksize=) with iterator-based pipeline execution. Includes schema validation against pandera DataFrameSchema definitions.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pandas-dataframe-pipeline-orchestrator/)
