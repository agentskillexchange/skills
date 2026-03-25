---
name: "Apache Kafka Stream Transformer"
description: "Processes real-time event streams using KafkaJS consumer groups and transforms messages with configurable schemas. Handles partition rebalancing, offset commits, and dead-letter queue routing for failed transformations."
category: "Data Extraction & Transformation"
framework: "Cursor"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/apache-kafka-stream-transformer-2/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "kafka"  # from ase_tool_match
  github_stars: 3987  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 2396148  # from ase_npm_downloads
  github_repo: "tulios/kafkajs"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: false  # from ase_tool_maintained
---

# Apache Kafka Stream Transformer

Processes real-time event streams using KafkaJS consumer groups and transforms messages with configurable schemas. Handles partition rebalancing, offset commits, and dead-letter queue routing for failed transformations.

## Overview

The Apache Kafka Stream Transformer provides real-time event processing capabilities using KafkaJS as the client library. It connects to Kafka clusters as a consumer group member, processes messages through configurable transformation pipelines, and produces enriched output to downstream topics.

Core functionality includes consumer group management with `kafka.consumer({ groupId })`, topic subscription with pattern matching, and manual offset management via `consumer.commitOffsets()`. The skill handles partition rebalancing events through the `GROUP_JOIN` and `REBALANCING` instrumentation events.

Message transformation supports Avro schema deserialization via Schema Registry integration (`@kafkajs/confluent-schema-registry`), field mapping, filtering, and enrichment from external sources. Failed transformations are routed to configurable dead-letter queues with original message metadata preserved. The agent monitors consumer lag via admin client `admin.fetchOffsets()` and provides alerting when lag exceeds thresholds. Supports exactly-once semantics with transactional producers.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill apache-kafka-stream-transformer-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill apache-kafka-stream-transformer-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill apache-kafka-stream-transformer-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill apache-kafka-stream-transformer-2 -a codex
```

### OpenClaw

```bash
clawhub install apache-kafka-stream-transformer-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/apache-kafka-stream-transformer-2/
