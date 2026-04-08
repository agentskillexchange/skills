---
title: Apache Spark DataFrame ETL Pipeline
description: The Apache Spark DataFrame ETL Pipeline skill automates complex data
  engineering workflows using PySpark and the Spark SQL API. It handles schema inference
  from heterogeneous data sources including Parquet, ORC, Avro, and JSON formats,
  applying automatic type coercion and null handling strategies. Key capabilities
  include partition pruning optimization for large-scale datasets, predicate pushdown
  to minimize I/O, and adaptive query execution tuning. The skill integrates natively
  with Delta Lake for ACID-compliant merge operations (MERGE INTO), enabling upsert
  patterns across billion-row tables. For cloud-native deployments, it connects to
  AWS Glue Data Catalog for centralized metadata management, supports Apache Iceberg
  table formats for schema evolution, and configures Spark session parameters for
  optimal memory and shuffle partition settings. Data quality checks via Great Expectations
  are built in, validating row counts, null percentages, and statistical distributions
  before committing writes.
verification: security_reviewed
source: https://agentskillexchange.com/skills/spark-dataframe-etl-pipeline/
category:
- Data Extraction &amp; Transformation
framework:
- OpenClaw
---

# Apache Spark DataFrame ETL Pipeline

The Apache Spark DataFrame ETL Pipeline skill automates complex data engineering workflows using PySpark and the Spark SQL API. It handles schema inference from heterogeneous data sources including Parquet, ORC, Avro, and JSON formats, applying automatic type coercion and null handling strategies. Key capabilities include partition pruning optimization for large-scale datasets, predicate pushdown to minimize I/O, and adaptive query execution tuning. The skill integrates natively with Delta Lake for ACID-compliant merge operations (MERGE INTO), enabling upsert patterns across billion-row tables. For cloud-native deployments, it connects to AWS Glue Data Catalog for centralized metadata management, supports Apache Iceberg table formats for schema evolution, and configures Spark session parameters for optimal memory and shuffle partition settings. Data quality checks via Great Expectations are built in, validating row counts, null percentages, and statistical distributions before committing writes.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/spark-dataframe-etl-pipeline/)
