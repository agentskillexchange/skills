---
name: dbt Data Transformation Orchestrator
description: Manages dbt Core and dbt Cloud API workflows for SQL-based data transformations.
  Handles model lineage, incremental builds, and data quality tests with Great Expectations
  integration.
verification: security_reviewed
source: https://agentskillexchange.com/skills/dbt-data-transformation-orchestrator/
category:
- Data Extraction &amp; Transformation
framework:
- Claude Code
---
# dbt Data Transformation Orchestrator

The dbt Data Transformation Orchestrator manages analytics engineering workflows through both dbt Core CLI and dbt Cloud Administrative API. It handles model compilation, execution, testing, and documentation across data warehouse platforms including Snowflake, BigQuery, Redshift, and DuckDB.
The skill manages dbt project configuration including profiles.yml, dbt_project.yml, and packages.yml for dependency management. Model lineage is tracked through ref() and source() macro resolution, generating DAG visualizations for impact analysis before running transformations.
Incremental model management optimizes build times by configuring merge strategies, unique keys, and incremental predicates. The agent supports snapshot strategies (timestamp and check) for slowly changing dimension tracking and manages seed files for reference data loading.
Data quality testing combines dbt native tests (unique, not_null, accepted_values, relationships) with Great Expectations integration for statistical validation including column distribution checks, outlier detection, and referential integrity verification. The dbt Cloud API integration supports triggering jobs, monitoring run status, and fetching artifacts programmatically for CI/CD pipeline integration. Documentation generation produces data dictionaries with column-level descriptions and freshness monitoring.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dbt-data-transformation-orchestrator/)
