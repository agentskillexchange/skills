---
name: "dbt Model Lineage Mapper"
description: "Parses dbt manifest.json and catalog.json to extract full model lineage graphs using the dbt Core artifact API. Generates interactive DAG visualizations and impact analysis for model changes."
category: "Data Extraction & Transformation"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/dbt-model-lineage-mapper/"
tool_ecosystem:
  tool: dbt
  github_stars: 12460
  github_repo: dbt-labs/dbt-core
  maintained: true
---

# dbt Model Lineage Mapper

Parses dbt manifest.json and catalog.json to extract full model lineage graphs using the dbt Core artifact API. Generates interactive DAG visualizations and impact analysis for model changes.

## Overview

The dbt Model Lineage Mapper skill analyzes dbt project artifacts (manifest.json, catalog.json, run_results.json) to construct comprehensive data lineage graphs from source to exposure. It leverages the dbt artifact schema to map dependencies across models, sources, seeds, snapshots, and exposures.

The skill builds a complete DAG showing upstream and downstream dependencies for any node, calculates critical path analysis for pipeline optimization, and identifies orphaned models with no downstream consumers. It cross-references catalog.json to enrich lineage with actual column-level lineage where available, tracing how specific columns flow through transformations.

Impact analysis features let you specify proposed model changes and see all affected downstream models, tests, and exposures. It calculates blast radius metrics and can generate PR descriptions summarizing lineage impact. The skill also validates ref() and source() function usage, detects circular dependencies, and checks model naming convention compliance.

Visualization outputs include Mermaid DAG diagrams, D3-compatible JSON for interactive exploration, and formatted Markdown reports. It can compare lineage between two manifest versions to show how the DAG evolved across releases.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill dbt-model-lineage-mapper
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill dbt-model-lineage-mapper -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill dbt-model-lineage-mapper -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill dbt-model-lineage-mapper -a codex
```

### OpenClaw

```bash
clawhub install dbt-model-lineage-mapper
```

## Source

- Marketplace: https://agentskillexchange.com/skills/dbt-model-lineage-mapper/
