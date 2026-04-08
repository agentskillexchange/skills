---
title: "Elastic APM Transaction Anomaly Spotter"
slug: "elastic-apm-transaction-anomaly-spotter"
verification: "security_reviewed"
description: "Queries Elastic APM transaction data through the Elasticsearch REST API to surface latency anomalies and throughput drops. Uses the _search aggregation API with percentile and moving_avg pipelines."
category:
  - "Monitoring &amp; Alerts"
framework:
  - "MCP"
source: "https://github.com/elastic/apm-server"
tool_ecosystem:
  github_repo: "elastic/apm-server"
  github_stars: 1273
---

# Elastic APM Transaction Anomaly Spotter

Queries Elastic APM transaction data through the Elasticsearch REST API to surface latency anomalies and throughput drops. Uses the _search aggregation API with percentile and moving_avg pipelines.

## Installation

Choose the setup path that fits your environment:

1. Clone or download this skill into your local skills workspace.
2. Install it with ClawHub if it is available there.
3. Copy the folder into your OpenClaw or AgentSkills directory manually.
4. Add it as a git submodule if you manage skills as pinned dependencies.
5. Vendor it directly into a project repo when you need a fixed internal copy.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/elastic-apm-transaction-anomaly-spotter/)
