---
name: "Elastic APM Transaction Anomaly Spotter"
slug: "elastic-apm-transaction-anomaly-spotter"
description: "Queries Elastic APM transaction data through the Elasticsearch REST API to surface latency anomalies and throughput drops. Uses the _search aggregation API with percentile and moving_avg pipelines."
github_stars: 1273
verification: "listed"
source: "https://github.com/elastic/apm-server"
author: "elastic"
category: "Monitoring & Alerts"
framework: "MCP"
tool_ecosystem:
  github_repo: "elastic/apm-server"
  github_stars: 1273
---

# Elastic APM Transaction Anomaly Spotter

Queries Elastic APM transaction data through the Elasticsearch REST API to surface latency anomalies and throughput drops. Uses the _search aggregation API with percentile and moving_avg pipelines.

## Installation

Use the upstream install or setup path that matches your environment:
- git clone git@github.com:[USER]/apm-server.git
- make
- make update
- make clean

Requirements and caveats from upstream:
- ### Building docker packages
- To customize image configuration, see [the docs](https://www.elastic.co/guide/en/apm/guide/current/running-on-docker.html).

Basic usage or getting-started notes:
- To get started with APM, see our [Quick start guide](https://www.elastic.co/guide/en/apm/guide/current/apm-quick-start.html).
- ## APM Server Development
- [Go][golang-download]

- Source: https://github.com/elastic/apm-server
- Extracted from upstream docs: https://raw.githubusercontent.com/elastic/apm-server/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/elastic-apm-transaction-anomaly-spotter/)
