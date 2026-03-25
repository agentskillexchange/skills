---
name: "Apache Spark DataFrame ETL Pipeline"
description: "Automates PySpark DataFrame transformations including schema inference, partition pruning, and Delta Lake merge operations. Integrates with AWS Glue Data Catalog and Apache Iceberg table formats for lakehouse architectures."
category: "Data Extraction & Transformation"
framework: "OpenClaw"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/spark-dataframe-etl-pipeline/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "spark"  # from ase_tool_match
  github_stars: 43027  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 9204385  # from ase_npm_downloads
  github_repo: "apache/spark"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Apache Spark DataFrame ETL Pipeline

Automates PySpark DataFrame transformations including schema inference, partition pruning, and Delta Lake merge operations. Integrates with AWS Glue Data Catalog and Apache Iceberg table formats for lakehouse architectures.

## Overview

The Apache Spark DataFrame ETL Pipeline skill automates complex data engineering workflows using PySpark and the Spark SQL API. It handles schema inference from heterogeneous data sources including Parquet, ORC, Avro, and JSON formats, applying automatic type coercion and null handling strategies.

Key capabilities include partition pruning optimization for large-scale datasets, predicate pushdown to minimize I/O, and adaptive query execution tuning. The skill integrates natively with Delta Lake for ACID-compliant merge operations (MERGE INTO), enabling upsert patterns across billion-row tables.

For cloud-native deployments, it connects to AWS Glue Data Catalog for centralized metadata management, supports Apache Iceberg table formats for schema evolution, and configures Spark session parameters for optimal memory and shuffle partition settings. Data quality checks via Great Expectations are built in, validating row counts, null percentages, and statistical distributions before committing writes.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill spark-dataframe-etl-pipeline
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill spark-dataframe-etl-pipeline -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill spark-dataframe-etl-pipeline -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill spark-dataframe-etl-pipeline -a codex
```

### OpenClaw

```bash
clawhub install spark-dataframe-etl-pipeline
```

## Source

- Marketplace: https://agentskillexchange.com/skills/spark-dataframe-etl-pipeline/
