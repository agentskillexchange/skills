---
name: "Compare dbt models and warehouse relations before trusting migration parity with dbt-audit-helper"
slug: "compare-dbt-models-and-warehouse-relations-before-trusting-migration-parity-with-dbt-audit-helper"
description: "Lets an agent run dbt parity checks, relation diffs, and row or value comparisons so refactors and source swaps can be verified before rollout."
github_stars: 402
verification: "security_reviewed"
source: "https://github.com/dbt-labs/dbt-audit-helper"
author: "dbt Labs"
publisher_type: "organization"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "dbt-labs/dbt-audit-helper"
  github_stars: 402
---

# Compare dbt models and warehouse relations before trusting migration parity with dbt-audit-helper

Lets an agent run dbt parity checks, relation diffs, and row or value comparisons so refactors and source swaps can be verified before rollout.

## Prerequisites

dbt Core, warehouse credentials, dbt-audit-helper package

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Add dbt-labs/audit_helper to packages.yml, then run dbt deps.
```

## Documentation

- https://hub.getdbt.com/dbt-labs/audit_helper/latest/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/compare-dbt-models-and-warehouse-relations-before-trusting-migration-parity-with-dbt-audit-helper/)
