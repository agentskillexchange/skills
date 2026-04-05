---
name: "dbt Model Transformation Architect"
description: "Generates and validates dbt (data build tool) models, tests, and documentation for Snowflake, BigQuery, and Redshift. Parses dbt manifest.json to analyze DAG lineage and detect circular dependencies."
category: "Data Extraction &amp; Transformation"
framework: "Claude Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/dbt-model-transformation-architect/"
---
# dbt Model Transformation Architect

Generates and validates dbt (data build tool) models, tests, and documentation for Snowflake, BigQuery, and Redshift. Parses dbt manifest.json to analyze DAG lineage and detect circular dependencies.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill dbt-model-transformation-architect
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill dbt-model-transformation-architect -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill dbt-model-transformation-architect -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill dbt-model-transformation-architect -a codex
```

### OpenClaw

```bash
clawhub install dbt-model-transformation-architect
```

## Details

The dbt Model Transformation Architect skill automates the creation and validation of dbt (data build tool) transformation models across cloud data warehouses. It generates SQL models following dbt best practices including staging/intermediate/mart layer conventions and incremental materialization strategies.

The skill parses dbt’s manifest.json and catalog.json artifacts to analyze the transformation DAG, detecting circular dependencies, orphaned models, and fan-out anti-patterns. It generates schema.yml files with column descriptions, data tests (not_null, unique, accepted_values, relationships), and source freshness checks.

Advanced features include generating dbt macros for common transformation patterns, creating custom generic tests, and scaffolding dbt packages with proper namespace isolation. The skill validates Jinja SQL syntax before compilation, suggests ref() and source() corrections, and generates dbt documentation blocks with DAG visualization metadata for dbt docs integration.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dbt-model-transformation-architect/)
