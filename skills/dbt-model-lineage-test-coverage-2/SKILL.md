---
title: "dbt Model Lineage &amp; Test Coverage Checker"
description: "Parses dbt project artifacts (manifest.json and catalog.json) to build a lineage graph and identify models with no tests, stale documentation, or missing uniqueness assertions. Integrates with dbt Cloud API to fetch latest run results and annotates each model with pass/fail status."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/dbt-model-lineage-test-coverage-2/"
category:
  - "Data Extraction &amp; Transformation"
---

# dbt Model Lineage &amp; Test Coverage Checker

Parses dbt project artifacts (manifest.json and catalog.json) to build a lineage graph and identify models with no tests, stale documentation, or missing uniqueness assertions. Integrates with dbt Cloud API to fetch latest run results and annotates each model with pass/fail status.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dbt-model-lineage-test-coverage-2/)
