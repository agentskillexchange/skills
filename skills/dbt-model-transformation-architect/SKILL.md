---
title: "dbt Model Transformation Architect"
description: "Generates and validates dbt (data build tool) models, tests, and documentation for Snowflake, BigQuery, and Redshift. Parses dbt manifest.json to analyze DAG lineage and detect circular dependencies."
verification: "security_reviewed"
source: "https://github.com/dbt-labs/dbt-core"
category:
  - "Data Extraction & Transformation"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "dbt-labs/dbt-core"
  github_stars: 12621
---

# dbt Model Transformation Architect

The dbt Model Transformation Architect skill automates the creation and validation of dbt (data build tool) transformation models across cloud data warehouses. It generates SQL models following dbt best practices including staging/intermediate/mart layer conventions and incremental materialization strategies.

The skill parses dbt’s manifest.json and catalog.json artifacts to analyze the transformation DAG, detecting circular dependencies, orphaned models, and fan-out anti-patterns. It generates schema.yml files with column descriptions, data tests (not_null, unique, accepted_values, relationships), and source freshness checks.

Advanced features include generating dbt macros for common transformation patterns, creating custom generic tests, and scaffolding dbt packages with proper namespace isolation. The skill validates Jinja SQL syntax before compilation, suggests ref() and source() corrections, and generates dbt documentation blocks with DAG visualization metadata for dbt docs integration.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/dbt-model-transformation-architect/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/dbt-model-transformation-architect
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/dbt-model-transformation-architect`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dbt-model-transformation-architect/)
