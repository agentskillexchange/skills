---
title: "ElasticSearch Cluster Vitals Agent"
description: "Polls Elasticsearch _cluster/health, _nodes/stats, and _cat/shards APIs to detect node drops, unassigned shards, and JVM heap pressure. Forwards anomalies to Opsgenie Alert API for on-call routing."
verification: security_reviewed
source: "https://github.com/elastic/elasticsearch"
category: ["Monitoring & Alerts"]
framework: ["Claude Agents"]
tool_ecosystem:
  github_repo: "elastic/elasticsearch"
  github_stars: 76426
---

# ElasticSearch Cluster Vitals Agent

Polls Elasticsearch _cluster/health, _nodes/stats, and _cat/shards APIs to detect node drops, unassigned shards, and JVM heap pressure. Forwards anomalies to Opsgenie Alert API for on-call routing.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI.
2. Add it through your agent or assistant skill manager.
3. Clone or copy this skill into your local skills directory.
4. Install with a package manager if the upstream project provides one.
5. Follow the upstream project documentation for manual setup.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/elasticsearch-cluster-vitals-agent/)
