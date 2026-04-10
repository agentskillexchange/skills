---
title: "Elastic APM Transaction Anomaly Spotter"
description: "Queries Elastic APM transaction data through the Elasticsearch REST API to surface latency anomalies and throughput drops. Uses the _search aggregation API with percentile and moving_avg pipelines."
slug: "elastic-apm-transaction-anomaly-spotter"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://github.com/elastic/apm-server"
tool_ecosystem:
  github_repo: "elastic/apm-server"
  github_stars: 1273
---

# Elastic APM Transaction Anomaly Spotter

Queries Elastic APM transaction data through the Elasticsearch REST API to surface latency anomalies and throughput drops. Uses the _search aggregation API with percentile and moving_avg pipelines.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install elastic-apm-transaction-anomaly-spotter
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Elastic APM Transaction Anomaly Spotter connects to your Elasticsearch cluster and analyzes APM transaction data to identify performance regressions and throughput anomalies. It constructs Elasticsearch queries using the _search API with date_histogram aggregations, percentile_ranks, and moving_avg pipeline aggregations to establish service-level baselines. The skill monitors p95 and p99 latency across service transactions, comparing current windows against historical patterns. When latency exceeds dynamic thresholds or throughput drops below expected levels, it generates detailed anomaly reports including the affected service name, transaction type, environment, and comparison metrics. It integrates with the Elastic Alerting framework and can push notifications to Opsgenie or Microsoft Teams via their respective webhook APIs. The skill supports APM agent filtering by service.name and transaction.type fields, and can drill into span-level data to pinpoint slow dependencies using nested aggregations on span.destination.service.resource.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/elastic-apm-transaction-anomaly-spotter/)
