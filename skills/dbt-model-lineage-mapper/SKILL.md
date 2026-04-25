---
title: "dbt Model Lineage Mapper"
description: "Parses dbt manifest.json and catalog.json to extract full model lineage graphs using the dbt Core artifact API. Generates interactive DAG visualizations and impact analysis for model changes."
verification: "security_reviewed"
source: "https://github.com/dbt-labs/dbt-core"
category:
  - "Data Extraction & Transformation"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "dbt-labs/dbt-core"
  github_stars: 12621
---

# dbt Model Lineage Mapper

The dbt Model Lineage Mapper skill analyzes dbt project artifacts (manifest.json, catalog.json, run_results.json) to construct comprehensive data lineage graphs from source to exposure. It leverages the dbt artifact schema to map dependencies across models, sources, seeds, snapshots, and exposures. The skill builds a complete DAG showing upstream and downstream dependencies for any node, calculates critical path analysis for pipeline optimization, and identifies orphaned models with no downstream consumers. It cross-references catalog.json to enrich lineage with actual column-level lineage where available, tracing how specific columns flow through transformations. Impact analysis features let you specify proposed model changes and see all affected downstream models, tests, and exposures. It calculates blast radius metrics and can generate PR descriptions summarizing lineage impact. The skill also validates ref() and source() function usage, detects circular dependencies, and checks model naming convention compliance. Visualization outputs include Mermaid DAG diagrams, D3-compatible JSON for interactive exploration, and formatted Markdown reports. It can compare lineage between two manifest versions to show how the DAG evolved across releases.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/dbt-model-lineage-mapper/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/dbt-model-lineage-mapper
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/dbt-model-lineage-mapper`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dbt-model-lineage-mapper/)
