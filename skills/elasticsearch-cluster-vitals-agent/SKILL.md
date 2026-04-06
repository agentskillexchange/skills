---
title: "ElasticSearch Cluster Vitals Agent"
slug: "elasticsearch-cluster-vitals-agent"
description: "Polls Elasticsearch _cluster/health, _nodes/stats, and _cat/shards APIs to detect node drops, unassigned shards, and JVM heap pressure. Forwards anomalies to Opsgenie Alert API for on-call routing."
verification: "security_reviewed"
source: "https://github.com/elastic/elasticsearch"
category: "Monitoring &amp; Alerts"
framework: "Claude Agents"
tool_ecosystem:
  github_repo: "elastic/elasticsearch"
  github_stars: 76426
---

# ElasticSearch Cluster Vitals Agent

Polls Elasticsearch _cluster/health, _nodes/stats, and _cat/shards APIs to detect node drops, unassigned shards, and JVM heap pressure. Forwards anomalies to Opsgenie Alert API for on-call routing.

## Installation

Choose whichever method fits your setup:

1. Browse and install from Agent Skill Exchange.
2. Clone or download the upstream project manually.
3. Use the project package manager or installer if available.
4. Copy the skill into your local skills directory.
5. Follow the upstream documentation for environment-specific setup.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/elasticsearch-cluster-vitals-agent/)
