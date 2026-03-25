---
name: "Pandas DataFrame Schema Validator"
description: "Validates Pandas DataFrame structures using the pandera library API and pa.DataFrameSchema definitions. Enforces column types, nullable constraints, and custom check functions via pandera.Check."
category: "Data Extraction & Transformation"
framework: "OpenClaw"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/pandas-dataframe-schema-validator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "pandas"  # from ase_tool_match
  github_stars: 48239  # from ase_github_stars (integer, not string)
  github_repo: "pandas-dev/pandas"  # from ase_github_repo
  license: "BSD-3-Clause"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Pandas DataFrame Schema Validator

Validates Pandas DataFrame structures using the pandera library API and pa.DataFrameSchema definitions. Enforces column types, nullable constraints, and custom check functions via pandera.Check.

## Overview

The Pandas DataFrame Schema Validator enforces data quality rules on Pandas DataFrames using the pandera schema validation library. It defines validation schemas using pa.DataFrameSchema with column-level type enforcement, nullable constraints, and value range specifications via pandera.Column definitions. The validator supports custom check functions using pandera.Check with lambda expressions, regex patterns, and statistical validations for distribution testing. It integrates with the pandas.api.types module to validate dtype compatibility across DataFrame operations. Schema inference is available using pandera.infer_schema() to generate baseline schemas from sample data, which can then be customized and tightened. The skill validates multi-index DataFrames, handles categorical dtype enforcement, and supports hypothesis testing checks using pandera.Hypothesis for statistical property validation. Error reporting generates detailed failure summaries with row indices, failing values, and schema violation categories.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill pandas-dataframe-schema-validator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill pandas-dataframe-schema-validator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill pandas-dataframe-schema-validator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill pandas-dataframe-schema-validator -a codex
```

### OpenClaw

```bash
clawhub install pandas-dataframe-schema-validator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/pandas-dataframe-schema-validator/
