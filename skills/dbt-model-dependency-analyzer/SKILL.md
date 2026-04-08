---
title: dbt Model Dependency Analyzer
description: Data transformation project analysis agent for dbt (data build tool)
  projects. Parses the manifest.json artifact to construct complete model dependency
  graphs including sources, seeds, snapshots, and exposures. Connects to the dbt Cloud
  API for run history analysis and model timing optimization. Detects circular dependencies,
  orphaned models without downstream consumers, and overly deep DAG chains that impact
  build performance. Generates interactive lineage visualizations using D3.js force-directed
  graphs. Analyzes SQL compilation output to identify expensive cross-database references
  and suggest materialization strategy changes between views, tables, and incremental
  models. Validates ref() and source() macro usage for correctness. Integrates with
  data catalog tools via the dbt exposures API for downstream impact analysis. Supports
  multi-project dependency analysis across dbt mesh architectures.
verification: security_reviewed
source: https://agentskillexchange.com/skills/dbt-model-dependency-analyzer/
category:
- Data Extraction &amp; Transformation
framework:
- Claude Code
---

# dbt Model Dependency Analyzer

Data transformation project analysis agent for dbt (data build tool) projects. Parses the manifest.json artifact to construct complete model dependency graphs including sources, seeds, snapshots, and exposures. Connects to the dbt Cloud API for run history analysis and model timing optimization. Detects circular dependencies, orphaned models without downstream consumers, and overly deep DAG chains that impact build performance. Generates interactive lineage visualizations using D3.js force-directed graphs. Analyzes SQL compilation output to identify expensive cross-database references and suggest materialization strategy changes between views, tables, and incremental models. Validates ref() and source() macro usage for correctness. Integrates with data catalog tools via the dbt exposures API for downstream impact analysis. Supports multi-project dependency analysis across dbt mesh architectures.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dbt-model-dependency-analyzer/)
