---
title: "Apache Kafka Stream Transformer"
description: "Processes real-time event streams using KafkaJS consumer groups and transforms messages with configurable schemas. Handles partition rebalancing, offset commits, and dead-letter queue routing for failed transformations."
slug: "apache-kafka-stream-transformer-2"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/apache-kafka-stream-transformer-2/"
listed: true
---

# Apache Kafka Stream Transformer

Processes real-time event streams using KafkaJS consumer groups and transforms messages with configurable schemas. Handles partition rebalancing, offset commits, and dead-letter queue routing for failed transformations.

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
clawhub install apache-kafka-stream-transformer-2
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Apache Kafka Stream Transformer provides real-time event processing capabilities using KafkaJS as the client library. It connects to Kafka clusters as a consumer group member, processes messages through configurable transformation pipelines, and produces enriched output to downstream topics.
Core functionality includes consumer group management with kafka.consumer({ groupId }), topic subscription with pattern matching, and manual offset management via consumer.commitOffsets(). The skill handles partition rebalancing events through the GROUP_JOIN and REBALANCING instrumentation events.
Message transformation supports Avro schema deserialization via Schema Registry integration (@kafkajs/confluent-schema-registry), field mapping, filtering, and enrichment from external sources. Failed transformations are routed to configurable dead-letter queues with original message metadata preserved. The agent monitors consumer lag via admin client admin.fetchOffsets() and provides alerting when lag exceeds thresholds. Supports exactly-once semantics with transactional producers.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apache-kafka-stream-transformer-2/)
