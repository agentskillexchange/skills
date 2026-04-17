---
name: ElasticSearch Cluster Vitals Agent
description: Polls Elasticsearch _cluster/health, _nodes/stats, and _cat/shards APIs
  to detect node drops, unassigned shards, and JVM heap pressure. Forwards anomalies
  to Opsgenie Alert API for on-call routing.
category: Monitoring & Alerts
framework: Claude Agents
verification: security_reviewed
source: https://github.com/elastic/elasticsearch
tool_ecosystem:
  github_repo: elastic/elasticsearch
  github_stars: 76475
  tool: elasticsearch
---
# ElasticSearch Cluster Vitals Agent
Polls Elasticsearch _cluster/health, _nodes/stats, and _cat/shards APIs to detect node drops, unassigned shards, and JVM heap pressure. Forwards anomalies to Opsgenie Alert API for on-call routing.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/elasticsearch-cluster-vitals-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/elasticsearch-cluster-vitals-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/elasticsearch-cluster-vitals-agent/)
