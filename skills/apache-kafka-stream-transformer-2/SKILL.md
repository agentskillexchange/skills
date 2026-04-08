---
title: Apache Kafka Stream Transformer
description: The Apache Kafka Stream Transformer provides real-time event processing
  capabilities using KafkaJS as the client library. It connects to Kafka clusters
  as a consumer group member, processes messages through configurable transformation
  pipelines, and produces enriched output to downstream topics. Core functionality
  includes consumer group management with kafka.consumer({ groupId }) , topic subscription
  with pattern matching, and manual offset management via consumer.commitOffsets()
  . The skill handles partition rebalancing events through the GROUP_JOIN and REBALANCING
  instrumentation events. Message transformation supports Avro schema deserialization
  via Schema Registry integration ( @kafkajs/confluent-schema-registry ), field mapping,
  filtering, and enrichment from external sources. Failed transformations are routed
  to configurable dead-letter queues with original message metadata preserved. The
  agent monitors consumer lag via admin client admin.fetchOffsets() and provides alerting
  when lag exceeds thresholds. Supports exactly-once semantics with transactional
  producers.
verification: security_reviewed
source: https://agentskillexchange.com/skills/apache-kafka-stream-transformer-2/
category:
- Data Extraction &amp; Transformation
framework:
- Cursor
---

# Apache Kafka Stream Transformer

The Apache Kafka Stream Transformer provides real-time event processing capabilities using KafkaJS as the client library. It connects to Kafka clusters as a consumer group member, processes messages through configurable transformation pipelines, and produces enriched output to downstream topics. Core functionality includes consumer group management with kafka.consumer({ groupId }) , topic subscription with pattern matching, and manual offset management via consumer.commitOffsets() . The skill handles partition rebalancing events through the GROUP_JOIN and REBALANCING instrumentation events. Message transformation supports Avro schema deserialization via Schema Registry integration ( @kafkajs/confluent-schema-registry ), field mapping, filtering, and enrichment from external sources. Failed transformations are routed to configurable dead-letter queues with original message metadata preserved. The agent monitors consumer lag via admin client admin.fetchOffsets() and provides alerting when lag exceeds thresholds. Supports exactly-once semantics with transactional producers.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apache-kafka-stream-transformer-2/)
