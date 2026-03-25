---
name: "Elastic APM Transaction Anomaly Spotter"
description: "Queries Elastic APM transaction data through the Elasticsearch REST API to surface latency anomalies and throughput drops. Uses the _search aggregation API with percentile and moving_avg pipelines."
category: "40"
framework: "32"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/elastic-apm-transaction-anomaly-spotter/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "elasticsearch"  # from ase_tool_match
  github_stars: 76387  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 1893773  # from ase_npm_downloads
  github_repo: "elastic/elasticsearch"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Elastic APM Transaction Anomaly Spotter

Queries Elastic APM transaction data through the Elasticsearch REST API to surface latency anomalies and throughput drops. Uses the _search aggregation API with percentile and moving_avg pipelines.

## Overview

The Elastic APM Transaction Anomaly Spotter connects to your Elasticsearch cluster and analyzes APM transaction data to identify performance regressions and throughput anomalies. It constructs Elasticsearch queries using the _search API with date_histogram aggregations, percentile_ranks, and moving_avg pipeline aggregations to establish service-level baselines. The skill monitors p95 and p99 latency across service transactions, comparing current windows against historical patterns. When latency exceeds dynamic thresholds or throughput drops below expected levels, it generates detailed anomaly reports including the affected service name, transaction type, environment, and comparison metrics. It integrates with the Elastic Alerting framework and can push notifications to Opsgenie or Microsoft Teams via their respective webhook APIs. The skill supports APM agent filtering by service.name and transaction.type fields, and can drill into span-level data to pinpoint slow dependencies using nested aggregations on span.destination.service.resource.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill elastic-apm-transaction-anomaly-spotter
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill elastic-apm-transaction-anomaly-spotter -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill elastic-apm-transaction-anomaly-spotter -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill elastic-apm-transaction-anomaly-spotter -a codex
```

### OpenClaw

```bash
clawhub install elastic-apm-transaction-anomaly-spotter
```

## Source

- Marketplace: https://agentskillexchange.com/skills/elastic-apm-transaction-anomaly-spotter/
