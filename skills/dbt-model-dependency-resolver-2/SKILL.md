---
title: "dbt Model Dependency Resolver"
description: "Analyzes dbt project DAGs to identify circular references, orphaned models, and suboptimal materialization strategies. Uses dbt-core manifest.json parsing with Jinja template resolution for accurate lineage tracking."
verification: "security_reviewed"
source: "https://github.com/dbt-labs/dbt-core"
category:
  - "Data Extraction & Transformation"
framework:
  - "Claude Code"
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "dbt-labs/dbt-core"
  github_stars: 12621
---

# dbt Model Dependency Resolver

The dbt Model Dependency Resolver skill provides deep analysis of dbt project directed acyclic graphs (DAGs) by parsing manifest.json artifacts and resolving Jinja template references across models, sources, and exposures. It identifies circular dependencies, orphaned models without downstream consumers, and models with excessive fan-out that impact warehouse compute costs.

The skill evaluates materialization strategies (view, table, incremental, ephemeral) against query patterns and data volumes, recommending optimal configurations. It detects anti-patterns like full-refresh incrementals on large tables, missing unique tests on primary keys, and source freshness configurations without warning thresholds.

Integration with Snowflake query history and BigQuery INFORMATION_SCHEMA enables cost attribution per model, helping teams prioritize optimization efforts. The resolver generates visual DAG diffs between branches for PR reviews and exports lineage metadata in OpenLineage format for cross-platform data governance.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/dbt-model-dependency-resolver-2/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/dbt-model-dependency-resolver-2
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/dbt-model-dependency-resolver-2`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dbt-model-dependency-resolver-2/)
