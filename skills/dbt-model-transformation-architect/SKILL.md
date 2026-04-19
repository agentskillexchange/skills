---
title: "dbt Model Transformation Architect"
description: "The dbt Model Transformation Architect skill automates the creation and validation of dbt (data build tool) transformation models across cloud data warehouses. It generates SQL models following dbt best practices including staging/intermediate/mart layer conventions and incremental materialization strategies. The skill parses dbt&#8217;s manifest.json and catalog.json artifacts to analyze the transformation DAG, detecting circular dependencies, orphaned models, and fan-out anti-patterns. It generates schema.yml files with column descriptions, data tests (not_null, unique, accepted_values, relationships), and source freshness checks. Advanced features include generating dbt macros for common transformation patterns, creating custom generic tests, and scaffolding dbt packages with proper namespace isolation. The skill validates Jinja SQL syntax before compilation, suggests ref() and source() corrections, and generates dbt documentation blocks with DAG visualization metadata for dbt docs integration."
source: "https://github.com/dbt-labs/dbt-core"
verification: "security_reviewed"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "dbt-labs/dbt-core"
  github_stars: 12621
---

# dbt Model Transformation Architect

The dbt Model Transformation Architect skill automates the creation and validation of dbt (data build tool) transformation models across cloud data warehouses. It generates SQL models following dbt best practices including staging/intermediate/mart layer conventions and incremental materialization strategies. The skill parses dbt&#8217;s manifest.json and catalog.json artifacts to analyze the transformation DAG, detecting circular dependencies, orphaned models, and fan-out anti-patterns. It generates schema.yml files with column descriptions, data tests (not_null, unique, accepted_values, relationships), and source freshness checks. Advanced features include generating dbt macros for common transformation patterns, creating custom generic tests, and scaffolding dbt packages with proper namespace isolation. The skill validates Jinja SQL syntax before compilation, suggests ref() and source() corrections, and generates dbt documentation blocks with DAG visualization metadata for dbt docs integration.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dbt-model-transformation-architect/)
