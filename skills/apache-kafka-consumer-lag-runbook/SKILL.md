---
title: Apache Kafka Consumer Lag Runbook
description: 'This skill connects to a Kafka cluster using the Apache Kafka AdminClient
  API (kafka-clients library) and queries consumer group offsets via the listConsumerGroupOffsets
  method. It cross-references committed offsets with latest partition offsets to calculate
  per-partition lag. JMX metrics are fetched from broker MBeans (kafka.server:type=FetcherLagMetrics)
  or, for Confluent Cloud, via the Confluent Metrics API REST endpoint. The skill
  identifies hotspot partitions by comparing lag growth rates across a rolling 10-minute
  window. Common root causes are diagnosed: slow deserialization, GC pauses, downstream
  database saturation, and rebalance loops triggered by session.timeout.ms misconfig.
  A step-by-step Markdown runbook is generated with exact configuration property changes
  and kafka-consumer-groups.sh commands for immediate lag reduction.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/apache-kafka-consumer-lag-runbook/
category:
- Runbooks &amp; Diagnostics
framework:
- Cursor
---

# Apache Kafka Consumer Lag Runbook

This skill connects to a Kafka cluster using the Apache Kafka AdminClient API (kafka-clients library) and queries consumer group offsets via the listConsumerGroupOffsets method. It cross-references committed offsets with latest partition offsets to calculate per-partition lag. JMX metrics are fetched from broker MBeans (kafka.server:type=FetcherLagMetrics) or, for Confluent Cloud, via the Confluent Metrics API REST endpoint. The skill identifies hotspot partitions by comparing lag growth rates across a rolling 10-minute window. Common root causes are diagnosed: slow deserialization, GC pauses, downstream database saturation, and rebalance loops triggered by session.timeout.ms misconfig. A step-by-step Markdown runbook is generated with exact configuration property changes and kafka-consumer-groups.sh commands for immediate lag reduction.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apache-kafka-consumer-lag-runbook/)
