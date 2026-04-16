---
title: "dbt Data Transformation Orchestrator"
description: "Manages dbt Core and dbt Cloud API workflows for SQL-based data transformations. Handles model lineage, incremental builds, and data quality tests with Great Expectations integration."
verification: "security_reviewed"
source: "https://github.com/dbt-labs/dbt-core"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "dbt-labs/dbt-core"
  github_stars: 12621
---

# dbt Data Transformation Orchestrator

The dbt Data Transformation Orchestrator manages analytics engineering workflows through both dbt Core CLI and dbt Cloud Administrative API. It handles model compilation, execution, testing, and documentation across data warehouse platforms including Snowflake, BigQuery, Redshift, and DuckDB.

The skill manages dbt project configuration including profiles.yml, dbt_project.yml, and packages.yml for dependency management. Model lineage is tracked through ref() and source() macro resolution, generating DAG visualizations for impact analysis before running transformations.

Incremental model management optimizes build times by configuring merge strategies, unique keys, and incremental predicates. The agent supports snapshot strategies (timestamp and check) for slowly changing dimension tracking and manages seed files for reference data loading.

Data quality testing combines dbt native tests (unique, not_null, accepted_values, relationships) with Great Expectations integration for statistical validation including column distribution checks, outlier detection, and referential integrity verification. The dbt Cloud API integration supports triggering jobs, monitoring run status, and fetching artifacts programmatically for CI/CD pipeline integration. Documentation generation produces data dictionaries with column-level descriptions and freshness monitoring.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dbt-data-transformation-orchestrator/)
