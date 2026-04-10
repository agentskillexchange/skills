---
name: "dbt Model Lineage Analyzer"
description: "Parses dbt project manifests and catalog artifacts to build complete data lineage graphs. Uses the dbt Cloud API v2 for run metadata and the dbt Core manifest.json for model dependency analysis."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/dbt-model-lineage-analyzer/"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Claude Agents"
---

# dbt Model Lineage Analyzer

The dbt Model Lineage Analyzer skill processes dbt Core manifest.json and catalog.json artifacts to construct comprehensive data lineage graphs across your analytics warehouse. It traces column-level lineage from source tables through staging, intermediate, and mart models, identifying transformation logic at each hop. The skill integrates with the dbt Cloud Administrative API v2 to pull run results, test outcomes, and freshness check data for operational lineage enrichment. Features include impact analysis for proposed model changes, orphan model detection, circular dependency identification, and exposure coverage reporting. Supports visualization export in DOT format for Graphviz rendering and Mermaid diagram syntax for documentation embedding. Provides automated data quality scoring based on test coverage, documentation completeness, and freshness SLA compliance.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dbt-model-lineage-analyzer/)
