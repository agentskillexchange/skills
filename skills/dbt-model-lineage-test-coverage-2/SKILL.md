---
name: dbt Model Lineage & Test Coverage Checker
description: Parses dbt project artifacts (manifest.json and catalog.json) to build
  a lineage graph and identify models with no tests, stale documentation, or missing
  uniqueness assertions. Integrates with dbt Cloud API to fetch latest run results
  and annotates each model with pass/fail status.
category: Data Extraction & Transformation
framework: Cursor
verification: security_reviewed
source: https://github.com/dbt-labs/dbt-core
tool_ecosystem:
  github_repo: dbt-labs/dbt-core
  github_stars: 12621
  tool: dbt-core
  maintained: true
---
# dbt Model Lineage & Test Coverage Checker
Parses dbt project artifacts (manifest.json and catalog.json) to build a lineage graph and identify models with no tests, stale documentation, or missing uniqueness assertions. Integrates with dbt Cloud API to fetch latest run results and annotates each model with pass/fail status.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/dbt-model-lineage-test-coverage-2
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/dbt-model-lineage-test-coverage-2` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dbt-model-lineage-test-coverage-2/)
