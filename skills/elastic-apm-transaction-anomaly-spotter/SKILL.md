---
title: "Elastic APM Transaction Anomaly Spotter"
description: "The Elastic APM Transaction Anomaly Spotter connects to your Elasticsearch cluster and analyzes APM transaction data to identify performance regressions and throughput anomalies. It constructs Elasticsearch queries using the _search API with date_histogram aggregations, percentile_ranks, and moving_avg pipeline aggregations to establish service-level baselines. The skill monitors p95 and p99 latency across service transactions, comparing current windows against historical patterns. When latency exceeds dynamic thresholds or throughput drops below expected levels, it generates detailed anomaly reports including the affected service name, transaction type, environment, and comparison metrics. It integrates with the Elastic Alerting framework and can push notifications to Opsgenie or Microsoft Teams via their respective webhook APIs. The skill supports APM agent filtering by service.name and transaction.type fields, and can drill into span-level data to pinpoint slow dependencies using nested aggregations on span.destination.service.resource."
source: "https://github.com/elastic/apm-server"
verification: "security_reviewed"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "elastic/apm-server"
  github_stars: 1273
---

# Elastic APM Transaction Anomaly Spotter

The Elastic APM Transaction Anomaly Spotter connects to your Elasticsearch cluster and analyzes APM transaction data to identify performance regressions and throughput anomalies. It constructs Elasticsearch queries using the _search API with date_histogram aggregations, percentile_ranks, and moving_avg pipeline aggregations to establish service-level baselines. The skill monitors p95 and p99 latency across service transactions, comparing current windows against historical patterns. When latency exceeds dynamic thresholds or throughput drops below expected levels, it generates detailed anomaly reports including the affected service name, transaction type, environment, and comparison metrics. It integrates with the Elastic Alerting framework and can push notifications to Opsgenie or Microsoft Teams via their respective webhook APIs. The skill supports APM agent filtering by service.name and transaction.type fields, and can drill into span-level data to pinpoint slow dependencies using nested aggregations on span.destination.service.resource.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/elastic-apm-transaction-anomaly-spotter/)
