---
title: "dbt Model Dependency Analyzer"
description: "Analyzes dbt project DAGs using the dbt manifest.json artifact and the dbt Cloud API. Detects circular dependencies, orphaned models, and generates lineage visualizations."
slug: "dbt-model-dependency-analyzer"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/dbt-model-dependency-analyzer/"
listed: true
---

# dbt Model Dependency Analyzer

Analyzes dbt project DAGs using the dbt manifest.json artifact and the dbt Cloud API. Detects circular dependencies, orphaned models, and generates lineage visualizations.

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
clawhub install dbt-model-dependency-analyzer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Data transformation project analysis agent for dbt (data build tool) projects. Parses the manifest.json artifact to construct complete model dependency graphs including sources, seeds, snapshots, and exposures. Connects to the dbt Cloud API for run history analysis and model timing optimization. Detects circular dependencies, orphaned models without downstream consumers, and overly deep DAG chains that impact build performance. Generates interactive lineage visualizations using D3.js force-directed graphs. Analyzes SQL compilation output to identify expensive cross-database references and suggest materialization strategy changes between views, tables, and incremental models. Validates ref() and source() macro usage for correctness. Integrates with data catalog tools via the dbt exposures API for downstream impact analysis. Supports multi-project dependency analysis across dbt mesh architectures.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dbt-model-dependency-analyzer/)
