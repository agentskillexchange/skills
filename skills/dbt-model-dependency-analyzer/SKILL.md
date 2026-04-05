---
name: "dbt Model Dependency Analyzer"
description: "Analyzes dbt project DAGs using the dbt manifest.json artifact and the dbt Cloud API. Detects circular dependencies, orphaned models, and generates lineage visualizations."
category: "Data Extraction &amp; Transformation"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/dbt-model-dependency-analyzer/"
---
# dbt Model Dependency Analyzer

Analyzes dbt project DAGs using the dbt manifest.json artifact and the dbt Cloud API. Detects circular dependencies, orphaned models, and generates lineage visualizations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill dbt-model-dependency-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill dbt-model-dependency-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill dbt-model-dependency-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill dbt-model-dependency-analyzer -a codex
```

### OpenClaw

```bash
clawhub install dbt-model-dependency-analyzer
```

## Details

Data transformation project analysis agent for dbt (data build tool) projects. Parses the manifest.json artifact to construct complete model dependency graphs including sources, seeds, snapshots, and exposures. Connects to the dbt Cloud API for run history analysis and model timing optimization. Detects circular dependencies, orphaned models without downstream consumers, and overly deep DAG chains that impact build performance. Generates interactive lineage visualizations using D3.js force-directed graphs. Analyzes SQL compilation output to identify expensive cross-database references and suggest materialization strategy changes between views, tables, and incremental models. Validates ref() and source() macro usage for correctness. Integrates with data catalog tools via the dbt exposures API for downstream impact analysis. Supports multi-project dependency analysis across dbt mesh architectures.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dbt-model-dependency-analyzer/)
