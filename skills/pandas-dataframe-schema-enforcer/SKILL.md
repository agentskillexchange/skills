---
name: "Pandas DataFrame Schema Enforcer"
description: "Validates and transforms Pandas DataFrames using Pandera schema definitions with column-level dtype, nullable, and custom check constraints. Auto-generates Pandera schema code from sample DataFrames."
category: "Data Extraction & Transformation"
framework: "ChatGPT Agents"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/pandas-dataframe-schema-enforcer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "pandas"  # from ase_tool_match
  github_stars: 48224  # from ase_github_stars (integer, not string)
  github_repo: "pandas-dev/pandas"  # from ase_github_repo
  license: "BSD-3-Clause"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Pandas DataFrame Schema Enforcer

Validates and transforms Pandas DataFrames using Pandera schema definitions with column-level dtype, nullable, and custom check constraints. Auto-generates Pandera schema code from sample DataFrames.

## Overview

The Pandas DataFrame Schema Enforcer skill integrates **Pandera** with Pandas to provide runtime data validation for DataFrame pipelines. It defines and enforces column-level schemas including data types, nullable constraints, value ranges, regex patterns, and custom validation functions.

The skill auto-generates Pandera SchemaModel classes from sample DataFrames, inferring appropriate column types and constraints from data distributions. It supports both eager validation (fail-fast on first error) and lazy validation (collect all errors) modes, with detailed error reporting including row indices and failing values.

Advanced features include schema evolution tracking, hypothesis testing integration for statistical property validation, and integration with Great Expectations for cross-platform data quality checks. The skill generates transformation code to coerce non-conforming data, handles timezone-aware datetime columns, and supports MultiIndex validation for hierarchical DataFrames.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill pandas-dataframe-schema-enforcer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill pandas-dataframe-schema-enforcer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill pandas-dataframe-schema-enforcer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill pandas-dataframe-schema-enforcer -a codex
```

### OpenClaw

```bash
clawhub install pandas-dataframe-schema-enforcer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/pandas-dataframe-schema-enforcer/
