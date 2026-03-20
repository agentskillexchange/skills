---
name: dbt Model Lineage & Test Coverage Checker
description: Parses dbt project artifacts (manifest.json and catalog.json) to build a lineage graph and identify models with no tests, stale documentation, or missing uniqueness assertions. Integrates with dbt Clo
category: Data Extraction & Transformation
framework: Cursor
verification: security_reviewed
rating: 4.8
reviews: 36
source: https://agentskillexchange.com/skill/dbt-model-lineage-test-coverage-2/
---

# dbt Model Lineage & Test Coverage Checker

Parses dbt project artifacts (manifest.json and catalog.json) to build a lineage graph and identify models with no tests, stale documentation, or missing uniqueness assertions. Integrates with dbt Cloud API to fetch latest run results and annotates each model with pass/fail status.

## Overview

Parses dbt project artifacts (manifest.json and catalog.json) to build a lineage graph and identify models with no tests, stale documentation, or missing uniqueness assertions. Integrates with dbt Cloud API to fetch latest run results and annotates each model with pass/fail status.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill dbt-model-lineage-test-coverage-2
```

### OpenClaw

```bash
openclaw install dbt-model-lineage-test-coverage-2
```

### Manual

Download this `SKILL.md` file and place it in your agent's skills directory.

## Metadata

| Field | Value |
|-------|-------|
| Category | Data Extraction & Transformation |
| Framework | Cursor |
| Verification | Security Reviewed |
| Rating | ⭐⭐⭐⭐ 4.8/5.0 (36 reviews) |

---

*Published on [Agent Skill Exchange](https://agentskillexchange.com/skill/dbt-model-lineage-test-coverage-2/)*
