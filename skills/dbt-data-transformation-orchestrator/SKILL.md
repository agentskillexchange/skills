---
title: "dbt Data Transformation Orchestrator"
description: "The dbt Data Transformation Orchestrator manages analytics engineering workflows through both dbt Core CLI and dbt Cloud Administrative API. It handles model compilation, execution, testing, and documentation across data warehouse platforms including Snowflake, BigQuery, Redshift, and DuckDB.\nThe skill manages dbt project configuration including profiles.yml, dbt_project.yml, and packages.yml for dependency management. Model lineage is tracked through ref() and source() macro resolution, generating DAG visualizations for impact analysis before running transformations.\nIncremental model management optimizes build times by configuring merge strategies, unique keys, and incremental predicates. The agent supports snapshot strategies (timestamp and check) for slowly changing dimension tracking and manages seed files for reference data loading.\nData quality testing combines dbt native tests (unique, not_null, accepted_values, relationships) with Great Expectations integration for statistical validation including column distribution checks, outlier detection, and referential integrity verification. The dbt Cloud API integration supports triggering jobs, monitoring run status, and fetching artifacts programmatically for CI/CD pipeline integration. Documentation generation produces data dictionaries with column-level descriptions and freshness monitoring."
verification: security_reviewed
source: "https://github.com/dbt-labs/dbt-core"
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

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/dbt-data-transformation-orchestrator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/dbt-data-transformation-orchestrator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dbt-data-transformation-orchestrator/)
