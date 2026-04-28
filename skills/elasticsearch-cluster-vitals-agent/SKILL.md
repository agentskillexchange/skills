---
title: ElasticSearch Cluster Vitals Agent
description: Polls Elasticsearch _cluster/health, _nodes/stats, and _cat/shards APIs
  to detect node drops, unassigned shards, and JVM heap pressure. Forwards anomalies
  to Opsgenie Alert API for on-call routing.
verification: security_reviewed
source: https://github.com/elastic/elasticsearch
category:
- Monitoring & Alerts
framework:
- Claude Agents
tool_ecosystem:
  github_repo: elastic/elasticsearch
  github_stars: 76475
---

# ElasticSearch Cluster Vitals Agent

Polls Elasticsearch _cluster/health, _nodes/stats, and _cat/shards APIs to detect node drops, unassigned shards, and JVM heap pressure. Forwards anomalies to Opsgenie Alert API for on-call routing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/elasticsearch-cluster-vitals-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/elasticsearch-cluster-vitals-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/elasticsearch-cluster-vitals-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/elasticsearch-cluster-vitals-agent/)
