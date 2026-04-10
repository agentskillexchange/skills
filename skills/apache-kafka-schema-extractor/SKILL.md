---
name: "Apache Kafka Schema Extractor"
description: "Extracts and transforms Avro, Protobuf, and JSON Schema definitions from Confluent Schema Registry. Generates typed data models and validates schema compatibility using the Schema Registry REST API."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/apache-kafka-schema-extractor/"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Codex"
---

# Apache Kafka Schema Extractor

The Apache Kafka Schema Extractor skill interfaces with the Confluent Schema Registry REST API to discover, extract, and transform message schemas across Kafka topics. It retrieves Avro, Protobuf, and JSON Schema definitions and generates typed data models in Python, TypeScript, and Go. The skill performs schema compatibility validation using the compatibility checker endpoints, supporting BACKWARD, FORWARD, FULL, and NONE compatibility modes. Features include automatic schema evolution tracking with diff visualization, dead letter queue schema mismatch detection, and bulk schema export for migration between registries. Integrates with Kafka Connect REST API for connector schema alignment verification and supports schema context management for multi-tenant environments. Provides schema documentation generation in Markdown format.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apache-kafka-schema-extractor/)
