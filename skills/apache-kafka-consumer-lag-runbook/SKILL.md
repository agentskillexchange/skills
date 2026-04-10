---
title: "Apache Kafka Consumer Lag Runbook"
description: "Diagnoses Kafka consumer group lag using the Kafka AdminClient API and JMX metrics exposed via the Confluent Metrics API. Identifies slow consumers, topic partition hotspots, and broker rebalance storms that contribute to lag growth. Provides a step-by-step runbook to tune fetch.min.bytes, max.poll.records, and partition count."
slug: "apache-kafka-consumer-lag-runbook"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/apache-kafka-consumer-lag-runbook/"
---

# Apache Kafka Consumer Lag Runbook

Diagnoses Kafka consumer group lag using the Kafka AdminClient API and JMX metrics exposed via the Confluent Metrics API. Identifies slow consumers, topic partition hotspots, and broker rebalance storms that contribute to lag growth. Provides a step-by-step runbook to tune fetch.min.bytes, max.poll.records, and partition count.

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
clawhub install apache-kafka-consumer-lag-runbook
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill connects to a Kafka cluster using the Apache Kafka AdminClient API (kafka-clients library) and queries consumer group offsets via the listConsumerGroupOffsets method. It cross-references committed offsets with latest partition offsets to calculate per-partition lag. JMX metrics are fetched from broker MBeans (kafka.server:type=FetcherLagMetrics) or, for Confluent Cloud, via the Confluent Metrics API REST endpoint. The skill identifies hotspot partitions by comparing lag growth rates across a rolling 10-minute window. Common root causes are diagnosed: slow deserialization, GC pauses, downstream database saturation, and rebalance loops triggered by session.timeout.ms misconfig. A step-by-step Markdown runbook is generated with exact configuration property changes and kafka-consumer-groups.sh commands for immediate lag reduction.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apache-kafka-consumer-lag-runbook/)
