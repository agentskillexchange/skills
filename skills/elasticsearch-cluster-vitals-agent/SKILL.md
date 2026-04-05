---
title: "ElasticSearch Cluster Vitals Agent"
description: "Polls Elasticsearch _cluster/health, _nodes/stats, and _cat/shards APIs to detect node drops, unassigned shards, and JVM heap pressure. Forwards anomalies to Opsgenie Alert API for on-call routing."
slug: "elasticsearch-cluster-vitals-agent"
verification: "security_reviewed"
source: "https://github.com/elastic/elasticsearch"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "elastic/elasticsearch"
  github_stars: 76426
---
# ElasticSearch Cluster Vitals Agent

Polls Elasticsearch _cluster/health, _nodes/stats, and _cat/shards APIs to detect node drops, unassigned shards, and JVM heap pressure. Forwards anomalies to Opsgenie Alert API for on-call routing.

## Installation

Choose the method that fits your setup:
1. Install from the Agent Skill Exchange website
2. Clone or download the upstream source repository
3. Install via npm if the project is published there
4. Use the tool's package manager or release binaries
5. Copy the skill files into your local skills directory manually

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/elasticsearch-cluster-vitals-agent/)
