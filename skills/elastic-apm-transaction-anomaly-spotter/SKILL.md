---
title: Elastic APM Transaction Anomaly Spotter
description: The Elastic APM Transaction Anomaly Spotter connects to your Elasticsearch
  cluster and analyzes APM transaction data to identify performance regressions and
  throughput anomalies. It constructs Elasticsearch queries using the _search API
  with date_histogram aggregations, percentile_ranks, and moving_avg pipeline aggregations
  to establish service-level baselines. The skill monitors p95 and p99 latency across
  service transactions, comparing current windows against historical patterns. When
  latency exceeds dynamic thresholds or throughput drops below expected levels, it
  generates detailed anomaly reports including the affected service name, transaction
  type, environment, and comparison metrics. It integrates with the Elastic Alerting
  framework and can push notifications to Opsgenie or Microsoft Teams via their respective
  webhook APIs. The skill supports APM agent filtering by service.name and transaction.type
  fields, and can drill into span-level data to pinpoint slow dependencies using nested
  aggregations on span.destination.service.resource.
verification: security_reviewed
source: https://github.com/elastic/apm-server
category:
- Monitoring &amp; Alerts
framework:
- MCP
tool_ecosystem:
  github_repo: elastic/apm-server
  github_stars: 1273
---

# Elastic APM Transaction Anomaly Spotter

The Elastic APM Transaction Anomaly Spotter connects to your Elasticsearch cluster and analyzes APM transaction data to identify performance regressions and throughput anomalies. It constructs Elasticsearch queries using the _search API with date_histogram aggregations, percentile_ranks, and moving_avg pipeline aggregations to establish service-level baselines. The skill monitors p95 and p99 latency across service transactions, comparing current windows against historical patterns. When latency exceeds dynamic thresholds or throughput drops below expected levels, it generates detailed anomaly reports including the affected service name, transaction type, environment, and comparison metrics. It integrates with the Elastic Alerting framework and can push notifications to Opsgenie or Microsoft Teams via their respective webhook APIs. The skill supports APM agent filtering by service.name and transaction.type fields, and can drill into span-level data to pinpoint slow dependencies using nested aggregations on span.destination.service.resource.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/elastic-apm-transaction-anomaly-spotter/)
