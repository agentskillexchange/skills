---
title: "dbt Model Lineage &amp; Test Coverage Checker"
slug: "dbt-model-lineage-test-coverage-2"
description: "Parses dbt project artifacts (manifest.json and catalog.json) to build a lineage graph and identify models with no tests, stale documentation, or missing uniqueness assertions. Integrates with dbt Cloud API to fetch latest run results and annotates each model with pass/fail status."
verification: security_reviewed
source: "https://github.com/dbt-labs/dbt-core"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "dbt-labs/dbt-core"
  github_stars: 12621
---

# dbt Model Lineage &amp; Test Coverage Checker

Parses dbt project artifacts (manifest.json and catalog.json) to build a lineage graph and identify models with no tests, stale documentation, or missing uniqueness assertions. Integrates with dbt Cloud API to fetch latest run results and annotates each model with pass/fail status.

## Installation

1. Clone this skill into your local skills directory.
2. Review the required tools and environment variables.
3. Install dependencies with your preferred package manager or runtime.
4. Run the upstream install command from the project documentation, if needed.
5. Validate the installation and test the skill in your agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dbt-model-lineage-test-coverage-2/)
