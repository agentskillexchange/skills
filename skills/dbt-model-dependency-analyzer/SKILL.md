---
name: "dbt Model Dependency Analyzer"
description: "Analyzes dbt project DAGs using the dbt manifest.json artifact and the dbt Cloud API. Detects circular dependencies, orphaned models, and generates lineage visualizations."
category: "Data Extraction & Transformation"
framework: "Claude Code"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/dbt-model-dependency-analyzer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "dbt"  # from ase_tool_match
  github_stars: 12457  # from ase_github_stars (integer, not string)
  github_repo: "dbt-labs/dbt-core"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# dbt Model Dependency Analyzer

Analyzes dbt project DAGs using the dbt manifest.json artifact and the dbt Cloud API. Detects circular dependencies, orphaned models, and generates lineage visualizations.

## Overview

Data transformation project analysis agent for dbt (data build tool) projects. Parses the manifest.json artifact to construct complete model dependency graphs including sources, seeds, snapshots, and exposures. Connects to the dbt Cloud API for run history analysis and model timing optimization. Detects circular dependencies, orphaned models without downstream consumers, and overly deep DAG chains that impact build performance. Generates interactive lineage visualizations using D3.js force-directed graphs. Analyzes SQL compilation output to identify expensive cross-database references and suggest materialization strategy changes between views, tables, and incremental models. Validates ref() and source() macro usage for correctness. Integrates with data catalog tools via the dbt exposures API for downstream impact analysis. Supports multi-project dependency analysis across dbt mesh architectures.

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

## Source

- Marketplace: https://agentskillexchange.com/skills/dbt-model-dependency-analyzer/
