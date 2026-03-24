---
name: "dbt Model Lineage & Test Coverage Checker"
description: "Parses dbt project artifacts (manifest.json and catalog.json) to build a lineage graph and identify models with no tests, stale documentation, or missing uniqueness assertions. Integrates with dbt Cloud API to fetch latest run results and annotates each model with pass/fail status."
category: "Data Extraction & Transformation"
framework: "Cursor"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/dbt-model-lineage-test-coverage-2/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "dbt"  # from ase_tool_match
  github_stars: 12457  # from ase_github_stars (integer, not string)
  github_repo: "dbt-labs/dbt-core"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# dbt Model Lineage & Test Coverage Checker

Parses dbt project artifacts (manifest.json and catalog.json) to build a lineage graph and identify models with no tests, stale documentation, or missing uniqueness assertions. Integrates with dbt Cloud API to fetch latest run results and annotates each model with pass/fail status.

## Overview

Parses dbt project artifacts (manifest.json and catalog.json) to build a lineage graph and identify models with no tests, stale documentation, or missing uniqueness assertions. Integrates with dbt Cloud API to fetch latest run results and annotates each model with pass/fail status.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill dbt-model-lineage-test-coverage-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill dbt-model-lineage-test-coverage-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill dbt-model-lineage-test-coverage-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill dbt-model-lineage-test-coverage-2 -a codex
```

### OpenClaw

```bash
clawhub install dbt-model-lineage-test-coverage-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/dbt-model-lineage-test-coverage-2/
