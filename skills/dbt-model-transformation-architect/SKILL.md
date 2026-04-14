---
title: "dbt Model Transformation Architect"
description: "Generates and validates dbt (data build tool) models, tests, and documentation for Snowflake, BigQuery, and Redshift. Parses dbt manifest.json to analyze DAG lineage and detect circular dependencies."
verification: security_reviewed
source: "https://github.com/dbt-labs/dbt-core"
category:
  - "Data Extraction &amp; Transformation"
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dbt-model-transformation-architect/)
