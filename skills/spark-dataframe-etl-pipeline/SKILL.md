---
title: "Apache Spark DataFrame ETL Pipeline"
description: "Automates PySpark DataFrame transformations including schema inference, partition pruning, and Delta Lake merge operations. Integrates with AWS Glue Data Catalog and Apache Iceberg table formats for lakehouse architectures."
verification: "security_reviewed"
source: "https://github.com/apache/spark"
category:
  - "Data Extraction & Transformation"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "apache/spark"
  github_stars: 43117
  license: "Apache-2.0"
---

# Apache Spark DataFrame ETL Pipeline

The Apache Spark DataFrame ETL Pipeline skill automates complex data engineering workflows using PySpark and the Spark SQL API. It handles schema inference from heterogeneous data sources including Parquet, ORC, Avro, and JSON formats, applying automatic type coercion and null handling strategies.


Key capabilities include partition pruning optimization for large-scale datasets, predicate pushdown to minimize I/O, and adaptive query execution tuning. The skill integrates natively with Delta Lake for ACID-compliant merge operations (MERGE INTO), enabling upsert patterns across billion-row tables.


For cloud-native deployments, it connects to AWS Glue Data Catalog for centralized metadata management, supports Apache Iceberg table formats for schema evolution, and configures Spark session parameters for optimal memory and shuffle partition settings. Data quality checks via Great Expectations are built in, validating row counts, null percentages, and statistical distributions before committing writes.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/spark-dataframe-etl-pipeline/)
