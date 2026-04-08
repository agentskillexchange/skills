---
title: dbt Model Lineage Mapper
description: The dbt Model Lineage Mapper skill analyzes dbt project artifacts (manifest.json,
  catalog.json, run_results.json) to construct comprehensive data lineage graphs from
  source to exposure. It leverages the dbt artifact schema to map dependencies across
  models, sources, seeds, snapshots, and exposures. The skill builds a complete DAG
  showing upstream and downstream dependencies for any node, calculates critical path
  analysis for pipeline optimization, and identifies orphaned models with no downstream
  consumers. It cross-references catalog.json to enrich lineage with actual column-level
  lineage where available, tracing how specific columns flow through transformations.
  Impact analysis features let you specify proposed model changes and see all affected
  downstream models, tests, and exposures. It calculates blast radius metrics and
  can generate PR descriptions summarizing lineage impact. The skill also validates
  ref() and source() function usage, detects circular dependencies, and checks model
  naming convention compliance. Visualization outputs include Mermaid DAG diagrams,
  D3-compatible JSON for interactive exploration, and formatted Markdown reports.
  It can compare lineage between two manifest versions to show how the DAG evolved
  across releases.
verification: security_reviewed
source: https://agentskillexchange.com/skills/dbt-model-lineage-mapper/
category:
- Data Extraction &amp; Transformation
framework:
- OpenClaw
---

# dbt Model Lineage Mapper

The dbt Model Lineage Mapper skill analyzes dbt project artifacts (manifest.json, catalog.json, run_results.json) to construct comprehensive data lineage graphs from source to exposure. It leverages the dbt artifact schema to map dependencies across models, sources, seeds, snapshots, and exposures. The skill builds a complete DAG showing upstream and downstream dependencies for any node, calculates critical path analysis for pipeline optimization, and identifies orphaned models with no downstream consumers. It cross-references catalog.json to enrich lineage with actual column-level lineage where available, tracing how specific columns flow through transformations. Impact analysis features let you specify proposed model changes and see all affected downstream models, tests, and exposures. It calculates blast radius metrics and can generate PR descriptions summarizing lineage impact. The skill also validates ref() and source() function usage, detects circular dependencies, and checks model naming convention compliance. Visualization outputs include Mermaid DAG diagrams, D3-compatible JSON for interactive exploration, and formatted Markdown reports. It can compare lineage between two manifest versions to show how the DAG evolved across releases.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dbt-model-lineage-mapper/)
