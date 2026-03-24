---
name: "ElasticSearch Cluster Vitals Agent"
description: "Polls Elasticsearch _cluster/health, _nodes/stats, and _cat/shards APIs to detect node drops, unassigned shards, and JVM heap pressure. Forwards anomalies to Opsgenie Alert API for on-call routing."
category: "Monitoring & Alerts"
framework: "Claude Agents"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/elasticsearch-cluster-vitals-agent/"
---

# ElasticSearch Cluster Vitals Agent

Polls Elasticsearch _cluster/health, _nodes/stats, and _cat/shards APIs to detect node drops, unassigned shards, and JVM heap pressure. Forwards anomalies to Opsgenie Alert API for on-call routing.

## Overview

The Elasticsearch Cluster Vitals Agent continuously monitors the health of Elasticsearch clusters by polling critical diagnostic APIs. The _cluster/health endpoint provides overall cluster status, active shard counts, and pending task queues while _nodes/stats delivers per-node metrics including JVM heap utilization, garbage collection frequency, thread pool rejections, and file descriptor usage. Shard allocation is tracked via _cat/shards to identify unassigned or relocating shards that could indicate storage pressure or node failures. The agent implements intelligent alerting through Opsgenie Alert API with severity-based routing that distinguishes between degraded performance warnings and critical cluster failures requiring immediate intervention. JVM heap pressure analysis tracks old generation garbage collection patterns to predict OutOfMemoryError conditions before they crash nodes. Index-level monitoring identifies hot indices consuming disproportionate resources, suggesting ILM policy adjustments or shard rebalancing. Circuit breaker status is monitored to catch request-level memory pressure before it cascades into cluster instability. The agent maintains a rolling health history for trend analysis and capacity planning.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill elasticsearch-cluster-vitals-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill elasticsearch-cluster-vitals-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill elasticsearch-cluster-vitals-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill elasticsearch-cluster-vitals-agent -a codex
```

### OpenClaw

```bash
clawhub install elasticsearch-cluster-vitals-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/elasticsearch-cluster-vitals-agent/
