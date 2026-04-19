---
title: "dbt Model Dependency Analyzer"
description: "Data transformation project analysis agent for dbt (data build tool) projects. Parses the manifest.json artifact to construct complete model dependency graphs including sources, seeds, snapshots, and exposures. Connects to the dbt Cloud API for run history analysis and model timing optimization. Detects circular dependencies, orphaned models without downstream consumers, and overly deep DAG chains that impact build performance. Generates interactive lineage visualizations using D3.js force-directed graphs. Analyzes SQL compilation output to identify expensive cross-database references and suggest materialization strategy changes between views, tables, and incremental models. Validates ref() and source() macro usage for correctness. Integrates with data catalog tools via the dbt exposures API for downstream impact analysis. Supports multi-project dependency analysis across dbt mesh architectures."
source: "https://github.com/dbt-labs/dbt-core"
verification: "security_reviewed"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "dbt-labs/dbt-core"
  github_stars: 12621
---

# dbt Model Dependency Analyzer

Data transformation project analysis agent for dbt (data build tool) projects. Parses the manifest.json artifact to construct complete model dependency graphs including sources, seeds, snapshots, and exposures. Connects to the dbt Cloud API for run history analysis and model timing optimization. Detects circular dependencies, orphaned models without downstream consumers, and overly deep DAG chains that impact build performance. Generates interactive lineage visualizations using D3.js force-directed graphs. Analyzes SQL compilation output to identify expensive cross-database references and suggest materialization strategy changes between views, tables, and incremental models. Validates ref() and source() macro usage for correctness. Integrates with data catalog tools via the dbt exposures API for downstream impact analysis. Supports multi-project dependency analysis across dbt mesh architectures.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dbt-model-dependency-analyzer/)
