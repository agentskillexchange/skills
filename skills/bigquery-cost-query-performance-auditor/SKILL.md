---
name: BigQuery Cost & Query Performance Auditor
description: Connects to BigQuery INFORMATION_SCHEMA.JOBS_BY_PROJECT to identify the top slot-consuming and highest-billed queries over a rolling 30-day window. Surfaces optimization recommendations — partition pruning, clustering key usage, redundant full-table scans — with specific job IDs and estimated savings.
category: Data Extraction &amp; Transformation
framework: Any Agent
verification: listed
rating: 4.2
reviews: 48
source: https://agentskillexchange.com/skill/bigquery-cost-query-performance-auditor/
---

# BigQuery Cost & Query Performance Auditor

Connects to BigQuery INFORMATION_SCHEMA.JOBS_BY_PROJECT to identify the top slot-consuming and highest-billed queries over a rolling 30-day window. Surfaces optimization recommendations — partition pruning, clustering key usage, redundant full-table scans — with specific job IDs and estimated savings.

## Overview

Connects to BigQuery INFORMATION_SCHEMA.JOBS_BY_PROJECT to identify the top slot-consuming and highest-billed queries over a rolling 30-day window. Surfaces optimization recommendations — partition pruning, clustering key usage, redundant full-table scans — with specific job IDs and estimated savings.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill bigquery-cost-query-performance-auditor
```

### OpenClaw

```bash
clawhub install bigquery-cost-query-performance-auditor
```

### Claude Code

```bash
claude mcp add bigquery-cost-query-performance-auditor
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/bigquery-cost-query-performance-auditor/) for detailed installation instructions.

## Verification

- **Status**: listed
- **Category**: Data Extraction &amp; Transformation
- **Framework**: Any Agent
- **Rating**: 4.2/5 (48 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/bigquery-cost-query-performance-auditor/)
