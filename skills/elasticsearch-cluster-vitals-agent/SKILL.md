---
name: "ElasticSearch Cluster Vitals Agent"
category: "Monitoring & Alerts"
verification: "security_reviewed"
source: "https://github.com/elastic/elasticsearch"
tool_ecosystem:
  github_repo: "elastic/elasticsearch"
  github_stars: 76426
---

# ElasticSearch Cluster Vitals Agent

Polls Elasticsearch _cluster/health, _nodes/stats, and _cat/shards APIs to detect node drops, unassigned shards, and JVM heap pressure. Forwards anomalies to Opsgenie Alert API for on-call routing.

## Installation

Install this skill using one of the following methods:

```bash
# ClawHub CLI
clawhub install elasticsearch-cluster-vitals-agent

# OpenClaw CLI
openclaw skills install elasticsearch-cluster-vitals-agent

# Chat command
/skill install elasticsearch-cluster-vitals-agent

# Direct download
curl -L https://agentskillexchange.com/skills/elasticsearch-cluster-vitals-agent/download -o elasticsearch-cluster-vitals-agent.zip

# Git clone this repo and copy the skill folder
cp -r skills/elasticsearch-cluster-vitals-agent ~/.openclaw/workspace/skills/
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/elasticsearch-cluster-vitals-agent/)
