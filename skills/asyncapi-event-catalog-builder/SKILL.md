---
title: "AsyncAPI Event Catalog Builder"
description: "Generates event-driven architecture documentation from AsyncAPI 3.0 specifications. Uses the AsyncAPI parser-js library to extract channels, message schemas, and server bindings for Kafka and RabbitMQ."
slug: "asyncapi-event-catalog-builder"
category:
  - "Library &amp; API Reference"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/asyncapi-event-catalog-builder/"
---

# AsyncAPI Event Catalog Builder

Generates event-driven architecture documentation from AsyncAPI 3.0 specifications. Uses the AsyncAPI parser-js library to extract channels, message schemas, and server bindings for Kafka and RabbitMQ.

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
clawhub install asyncapi-event-catalog-builder
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The AsyncAPI Event Catalog Builder parses AsyncAPI 3.0 specification files to generate comprehensive event-driven architecture documentation. Using the official @asyncapi/parser library, it extracts channel definitions, message payload schemas (JSON Schema and Avro), server bindings, and operation traits. The skill generates catalog pages for each event type showing producers, consumers, schema evolution history, and payload examples. Kafka-specific bindings are resolved to show topic configurations, partition key strategies, and consumer group assignments. RabbitMQ bindings map exchanges, routing keys, and queue configurations. The skill supports schema registry integration for Confluent Schema Registry and AWS Glue, tracking schema compatibility levels (BACKWARD, FORWARD, FULL). Cross-reference analysis identifies event chains and saga patterns across multiple AsyncAPI specs. Output includes an interactive HTML catalog with search, filtering by domain, and dependency visualization between services.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/asyncapi-event-catalog-builder/)
