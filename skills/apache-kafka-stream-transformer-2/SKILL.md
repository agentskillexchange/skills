---
name: Apache Kafka Stream Transformer
description: Processes real-time event streams using KafkaJS consumer groups and transforms
  messages with configurable schemas. Handles partition rebalancing, offset commits,
  and dead-letter queue routing for failed transformations.
verification: security_reviewed
source: https://agentskillexchange.com/skills/apache-kafka-stream-transformer-2/
category:
- Data Extraction &amp; Transformation
framework:
- Cursor
---
# Apache Kafka Stream Transformer

The Apache Kafka Stream Transformer provides real-time event processing capabilities using KafkaJS as the client library. It connects to Kafka clusters as a consumer group member, processes messages through configurable transformation pipelines, and produces enriched output to downstream topics.
Core functionality includes consumer group management with kafka.consumer({ groupId }), topic subscription with pattern matching, and manual offset management via consumer.commitOffsets(). The skill handles partition rebalancing events through the GROUP_JOIN and REBALANCING instrumentation events.
Message transformation supports Avro schema deserialization via Schema Registry integration (@kafkajs/confluent-schema-registry), field mapping, filtering, and enrichment from external sources. Failed transformations are routed to configurable dead-letter queues with original message metadata preserved. The agent monitors consumer lag via admin client admin.fetchOffsets() and provides alerting when lag exceeds thresholds. Supports exactly-once semantics with transactional producers.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apache-kafka-stream-transformer-2/)
