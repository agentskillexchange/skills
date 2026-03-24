---
name: "BigQuery Cost & Query Performance Auditor"
description: "Queries BigQuery INFORMATION_SCHEMA.JOBS_BY_PROJECT to identify top slot-consuming queries over 30 days. Surfaces optimization recommendations — partition pruning, clustering keys, redundant scans — with specific job IDs and estimated byte savings."
category: "Data Extraction & Transformation"
framework: "Custom Agents"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/bigquery-cost-query-performance-auditor-2/"
---

# BigQuery Cost & Query Performance Auditor

Queries BigQuery INFORMATION_SCHEMA.JOBS_BY_PROJECT to identify top slot-consuming queries over 30 days. Surfaces optimization recommendations — partition pruning, clustering keys, redundant scans — with specific job IDs and estimated byte savings.

## Overview

Queries BigQuery INFORMATION_SCHEMA.JOBS_BY_PROJECT to identify top slot-consuming queries over 30 days. Surfaces optimization recommendations — partition pruning, clustering keys, redundant scans — with specific job IDs and estimated byte savings.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill bigquery-cost-query-performance-auditor-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill bigquery-cost-query-performance-auditor-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill bigquery-cost-query-performance-auditor-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill bigquery-cost-query-performance-auditor-2 -a codex
```

### OpenClaw

```bash
clawhub install bigquery-cost-query-performance-auditor-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/bigquery-cost-query-performance-auditor-2/
