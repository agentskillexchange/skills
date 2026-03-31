---
name: "Apache Spark DataFrame ETL Pipeline"
description: "Automates PySpark DataFrame transformations including schema inference, partition pruning, and Delta Lake merge operations. Integrates with AWS Glue Data Catalog and Apache Iceberg table formats for lakehouse architectures."
category: "Data Extraction &amp; Transformation"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/spark-dataframe-etl-pipeline/"
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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/spark-dataframe-etl-pipeline/)
