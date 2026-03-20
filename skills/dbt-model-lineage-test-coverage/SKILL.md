---
name: dbt Model Lineage & Test Coverage Checker
description: Parses dbt project artifacts (manifest.json and catalog.json) to build a lineage graph and identify models with no tests, stale documentation, or missing uniqueness assertions. Integrates with dbt Cloud API to fetch the latest run results and annotates each model with its last pass/fail status.
category: Data Extraction &amp; Transformation
framework: Any Agent
verification: listed
rating: 4.3
reviews: 13
source: https://agentskillexchange.com/skill/dbt-model-lineage-test-coverage/
---

# dbt Model Lineage & Test Coverage Checker

Parses dbt project artifacts (manifest.json and catalog.json) to build a lineage graph and identify models with no tests, stale documentation, or missing uniqueness assertions. Integrates with dbt Cloud API to fetch the latest run results and annotates each model with its last pass/fail status.

## Overview

Parses dbt project artifacts (manifest.json and catalog.json) to build a lineage graph and identify models with no tests, stale documentation, or missing uniqueness assertions. Integrates with dbt Cloud API to fetch the latest run results and annotates each model with its last pass/fail status.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill dbt-model-lineage-test-coverage
```

### OpenClaw

```bash
clawhub install dbt-model-lineage-test-coverage
```

### Claude Code

```bash
claude mcp add dbt-model-lineage-test-coverage
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/dbt-model-lineage-test-coverage/) for detailed installation instructions.

## Verification

- **Status**: listed
- **Category**: Data Extraction &amp; Transformation
- **Framework**: Any Agent
- **Rating**: 4.3/5 (13 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/dbt-model-lineage-test-coverage/)
