---
title: "Compare dbt models and warehouse relations before trusting migration parity with dbt-audit-helper"
description: "Lets an agent run dbt parity checks, relation diffs, and row or value comparisons so refactors and source swaps can be verified before rollout."
verification: "listed"
source: "https://github.com/dbt-labs/dbt-audit-helper"
category:
  - "Data Extraction & Transformation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "dbt-labs/dbt-audit-helper"
  github_stars: 402
---

# Compare dbt models and warehouse relations before trusting migration parity with dbt-audit-helper

Use dbt-audit-helper when an agent needs to prove that a dbt refactor, relation swap, or migration still matches expected warehouse results. It fits analytics engineering work where parity evidence is needed before trust is restored. Invoke this instead of using dbt normally when the agent must run targeted comparison macros, inspect row and value differences, and document migration parity. This is skill-shaped because the workflow boundary is precise: compare dbt relations and outputs during change validation. It is not a generic dbt package listing or broad data transformation platform card.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/compare-dbt-models-and-warehouse-relations-before-trusting-migration-parity-with-dbt-audit-helper/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/compare-dbt-models-and-warehouse-relations-before-trusting-migration-parity-with-dbt-audit-helper
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/compare-dbt-models-and-warehouse-relations-before-trusting-migration-parity-with-dbt-audit-helper`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/compare-dbt-models-and-warehouse-relations-before-trusting-migration-parity-with-dbt-audit-helper/)
