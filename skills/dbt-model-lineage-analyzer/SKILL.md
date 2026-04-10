---
title: "dbt Model Lineage Analyzer"
description: "Parses dbt project manifests and catalog artifacts to build complete data lineage graphs. Uses the dbt Cloud API v2 for run metadata and the dbt Core manifest.json for model dependency analysis."
slug: "dbt-model-lineage-analyzer"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/dbt-model-lineage-analyzer/"
---

# dbt Model Lineage Analyzer

Parses dbt project manifests and catalog artifacts to build complete data lineage graphs. Uses the dbt Cloud API v2 for run metadata and the dbt Core manifest.json for model dependency analysis.

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
clawhub install dbt-model-lineage-analyzer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The dbt Model Lineage Analyzer skill processes dbt Core manifest.json and catalog.json artifacts to construct comprehensive data lineage graphs across your analytics warehouse. It traces column-level lineage from source tables through staging, intermediate, and mart models, identifying transformation logic at each hop. The skill integrates with the dbt Cloud Administrative API v2 to pull run results, test outcomes, and freshness check data for operational lineage enrichment. Features include impact analysis for proposed model changes, orphan model detection, circular dependency identification, and exposure coverage reporting. Supports visualization export in DOT format for Graphviz rendering and Mermaid diagram syntax for documentation embedding. Provides automated data quality scoring based on test coverage, documentation completeness, and freshness SLA compliance.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dbt-model-lineage-analyzer/)
