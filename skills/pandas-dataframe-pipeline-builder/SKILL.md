---
name: "Pandas DataFrame Pipeline Builder"
description: "Constructs data transformation pipelines using Pandas and the pipe() method chain pattern. Integrates with SQLAlchemy for database I/O and PyArrow for high-performance Parquet operations."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/pandas-dataframe-pipeline-builder/"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Cursor"
---

# Pandas DataFrame Pipeline Builder

Data transformation pipeline construction agent using the Pandas library. Builds composable transformation pipelines using the DataFrame.pipe() method chain pattern for readable and testable data processing. Implements common transformations including type casting, null handling, deduplication, pivoting, and window functions. Integrates with SQLAlchemy for reading from and writing to relational databases including PostgreSQL, MySQL, and BigQuery via the pandas-gbq connector. Uses PyArrow as the computation backend for high-performance Parquet file operations and columnar data processing. Supports schema validation using Pandera with automatic data quality checks at each pipeline stage. Implements chunked processing for datasets exceeding available memory using Dask DataFrame as a drop-in replacement. Generates pipeline documentation with input/output schema descriptions and transformation logs for data lineage tracking.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pandas-dataframe-pipeline-builder/)
