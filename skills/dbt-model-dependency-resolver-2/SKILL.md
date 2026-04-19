---
title: "dbt Model Dependency Resolver"
description: "The dbt Model Dependency Resolver skill provides deep analysis of dbt project directed acyclic graphs (DAGs) by parsing manifest.json artifacts and resolving Jinja template references across models, sources, and exposures. It identifies circular dependencies, orphaned models without downstream consumers, and models with excessive fan-out that impact warehouse compute costs. The skill evaluates materialization strategies (view, table, incremental, ephemeral) against query patterns and data volumes, recommending optimal configurations. It detects anti-patterns like full-refresh incrementals on large tables, missing unique tests on primary keys, and source freshness configurations without warning thresholds. Integration with Snowflake query history and BigQuery INFORMATION_SCHEMA enables cost attribution per model, helping teams prioritize optimization efforts. The resolver generates visual DAG diffs between branches for PR reviews and exports lineage metadata in OpenLineage format for cross-platform data governance."
source: "https://github.com/dbt-labs/dbt-core"
verification: "security_reviewed"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Claude Code"
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "dbt-labs/dbt-core"
  github_stars: 12621
---

# dbt Model Dependency Resolver

The dbt Model Dependency Resolver skill provides deep analysis of dbt project directed acyclic graphs (DAGs) by parsing manifest.json artifacts and resolving Jinja template references across models, sources, and exposures. It identifies circular dependencies, orphaned models without downstream consumers, and models with excessive fan-out that impact warehouse compute costs. The skill evaluates materialization strategies (view, table, incremental, ephemeral) against query patterns and data volumes, recommending optimal configurations. It detects anti-patterns like full-refresh incrementals on large tables, missing unique tests on primary keys, and source freshness configurations without warning thresholds. Integration with Snowflake query history and BigQuery INFORMATION_SCHEMA enables cost attribution per model, helping teams prioritize optimization efforts. The resolver generates visual DAG diffs between branches for PR reviews and exports lineage metadata in OpenLineage format for cross-platform data governance.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dbt-model-dependency-resolver-2/)
