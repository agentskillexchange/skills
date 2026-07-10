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

Requirements and caveats from upstream:
- Each relation must have the same columns with the same names, but they do not have to be in the same order.
- Each relation must have the same columns with the same names, but they do not have to be in the same order. Build long lists with a few exclusions with dbt_utils.get_filtered_columns_in_relation, or pass None and the...
- Each relation must have the same columns with the same names, but they do not have to be in the same order. Use exclude_columns if some columns only exist in one relation.

Basic usage or getting-started notes:
- [Advanced Usage](#advanced-usage)
- New to dbt packages? Read more about them [here](https://docs.getdbt.com/docs/building-a-dbt-project/package-management/).
- Include this package in your packages.yml file — check [here](https://hub.getdbt.com/dbt-labs/audit_helper/latest/) for the latest version number.

- Source: https://github.com/dbt-labs/dbt-audit-helper
- Extracted from upstream docs: https://raw.githubusercontent.com/dbt-labs/dbt-audit-helper/HEAD/README.md

## Documentation

- https://hub.getdbt.com/dbt-labs/audit_helper/latest/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/compare-dbt-models-and-warehouse-relations-before-trusting-migration-parity-with-dbt-audit-helper/)
