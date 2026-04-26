---
title: "Apache Kafka Stream Transformer"
description: "Processes real-time event streams using KafkaJS consumer groups and transforms messages with configurable schemas. Handles partition rebalancing, offset commits, and dead-letter queue routing for failed transformations."
verification: "security_reviewed"
source: "https://github.com/apache/kafka"
category:
  - "Data Extraction & Transformation"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "apache/kafka"
  github_stars: 32377
---

# Apache Kafka Stream Transformer

The Apache Kafka Stream Transformer provides real-time event processing capabilities using KafkaJS as the client library. It connects to Kafka clusters as a consumer group member, processes messages through configurable transformation pipelines, and produces enriched output to downstream topics.

Core functionality includes consumer group management with kafka.consumer({ groupId }), topic subscription with pattern matching, and manual offset management via consumer.commitOffsets(). The skill handles partition rebalancing events through the GROUP_JOIN and REBALANCING instrumentation events.

Message transformation supports Avro schema deserialization via Schema Registry integration (@kafkajs/confluent-schema-registry), field mapping, filtering, and enrichment from external sources. Failed transformations are routed to configurable dead-letter queues with original message metadata preserved. The agent monitors consumer lag via admin client admin.fetchOffsets() and provides alerting when lag exceeds thresholds. Supports exactly-once semantics with transactional producers.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/apache-kafka-stream-transformer-2/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/apache-kafka-stream-transformer-2
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/apache-kafka-stream-transformer-2`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apache-kafka-stream-transformer-2/)
