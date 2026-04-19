---
title: "Apache Kafka Stream Transformer"
description: "The Apache Kafka Stream Transformer provides real-time event processing capabilities using KafkaJS as the client library. It connects to Kafka clusters as a consumer group member, processes messages through configurable transformation pipelines, and produces enriched output to downstream topics. Core functionality includes consumer group management with kafka.consumer({ groupId }) , topic subscription with pattern matching, and manual offset management via consumer.commitOffsets() . The skill handles partition rebalancing events through the GROUP_JOIN and REBALANCING instrumentation events. Message transformation supports Avro schema deserialization via Schema Registry integration ( @kafkajs/confluent-schema-registry ), field mapping, filtering, and enrichment from external sources. Failed transformations are routed to configurable dead-letter queues with original message metadata preserved. The agent monitors consumer lag via admin client admin.fetchOffsets() and provides alerting when lag exceeds thresholds. Supports exactly-once semantics with transactional producers."
source: "https://github.com/apache/kafka"
verification: "security_reviewed"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "apache/kafka"
  github_stars: 32377
---

# Apache Kafka Stream Transformer

The Apache Kafka Stream Transformer provides real-time event processing capabilities using KafkaJS as the client library. It connects to Kafka clusters as a consumer group member, processes messages through configurable transformation pipelines, and produces enriched output to downstream topics. Core functionality includes consumer group management with kafka.consumer({ groupId }) , topic subscription with pattern matching, and manual offset management via consumer.commitOffsets() . The skill handles partition rebalancing events through the GROUP_JOIN and REBALANCING instrumentation events. Message transformation supports Avro schema deserialization via Schema Registry integration ( @kafkajs/confluent-schema-registry ), field mapping, filtering, and enrichment from external sources. Failed transformations are routed to configurable dead-letter queues with original message metadata preserved. The agent monitors consumer lag via admin client admin.fetchOffsets() and provides alerting when lag exceeds thresholds. Supports exactly-once semantics with transactional producers.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apache-kafka-stream-transformer-2/)
