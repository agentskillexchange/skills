---
name: Apache Kafka Consumer Lag Runbook
description: Diagnoses Kafka consumer group lag using the Kafka AdminClient API and
  JMX metrics exposed via the Confluent Metrics API. Identifies slow consumers, topic
  partition hotspots, and broker rebalance storms that contribute to lag growth. Provides
  a step-by-step runbook to tune fetch.min.bytes, max.poll.records, and partition
  count.
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

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apache-kafka-consumer-lag-runbook/)
