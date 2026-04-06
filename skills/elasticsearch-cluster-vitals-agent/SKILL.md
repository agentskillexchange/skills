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

Choose the installation path that fits your setup:

1. Install from Agent Skill Exchange in the OpenClaw UI.
2. Copy the skill folder into your local skills directory.
3. Add it to your shared workspace skills collection.
4. Install it through a compatible agent skill manager.
5. Clone or download the upstream source and wire it into your agent runtime.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/elasticsearch-cluster-vitals-agent/)
