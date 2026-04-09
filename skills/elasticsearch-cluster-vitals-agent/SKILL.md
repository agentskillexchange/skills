---
title: "ElasticSearch Cluster Vitals Agent"
description: "Polls Elasticsearch _cluster/health, _nodes/stats, and _cat/shards APIs to detect node drops, unassigned shards, and JVM heap pressure. Forwards anomalies to Opsgenie Alert API for on-call routing."
slug: "elasticsearch-cluster-vitals-agent"
verification: "security_reviewed"
source: "https://github.com/elastic/elasticsearch"
category:
  - "Monitoring & Alerts"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "elastic/elasticsearch"
  github_stars: 76475
---
# ElasticSearch Cluster Vitals Agent

Polls Elasticsearch _cluster/health, _nodes/stats, and _cat/shards APIs to detect node drops, unassigned shards, and JVM heap pressure. Forwards anomalies to Opsgenie Alert API for on-call routing.

## Installation

Choose the method that fits your setup:

1. Install from Agent Skill Exchange
2. Add as a local skill folder
3. Install from a Git repository
4. Install via package manager if supported
5. Copy the skill into your OpenClaw skills directory

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/elasticsearch-cluster-vitals-agent/)
