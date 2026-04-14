---
title: "Elastic APM Transaction Anomaly Spotter"
description: "Queries Elastic APM transaction data through the Elasticsearch REST API to surface latency anomalies and throughput drops. Uses the _search aggregation API with percentile and moving_avg pipelines."
verification: security_reviewed
source: "https://github.com/elastic/apm-server"
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/elastic-apm-transaction-anomaly-spotter/)
