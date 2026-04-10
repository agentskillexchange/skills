---
name: AsyncAPI Event Catalog Builder
description: Generates event-driven architecture documentation from AsyncAPI 3.0 specifications.
  Uses the AsyncAPI parser-js library to extract channels, message schemas, and server
  bindings for Kafka and RabbitMQ.
verification: security_reviewed
source: https://agentskillexchange.com/skills/asyncapi-event-catalog-builder/
category:
- Library &amp; API Reference
framework:
- Gemini
---
# AsyncAPI Event Catalog Builder

The AsyncAPI Event Catalog Builder parses AsyncAPI 3.0 specification files to generate comprehensive event-driven architecture documentation. Using the official @asyncapi/parser library, it extracts channel definitions, message payload schemas (JSON Schema and Avro), server bindings, and operation traits. The skill generates catalog pages for each event type showing producers, consumers, schema evolution history, and payload examples. Kafka-specific bindings are resolved to show topic configurations, partition key strategies, and consumer group assignments. RabbitMQ bindings map exchanges, routing keys, and queue configurations. The skill supports schema registry integration for Confluent Schema Registry and AWS Glue, tracking schema compatibility levels (BACKWARD, FORWARD, FULL). Cross-reference analysis identifies event chains and saga patterns across multiple AsyncAPI specs. Output includes an interactive HTML catalog with search, filtering by domain, and dependency visualization between services.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/asyncapi-event-catalog-builder/)
