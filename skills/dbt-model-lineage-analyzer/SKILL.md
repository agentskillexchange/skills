---
name: "dbt Model Lineage Analyzer"
description: "Parses dbt project manifests and catalog artifacts to build complete data lineage graphs. Uses the dbt Cloud API v2 for run metadata and the dbt Core manifest.json for model dependency analysis."
category: "Data Extraction & Transformation"
framework: "Claude Agents"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/dbt-model-lineage-analyzer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "dbt"  # from ase_tool_match
  github_stars: 12457  # from ase_github_stars (integer, not string)
  github_repo: "dbt-labs/dbt-core"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# dbt Model Lineage Analyzer

Parses dbt project manifests and catalog artifacts to build complete data lineage graphs. Uses the dbt Cloud API v2 for run metadata and the dbt Core manifest.json for model dependency analysis.

## Overview

The dbt Model Lineage Analyzer skill processes dbt Core manifest.json and catalog.json artifacts to construct comprehensive data lineage graphs across your analytics warehouse. It traces column-level lineage from source tables through staging, intermediate, and mart models, identifying transformation logic at each hop. The skill integrates with the dbt Cloud Administrative API v2 to pull run results, test outcomes, and freshness check data for operational lineage enrichment. Features include impact analysis for proposed model changes, orphan model detection, circular dependency identification, and exposure coverage reporting. Supports visualization export in DOT format for Graphviz rendering and Mermaid diagram syntax for documentation embedding. Provides automated data quality scoring based on test coverage, documentation completeness, and freshness SLA compliance.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill dbt-model-lineage-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill dbt-model-lineage-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill dbt-model-lineage-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill dbt-model-lineage-analyzer -a codex
```

### OpenClaw

```bash
clawhub install dbt-model-lineage-analyzer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/dbt-model-lineage-analyzer/
