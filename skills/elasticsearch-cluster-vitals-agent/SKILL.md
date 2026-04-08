---
title: ElasticSearch Cluster Vitals Agent
description: The Elasticsearch Cluster Vitals Agent continuously monitors the health
  of Elasticsearch clusters by polling critical diagnostic APIs. The _cluster/health
  endpoint provides overall cluster status, active shard counts, and pending task
  queues while _nodes/stats delivers per-node metrics including JVM heap utilization,
  garbage collection frequency, thread pool rejections, and file descriptor usage.
  Shard allocation is tracked via _cat/shards to identify unassigned or relocating
  shards that could indicate storage pressure or node failures. The agent implements
  intelligent alerting through Opsgenie Alert API with severity-based routing that
  distinguishes between degraded performance warnings and critical cluster failures
  requiring immediate intervention. JVM heap pressure analysis tracks old generation
  garbage collection patterns to predict OutOfMemoryError conditions before they crash
  nodes. Index-level monitoring identifies hot indices consuming disproportionate
  resources, suggesting ILM policy adjustments or shard rebalancing. Circuit breaker
  status is monitored to catch request-level memory pressure before it cascades into
  cluster instability. The agent maintains a rolling health history for trend analysis
  and capacity planning.
verification: security_reviewed
source: https://github.com/elastic/elasticsearch
category:
- Monitoring &amp; Alerts
framework:
- Claude Agents
tool_ecosystem:
  github_repo: elastic/elasticsearch
  github_stars: 76426
---

# ElasticSearch Cluster Vitals Agent

The Elasticsearch Cluster Vitals Agent continuously monitors the health of Elasticsearch clusters by polling critical diagnostic APIs. The _cluster/health endpoint provides overall cluster status, active shard counts, and pending task queues while _nodes/stats delivers per-node metrics including JVM heap utilization, garbage collection frequency, thread pool rejections, and file descriptor usage. Shard allocation is tracked via _cat/shards to identify unassigned or relocating shards that could indicate storage pressure or node failures. The agent implements intelligent alerting through Opsgenie Alert API with severity-based routing that distinguishes between degraded performance warnings and critical cluster failures requiring immediate intervention. JVM heap pressure analysis tracks old generation garbage collection patterns to predict OutOfMemoryError conditions before they crash nodes. Index-level monitoring identifies hot indices consuming disproportionate resources, suggesting ILM policy adjustments or shard rebalancing. Circuit breaker status is monitored to catch request-level memory pressure before it cascades into cluster instability. The agent maintains a rolling health history for trend analysis and capacity planning.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/elasticsearch-cluster-vitals-agent/)
