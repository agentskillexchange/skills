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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apache-kafka-stream-transformer-2/)
