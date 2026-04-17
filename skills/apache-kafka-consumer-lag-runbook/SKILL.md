---
title: "Apache Kafka Consumer Lag Runbook"
description: "This skill connects to a Kafka cluster using the Apache Kafka AdminClient API (kafka-clients library) and queries consumer group offsets via the listConsumerGroupOffsets method. It cross-references committed offsets with latest partition offsets to calculate per-partition lag. JMX metrics are fetched from broker MBeans (kafka.server:type=FetcherLagMetrics) or, for Confluent Cloud, via the Confluent Metrics API REST endpoint. The skill identifies hotspot partitions by comparing lag growth rates across a rolling 10-minute window. Common root causes are diagnosed: slow deserialization, GC pauses, downstream database saturation, and rebalance loops triggered by session.timeout.ms misconfig. A step-by-step Markdown runbook is generated with exact configuration property changes and kafka-consumer-groups.sh commands for immediate lag reduction."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/apache-kafka-consumer-lag-runbook/"
framework:
  - "Cursor"
---

# Apache Kafka Consumer Lag Runbook

This skill connects to a Kafka cluster using the Apache Kafka AdminClient API (kafka-clients library) and queries consumer group offsets via the listConsumerGroupOffsets method. It cross-references committed offsets with latest partition offsets to calculate per-partition lag. JMX metrics are fetched from broker MBeans (kafka.server:type=FetcherLagMetrics) or, for Confluent Cloud, via the Confluent Metrics API REST endpoint. The skill identifies hotspot partitions by comparing lag growth rates across a rolling 10-minute window. Common root causes are diagnosed: slow deserialization, GC pauses, downstream database saturation, and rebalance loops triggered by session.timeout.ms misconfig. A step-by-step Markdown runbook is generated with exact configuration property changes and kafka-consumer-groups.sh commands for immediate lag reduction.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/apache-kafka-consumer-lag-runbook
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/apache-kafka-consumer-lag-runbook` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apache-kafka-consumer-lag-runbook/)
