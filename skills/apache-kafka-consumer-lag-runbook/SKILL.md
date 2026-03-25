---
name: "Apache Kafka Consumer Lag Runbook"
description: "Diagnoses Kafka consumer group lag using the Kafka AdminClient API and JMX metrics exposed via the Confluent Metrics API. Identifies slow consumers, topic partition hotspots, and broker rebalance storms that contribute to lag growth. Provides a step-by-step runbook to tune fetch.min.bytes, max.poll.records, and partition count."
category: "Runbooks & Diagnostics"
framework: "Cursor"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/apache-kafka-consumer-lag-runbook/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "kafka"  # from ase_tool_match
  github_stars: 3987  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 2396148  # from ase_npm_downloads
  github_repo: "tulios/kafkajs"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: false  # from ase_tool_maintained
---

# Apache Kafka Consumer Lag Runbook

Diagnoses Kafka consumer group lag using the Kafka AdminClient API and JMX metrics exposed via the Confluent Metrics API. Identifies slow consumers, topic partition hotspots, and broker rebalance storms that contribute to lag growth. Provides a step-by-step runbook to tune fetch.min.bytes, max.poll.records, and partition count.

## Overview

This skill connects to a Kafka cluster using the Apache Kafka AdminClient API (kafka-clients library) and queries consumer group offsets via the listConsumerGroupOffsets method. It cross-references committed offsets with latest partition offsets to calculate per-partition lag. JMX metrics are fetched from broker MBeans (kafka.server:type=FetcherLagMetrics) or, for Confluent Cloud, via the Confluent Metrics API REST endpoint. The skill identifies hotspot partitions by comparing lag growth rates across a rolling 10-minute window. Common root causes are diagnosed: slow deserialization, GC pauses, downstream database saturation, and rebalance loops triggered by session.timeout.ms misconfig. A step-by-step Markdown runbook is generated with exact configuration property changes and kafka-consumer-groups.sh commands for immediate lag reduction.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill apache-kafka-consumer-lag-runbook
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill apache-kafka-consumer-lag-runbook -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill apache-kafka-consumer-lag-runbook -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill apache-kafka-consumer-lag-runbook -a codex
```

### OpenClaw

```bash
clawhub install apache-kafka-consumer-lag-runbook
```

## Source

- Marketplace: https://agentskillexchange.com/skills/apache-kafka-consumer-lag-runbook/
