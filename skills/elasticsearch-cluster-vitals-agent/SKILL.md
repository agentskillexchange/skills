---
title: "ElasticSearch Cluster Vitals Agent"
slug: "elasticsearch-cluster-vitals-agent"
description: "Polls Elasticsearch _cluster/health, _nodes/stats, and _cat/shards APIs to detect node drops, unassigned shards, and JVM heap pressure. Forwards anomalies to Opsgenie Alert API for on-call routing."
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Claude Agents"
verification: "security_reviewed"
source: "https://github.com/elastic/elasticsearch"
tool_ecosystem:
  github_repo: "elastic/elasticsearch"
  github_stars: 76426
---

# ElasticSearch Cluster Vitals Agent

Polls Elasticsearch _cluster/health, _nodes/stats, and _cat/shards APIs to detect node drops, unassigned shards, and JVM heap pressure. Forwards anomalies to Opsgenie Alert API for on-call routing.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange catalog in your compatible client.
2. Clone or download this repository and copy the skill folder into your local skills directory.
3. Add it as a git submodule inside your skills collection.
4. Use a package or automation workflow that syncs skills from this repository.
5. Install directly from the original upstream project if you prefer to track source releases.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/elasticsearch-cluster-vitals-agent/)
