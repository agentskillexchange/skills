---
title: "ElasticSearch Cluster Vitals Agent"
description: "Polls Elasticsearch _cluster/health, _nodes/stats, and _cat/shards APIs to detect node drops, unassigned shards, and JVM heap pressure. Forwards anomalies to Opsgenie Alert API for on-call routing."
slug: "elasticsearch-cluster-vitals-agent"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Claude Agents"
verification: "security_reviewed"
source: "https://github.com/elastic/elasticsearch"
tool_ecosystem:
  github_repo: "elastic/elasticsearch"
  github_stars: 76475
---

# ElasticSearch Cluster Vitals Agent

Polls Elasticsearch _cluster/health, _nodes/stats, and _cat/shards APIs to detect node drops, unassigned shards, and JVM heap pressure. Forwards anomalies to Opsgenie Alert API for on-call routing.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install elasticsearch-cluster-vitals-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Elasticsearch Cluster Vitals Agent continuously monitors the health of Elasticsearch clusters by polling critical diagnostic APIs. The _cluster/health endpoint provides overall cluster status, active shard counts, and pending task queues while _nodes/stats delivers per-node metrics including JVM heap utilization, garbage collection frequency, thread pool rejections, and file descriptor usage. Shard allocation is tracked via _cat/shards to identify unassigned or relocating shards that could indicate storage pressure or node failures. The agent implements intelligent alerting through Opsgenie Alert API with severity-based routing that distinguishes between degraded performance warnings and critical cluster failures requiring immediate intervention. JVM heap pressure analysis tracks old generation garbage collection patterns to predict OutOfMemoryError conditions before they crash nodes. Index-level monitoring identifies hot indices consuming disproportionate resources, suggesting ILM policy adjustments or shard rebalancing. Circuit breaker status is monitored to catch request-level memory pressure before it cascades into cluster instability. The agent maintains a rolling health history for trend analysis and capacity planning.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/elasticsearch-cluster-vitals-agent/)
