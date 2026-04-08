---
title: dbt Model Transformation Architect
description: The dbt Model Transformation Architect skill automates the creation and
  validation of dbt (data build tool) transformation models across cloud data warehouses.
  It generates SQL models following dbt best practices including staging/intermediate/mart
  layer conventions and incremental materialization strategies. The skill parses dbt’s
  manifest.json and catalog.json artifacts to analyze the transformation DAG, detecting
  circular dependencies, orphaned models, and fan-out anti-patterns. It generates
  schema.yml files with column descriptions, data tests (not_null, unique, accepted_values,
  relationships), and source freshness checks. Advanced features include generating
  dbt macros for common transformation patterns, creating custom generic tests, and
  scaffolding dbt packages with proper namespace isolation. The skill validates Jinja
  SQL syntax before compilation, suggests ref() and source() corrections, and generates
  dbt documentation blocks with DAG visualization metadata for dbt docs integration.
verification: security_reviewed
source: https://agentskillexchange.com/skills/dbt-model-transformation-architect/
category:
- Data Extraction &amp; Transformation
framework:
- Claude Agents
---

# dbt Model Transformation Architect

The dbt Model Transformation Architect skill automates the creation and validation of dbt (data build tool) transformation models across cloud data warehouses. It generates SQL models following dbt best practices including staging/intermediate/mart layer conventions and incremental materialization strategies. The skill parses dbt’s manifest.json and catalog.json artifacts to analyze the transformation DAG, detecting circular dependencies, orphaned models, and fan-out anti-patterns. It generates schema.yml files with column descriptions, data tests (not_null, unique, accepted_values, relationships), and source freshness checks. Advanced features include generating dbt macros for common transformation patterns, creating custom generic tests, and scaffolding dbt packages with proper namespace isolation. The skill validates Jinja SQL syntax before compilation, suggests ref() and source() corrections, and generates dbt documentation blocks with DAG visualization metadata for dbt docs integration.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dbt-model-transformation-architect/)
