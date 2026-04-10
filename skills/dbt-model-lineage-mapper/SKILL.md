---
title: "dbt Model Lineage Mapper"
description: "Parses dbt manifest.json and catalog.json to extract full model lineage graphs using the dbt Core artifact API. Generates interactive DAG visualizations and impact analysis for model changes."
slug: "dbt-model-lineage-mapper"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/dbt-model-lineage-mapper/"
listed: true
---

# dbt Model Lineage Mapper

Parses dbt manifest.json and catalog.json to extract full model lineage graphs using the dbt Core artifact API. Generates interactive DAG visualizations and impact analysis for model changes.

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
clawhub install dbt-model-lineage-mapper
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The dbt Model Lineage Mapper skill analyzes dbt project artifacts (manifest.json, catalog.json, run_results.json) to construct comprehensive data lineage graphs from source to exposure. It leverages the dbt artifact schema to map dependencies across models, sources, seeds, snapshots, and exposures.
The skill builds a complete DAG showing upstream and downstream dependencies for any node, calculates critical path analysis for pipeline optimization, and identifies orphaned models with no downstream consumers. It cross-references catalog.json to enrich lineage with actual column-level lineage where available, tracing how specific columns flow through transformations.
Impact analysis features let you specify proposed model changes and see all affected downstream models, tests, and exposures. It calculates blast radius metrics and can generate PR descriptions summarizing lineage impact. The skill also validates ref() and source() function usage, detects circular dependencies, and checks model naming convention compliance.
Visualization outputs include Mermaid DAG diagrams, D3-compatible JSON for interactive exploration, and formatted Markdown reports. It can compare lineage between two manifest versions to show how the DAG evolved across releases.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dbt-model-lineage-mapper/)
