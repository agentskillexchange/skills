---
name: "Pandas DataFrame Pipeline Builder"
description: "Constructs data transformation pipelines using Pandas and the pipe() method chain pattern. Integrates with SQLAlchemy for database I/O and PyArrow for high-performance Parquet operations."
category: "Data Extraction & Transformation"
framework: "Cursor"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/pandas-dataframe-pipeline-builder/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "pandas"  # from ase_tool_match
  github_stars: 48239  # from ase_github_stars (integer, not string)
  github_repo: "pandas-dev/pandas"  # from ase_github_repo
  license: "BSD-3-Clause"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Pandas DataFrame Pipeline Builder

Constructs data transformation pipelines using Pandas and the pipe() method chain pattern. Integrates with SQLAlchemy for database I/O and PyArrow for high-performance Parquet operations.

## Overview

Data transformation pipeline construction agent using the Pandas library. Builds composable transformation pipelines using the DataFrame.pipe() method chain pattern for readable and testable data processing. Implements common transformations including type casting, null handling, deduplication, pivoting, and window functions. Integrates with SQLAlchemy for reading from and writing to relational databases including PostgreSQL, MySQL, and BigQuery via the pandas-gbq connector. Uses PyArrow as the computation backend for high-performance Parquet file operations and columnar data processing. Supports schema validation using Pandera with automatic data quality checks at each pipeline stage. Implements chunked processing for datasets exceeding available memory using Dask DataFrame as a drop-in replacement. Generates pipeline documentation with input/output schema descriptions and transformation logs for data lineage tracking.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill pandas-dataframe-pipeline-builder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill pandas-dataframe-pipeline-builder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill pandas-dataframe-pipeline-builder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill pandas-dataframe-pipeline-builder -a codex
```

### OpenClaw

```bash
clawhub install pandas-dataframe-pipeline-builder
```

## Source

- Marketplace: https://agentskillexchange.com/skills/pandas-dataframe-pipeline-builder/
