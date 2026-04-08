---
title: dlt Python Data Load Tool
description: 'dlt (data load tool) is an open-source Python library maintained by
  dlt-hub that transforms the way developers build and maintain data pipelines. With
  over 5,000 GitHub stars, active development, and an Apache 2.0 license, dlt has
  emerged as one of the most practical data loading frameworks in the Python ecosystem.
  How It Works dlt lets you write data pipelines in pure Python. You define a source
  (REST API, SQL database, cloud storage, or raw Python data structures), and dlt
  handles the heavy lifting: it infers schemas and data types, normalizes nested JSON
  structures into relational tables, and loads the result into your chosen destination.
  The pipeline definition is typically under 20 lines of Python code. dlt uses a declarative
  REST API source that lets you configure pagination, authentication, and response
  parsing without writing custom extraction logic. Key Capabilities dlt supports incremental
  loading with merge, append, and replace write dispositions. Schema evolution is
  automatic — when source data changes shape, dlt adapts the destination schema accordingly.
  Schema and data contracts let you enforce strict rules on incoming data, catching
  breaking changes before they hit your warehouse. The library supports over 30 destinations
  out of the box, including DuckDB, BigQuery, Snowflake, Redshift, PostgreSQL, Motherduck,
  Databricks, and filesystem targets for Parquet and CSV output. A custom destination
  interface enables reverse ETL patterns by routing pipeline output to any Python
  callable. Integration Points dlt runs anywhere Python runs: Google Colab notebooks,
  AWS Lambda, Apache Airflow DAGs, GitHub Actions, or local machines. It integrates
  with dbt for downstream transformations and supports Marimo Notebooks for data visualization.
  The dlt MCP server enables AI agents to inspect and run pipelines interactively.
  SQL and Python data access interfaces make it easy to query loaded data programmatically.
  With over 5,000 pre-built source configurations in the dlt workspace hub, most common
  APIs already have verified extraction patterns ready to use. What It Produces dlt
  outputs structured, typed datasets in your destination of choice. Every pipeline
  run produces a trace with metadata including row counts, schema changes, and load
  timing. The pipeline dashboard provides a visual overview of runs, schema state,
  and data lineage. dlt follows semantic versioning and maintains backward compatibility
  across minor releases.'
verification: security_reviewed
source: https://github.com/dlt-hub/dlt
category:
- Data Extraction &amp; Transformation
framework:
- Custom Agents
tool_ecosystem:
  github_repo: dlt-hub/dlt
  github_stars: 5161
---

# dlt Python Data Load Tool

dlt (data load tool) is an open-source Python library maintained by dlt-hub that transforms the way developers build and maintain data pipelines. With over 5,000 GitHub stars, active development, and an Apache 2.0 license, dlt has emerged as one of the most practical data loading frameworks in the Python ecosystem. How It Works dlt lets you write data pipelines in pure Python. You define a source (REST API, SQL database, cloud storage, or raw Python data structures), and dlt handles the heavy lifting: it infers schemas and data types, normalizes nested JSON structures into relational tables, and loads the result into your chosen destination. The pipeline definition is typically under 20 lines of Python code. dlt uses a declarative REST API source that lets you configure pagination, authentication, and response parsing without writing custom extraction logic. Key Capabilities dlt supports incremental loading with merge, append, and replace write dispositions. Schema evolution is automatic — when source data changes shape, dlt adapts the destination schema accordingly. Schema and data contracts let you enforce strict rules on incoming data, catching breaking changes before they hit your warehouse. The library supports over 30 destinations out of the box, including DuckDB, BigQuery, Snowflake, Redshift, PostgreSQL, Motherduck, Databricks, and filesystem targets for Parquet and CSV output. A custom destination interface enables reverse ETL patterns by routing pipeline output to any Python callable. Integration Points dlt runs anywhere Python runs: Google Colab notebooks, AWS Lambda, Apache Airflow DAGs, GitHub Actions, or local machines. It integrates with dbt for downstream transformations and supports Marimo Notebooks for data visualization. The dlt MCP server enables AI agents to inspect and run pipelines interactively. SQL and Python data access interfaces make it easy to query loaded data programmatically. With over 5,000 pre-built source configurations in the dlt workspace hub, most common APIs already have verified extraction patterns ready to use. What It Produces dlt outputs structured, typed datasets in your destination of choice. Every pipeline run produces a trace with metadata including row counts, schema changes, and load timing. The pipeline dashboard provides a visual overview of runs, schema state, and data lineage. dlt follows semantic versioning and maintains backward compatibility across minor releases.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dlt-python-data-load-tool/)
