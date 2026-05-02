---
title: "dbt Model Lineage Analyzer"
description: "Parses dbt project manifests and catalog artifacts to build complete data lineage graphs. Uses the dbt Cloud API v2 for run metadata and the dbt Core manifest.json for model dependency analysis."
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

# dbt Model Lineage Analyzer

The dbt Model Lineage Analyzer skill processes dbt Core manifest.json and catalog.json artifacts to construct comprehensive data lineage graphs across your analytics warehouse. It traces column-level lineage from source tables through staging, intermediate, and mart models, identifying transformation logic at each hop. The skill integrates with the dbt Cloud Administrative API v2 to pull run results, test outcomes, and freshness check data for operational lineage enrichment. Features include impact analysis for proposed model changes, orphan model detection, circular dependency identification, and exposure coverage reporting. Supports visualization export in DOT format for Graphviz rendering and Mermaid diagram syntax for documentation embedding. Provides automated data quality scoring based on test coverage, documentation completeness, and freshness SLA compliance.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/dbt-model-lineage-analyzer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/dbt-model-lineage-analyzer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/dbt-model-lineage-analyzer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dbt-model-lineage-analyzer/)
