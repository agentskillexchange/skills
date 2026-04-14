---
title: "dbt Model Dependency Analyzer"
description: "Analyzes dbt project DAGs using the dbt manifest.json artifact and the dbt Cloud API. Detects circular dependencies, orphaned models, and generates lineage visualizations."
verification: security_reviewed
source: "https://github.com/dbt-labs/dbt-core"
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dbt-model-dependency-analyzer/)
