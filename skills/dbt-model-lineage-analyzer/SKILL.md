---
title: dbt Model Lineage Analyzer
description: The dbt Model Lineage Analyzer skill processes dbt Core manifest.json
  and catalog.json artifacts to construct comprehensive data lineage graphs across
  your analytics warehouse. It traces column-level lineage from source tables through
  staging, intermediate, and mart models, identifying transformation logic at each
  hop. The skill integrates with the dbt Cloud Administrative API v2 to pull run results,
  test outcomes, and freshness check data for operational lineage enrichment. Features
  include impact analysis for proposed model changes, orphan model detection, circular
  dependency identification, and exposure coverage reporting. Supports visualization
  export in DOT format for Graphviz rendering and Mermaid diagram syntax for documentation
  embedding. Provides automated data quality scoring based on test coverage, documentation
  completeness, and freshness SLA compliance.
verification: security_reviewed
source: https://agentskillexchange.com/skills/dbt-model-lineage-analyzer/
category:
- Data Extraction &amp; Transformation
framework:
- Claude Agents
---

# dbt Model Lineage Analyzer

The dbt Model Lineage Analyzer skill processes dbt Core manifest.json and catalog.json artifacts to construct comprehensive data lineage graphs across your analytics warehouse. It traces column-level lineage from source tables through staging, intermediate, and mart models, identifying transformation logic at each hop. The skill integrates with the dbt Cloud Administrative API v2 to pull run results, test outcomes, and freshness check data for operational lineage enrichment. Features include impact analysis for proposed model changes, orphan model detection, circular dependency identification, and exposure coverage reporting. Supports visualization export in DOT format for Graphviz rendering and Mermaid diagram syntax for documentation embedding. Provides automated data quality scoring based on test coverage, documentation completeness, and freshness SLA compliance.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dbt-model-lineage-analyzer/)
