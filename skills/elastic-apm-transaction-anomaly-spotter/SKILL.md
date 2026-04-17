---
name: Elastic APM Transaction Anomaly Spotter
description: Queries Elastic APM transaction data through the Elasticsearch REST API
  to surface latency anomalies and throughput drops. Uses the _search aggregation
  API with percentile and moving_avg pipelines.
category: Monitoring & Alerts
framework: MCP
verification: security_reviewed
source: https://github.com/elastic/apm-server
tool_ecosystem:
  github_repo: elastic/apm-server
  github_stars: 1273
  tool: apm-server
---
# Elastic APM Transaction Anomaly Spotter
Queries Elastic APM transaction data through the Elasticsearch REST API to surface latency anomalies and throughput drops. Uses the _search aggregation API with percentile and moving_avg pipelines.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/elastic-apm-transaction-anomaly-spotter
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/elastic-apm-transaction-anomaly-spotter` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/elastic-apm-transaction-anomaly-spotter/)
