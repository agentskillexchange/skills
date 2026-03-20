---
name: "dbt Model Lineage & Test Coverage Checker"
description: "Parses dbt project artifacts (manifest.json and catalog.json) to build a lineage graph and identify models with no tests, stale documentation, or missing uniqueness assertions. Integrates with dbt Cloud API to fetch the latest run results and annotates each model with its last pass/fail status."
category: "Data Extraction & Transformation"
framework: "Cursor"
verification: 
rating: 4.3
reviews: 13
creator: Yuki Tanaka
creator_handle: yukitanaka
creator_verified: true
source: https://agentskillexchange.com/skill/dbt-model-lineage-test-coverage/
---

# dbt Model Lineage & Test Coverage Checker

Parses dbt project artifacts (manifest.json and catalog.json) to build a lineage graph and identify models with no tests, stale documentation, or missing uniqueness assertions. Integrates with dbt Cloud API to fetch the latest run results and annotates each model with its last pass/fail status.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill dbt-model-lineage-test-coverage
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill dbt-model-lineage-test-coverage -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill dbt-model-lineage-test-coverage -a cursor
```

### OpenClaw

```bash
clawhub install dbt-model-lineage-test-coverage
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill dbt-model-lineage-test-coverage -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Data Extraction & Transformation |
| Framework | Cursor |
| Verification | Listed |
| Rating | 4.3/5 (13 reviews) |

## Creator

**Yuki Tanaka** (Verified Creator ✓)
- Profile: [@yukitanaka](https://agentskillexchange.com/browse-skills/?creator=yukitanaka)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/dbt-model-lineage-test-coverage/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
