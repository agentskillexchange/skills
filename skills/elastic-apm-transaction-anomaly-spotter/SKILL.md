---
name: "Elastic APM Transaction Anomaly Spotter"
category: "Monitoring & Alerts"
verification: "security_reviewed"
source: "https://github.com/elastic/apm-server"
tool_ecosystem:
  github_repo: "elastic/apm-server"
  github_stars: 1273
---

# Elastic APM Transaction Anomaly Spotter

Queries Elastic APM transaction data through the Elasticsearch REST API to surface latency anomalies and throughput drops. Uses the _search aggregation API with percentile and moving_avg pipelines.

## Installation

Install this skill using one of the following methods:

```bash
# ClawHub CLI
clawhub install elastic-apm-transaction-anomaly-spotter

# OpenClaw CLI
openclaw skills install elastic-apm-transaction-anomaly-spotter

# Chat command
/skill install elastic-apm-transaction-anomaly-spotter

# Direct download
curl -L https://agentskillexchange.com/skills/elastic-apm-transaction-anomaly-spotter/download -o elastic-apm-transaction-anomaly-spotter.zip

# Git clone this repo and copy the skill folder
cp -r skills/elastic-apm-transaction-anomaly-spotter ~/.openclaw/workspace/skills/
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/elastic-apm-transaction-anomaly-spotter/)
