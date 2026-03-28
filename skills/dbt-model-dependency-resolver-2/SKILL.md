---
name: "dbt Model Dependency Resolver"
description: "Analyzes dbt project DAGs to identify circular references, orphaned models, and suboptimal materialization strategies. Uses dbt-core manifest.json parsing with Jinja template resolution for accurate lineage tracking."
category: "Data Extraction & Transformation"
framework: "Claude Code"
verification: security_reviewed
source: "https://github.com/dbt-labs/dbt-core"
tool_ecosystem:
  tool: dbt
  github_stars: 12460
  github_repo: dbt-labs/dbt-core
  maintained: true
---

# dbt Model Dependency Resolver

Analyzes dbt project DAGs to identify circular references, orphaned models, and suboptimal materialization strategies. Uses dbt-core manifest.json parsing with Jinja template resolution for accurate lineage tracking.

## Overview

The dbt Model Dependency Resolver skill provides deep analysis of dbt project directed acyclic graphs (DAGs) by parsing manifest.json artifacts and resolving Jinja template references across models, sources, and exposures. It identifies circular dependencies, orphaned models without downstream consumers, and models with excessive fan-out that impact warehouse compute costs.

The skill evaluates materialization strategies (view, table, incremental, ephemeral) against query patterns and data volumes, recommending optimal configurations. It detects anti-patterns like full-refresh incrementals on large tables, missing unique tests on primary keys, and source freshness configurations without warning thresholds.

Integration with Snowflake query history and BigQuery INFORMATION_SCHEMA enables cost attribution per model, helping teams prioritize optimization efforts. The resolver generates visual DAG diffs between branches for PR reviews and exports lineage metadata in OpenLineage format for cross-platform data governance.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill dbt-model-dependency-resolver-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill dbt-model-dependency-resolver-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill dbt-model-dependency-resolver-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill dbt-model-dependency-resolver-2 -a codex
```

### OpenClaw

```bash
clawhub install dbt-model-dependency-resolver-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/dbt-model-dependency-resolver-2/
