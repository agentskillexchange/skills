---
title: "dbt Model Dependency Resolver"
description: "Analyzes dbt project DAGs to identify circular references, orphaned models, and suboptimal materialization strategies. Uses dbt-core manifest.json parsing with Jinja template resolution for accurate lineage tracking."
slug: "dbt-model-dependency-resolver-2"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Claude Code"
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/dbt-model-dependency-resolver-2/"
listed: true
---

# dbt Model Dependency Resolver

Analyzes dbt project DAGs to identify circular references, orphaned models, and suboptimal materialization strategies. Uses dbt-core manifest.json parsing with Jinja template resolution for accurate lineage tracking.

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
clawhub install dbt-model-dependency-resolver-2
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The dbt Model Dependency Resolver skill provides deep analysis of dbt project directed acyclic graphs (DAGs) by parsing manifest.json artifacts and resolving Jinja template references across models, sources, and exposures. It identifies circular dependencies, orphaned models without downstream consumers, and models with excessive fan-out that impact warehouse compute costs.
The skill evaluates materialization strategies (view, table, incremental, ephemeral) against query patterns and data volumes, recommending optimal configurations. It detects anti-patterns like full-refresh incrementals on large tables, missing unique tests on primary keys, and source freshness configurations without warning thresholds.
Integration with Snowflake query history and BigQuery INFORMATION_SCHEMA enables cost attribution per model, helping teams prioritize optimization efforts. The resolver generates visual DAG diffs between branches for PR reviews and exports lineage metadata in OpenLineage format for cross-platform data governance.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dbt-model-dependency-resolver-2/)
