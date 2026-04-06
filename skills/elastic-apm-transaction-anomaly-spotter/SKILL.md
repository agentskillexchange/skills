---
name: "elastic-apm-transaction-anomaly-spotter"
description: "Queries Elastic APM transaction data through the Elasticsearch REST API to surface latency anomalies and throughput drops. Uses the _search aggregation API with percentile and moving_avg pipelines."
category: "Monitoring &amp; Alerts"
framework: "MCP"
verification: "security_reviewed"
source: "https://github.com/elastic/apm-server"
tool_ecosystem:
  github_repo: "elastic/apm-server"
  github_stars: 1273
---

# Elastic APM Transaction Anomaly Spotter

Queries Elastic APM transaction data through the Elasticsearch REST API to surface latency anomalies and throughput drops. Uses the _search aggregation API with percentile and moving_avg pipelines.

## Installation

You can install this skill using one of these common methods:

1. **ClawHub** — install from the marketplace if available.
2. **Git clone** — clone the skill folder into your local skills directory.
3. **Download ZIP** — download and extract the skill files manually.
4. **Copy files** — copy the skill directory into your agent skills path.
5. **Package manager / upstream installer** — use the original project installer if the source provides one.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/elastic-apm-transaction-anomaly-spotter/)
