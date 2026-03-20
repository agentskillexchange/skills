---
name: BigQuery Cost & Query Performance Auditor
description: Queries BigQuery INFORMATION_SCHEMA.JOBS_BY_PROJECT to identify top slot-consuming queries over 30 days. Surfaces optimization recommendations — partition pruning, clustering keys, redundant scans — w
category: Data Extraction & Transformation
framework: Custom Agents
verification: security_reviewed
rating: 4.8
reviews: 53
source: https://agentskillexchange.com/skill/bigquery-cost-query-performance-auditor-2/
---

# BigQuery Cost & Query Performance Auditor

Queries BigQuery INFORMATION_SCHEMA.JOBS_BY_PROJECT to identify top slot-consuming queries over 30 days. Surfaces optimization recommendations — partition pruning, clustering keys, redundant scans — with specific job IDs and estimated byte savings.

## Overview

Queries BigQuery INFORMATION_SCHEMA.JOBS_BY_PROJECT to identify top slot-consuming queries over 30 days. Surfaces optimization recommendations — partition pruning, clustering keys, redundant scans — with specific job IDs and estimated byte savings.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill bigquery-cost-query-performance-auditor-2
```

### OpenClaw

```bash
openclaw install bigquery-cost-query-performance-auditor-2
```

### Manual

Download this `SKILL.md` file and place it in your agent's skills directory.

## Metadata

| Field | Value |
|-------|-------|
| Category | Data Extraction & Transformation |
| Framework | Custom Agents |
| Verification | Security Reviewed |
| Rating | ⭐⭐⭐⭐ 4.8/5.0 (53 reviews) |

---

*Published on [Agent Skill Exchange](https://agentskillexchange.com/skill/bigquery-cost-query-performance-auditor-2/)*
