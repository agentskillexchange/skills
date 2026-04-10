---
title: "dbt Data Transformation Orchestrator"
description: "Manages dbt Core and dbt Cloud API workflows for SQL-based data transformations. Handles model lineage, incremental builds, and data quality tests with Great Expectations integration."
slug: "dbt-data-transformation-orchestrator"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/dbt-data-transformation-orchestrator/"
---

# dbt Data Transformation Orchestrator

Manages dbt Core and dbt Cloud API workflows for SQL-based data transformations. Handles model lineage, incremental builds, and data quality tests with Great Expectations integration.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install dbt-data-transformation-orchestrator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The dbt Data Transformation Orchestrator manages analytics engineering workflows through both dbt Core CLI and dbt Cloud Administrative API. It handles model compilation, execution, testing, and documentation across data warehouse platforms including Snowflake, BigQuery, Redshift, and DuckDB.
The skill manages dbt project configuration including profiles.yml, dbt_project.yml, and packages.yml for dependency management. Model lineage is tracked through ref() and source() macro resolution, generating DAG visualizations for impact analysis before running transformations.
Incremental model management optimizes build times by configuring merge strategies, unique keys, and incremental predicates. The agent supports snapshot strategies (timestamp and check) for slowly changing dimension tracking and manages seed files for reference data loading.
Data quality testing combines dbt native tests (unique, not_null, accepted_values, relationships) with Great Expectations integration for statistical validation including column distribution checks, outlier detection, and referential integrity verification. The dbt Cloud API integration supports triggering jobs, monitoring run status, and fetching artifacts programmatically for CI/CD pipeline integration. Documentation generation produces data dictionaries with column-level descriptions and freshness monitoring.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dbt-data-transformation-orchestrator/)
