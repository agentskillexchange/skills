---
title: dbt Data Transformation Orchestrator
description: The dbt Data Transformation Orchestrator manages analytics engineering
  workflows through both dbt Core CLI and dbt Cloud Administrative API. It handles
  model compilation, execution, testing, and documentation across data warehouse platforms
  including Snowflake, BigQuery, Redshift, and DuckDB. The skill manages dbt project
  configuration including profiles.yml, dbt_project.yml, and packages.yml for dependency
  management. Model lineage is tracked through ref() and source() macro resolution,
  generating DAG visualizations for impact analysis before running transformations.
  Incremental model management optimizes build times by configuring merge strategies,
  unique keys, and incremental predicates. The agent supports snapshot strategies
  (timestamp and check) for slowly changing dimension tracking and manages seed files
  for reference data loading. Data quality testing combines dbt native tests (unique,
  not_null, accepted_values, relationships) with Great Expectations integration for
  statistical validation including column distribution checks, outlier detection,
  and referential integrity verification. The dbt Cloud API integration supports triggering
  jobs, monitoring run status, and fetching artifacts programmatically for CI/CD pipeline
  integration. Documentation generation produces data dictionaries with column-level
  descriptions and freshness monitoring.
verification: security_reviewed
source: https://agentskillexchange.com/skills/dbt-data-transformation-orchestrator/
category:
- Data Extraction &amp; Transformation
framework:
- Claude Code
---

# dbt Data Transformation Orchestrator

The dbt Data Transformation Orchestrator manages analytics engineering workflows through both dbt Core CLI and dbt Cloud Administrative API. It handles model compilation, execution, testing, and documentation across data warehouse platforms including Snowflake, BigQuery, Redshift, and DuckDB. The skill manages dbt project configuration including profiles.yml, dbt_project.yml, and packages.yml for dependency management. Model lineage is tracked through ref() and source() macro resolution, generating DAG visualizations for impact analysis before running transformations. Incremental model management optimizes build times by configuring merge strategies, unique keys, and incremental predicates. The agent supports snapshot strategies (timestamp and check) for slowly changing dimension tracking and manages seed files for reference data loading. Data quality testing combines dbt native tests (unique, not_null, accepted_values, relationships) with Great Expectations integration for statistical validation including column distribution checks, outlier detection, and referential integrity verification. The dbt Cloud API integration supports triggering jobs, monitoring run status, and fetching artifacts programmatically for CI/CD pipeline integration. Documentation generation produces data dictionaries with column-level descriptions and freshness monitoring.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dbt-data-transformation-orchestrator/)
