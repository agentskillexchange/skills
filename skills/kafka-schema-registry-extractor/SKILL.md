---
name: Apache Kafka Schema Registry Extractor
description: Extracts and transforms Avro/Protobuf schemas from Confluent Schema Registry
  using the REST API. Generates TypeScript interfaces, JSON Schema, and data contract
  documentation from registered subjects.
verification: security_reviewed
source: https://agentskillexchange.com/skills/kafka-schema-registry-extractor/
category:
- Data Extraction &amp; Transformation
framework:
- Claude Agents
---
# Apache Kafka Schema Registry Extractor

The Apache Kafka Schema Registry Extractor skill connects to Confluent Schema Registry instances via the REST API (/subjects, /schemas/ids) to catalog, extract, and transform all registered Avro, Protobuf, and JSON Schema definitions. It provides a comprehensive view of your event-driven architecture's data contracts.
The skill fetches all subject versions with compatibility metadata, resolves schema references and cross-subject dependencies, and generates a complete schema dependency graph. For each schema, it can produce TypeScript interfaces using avsc and protobufjs, JSON Schema drafts for API documentation, and Python dataclass stubs using dataclasses-avroschema.
Advanced features include schema evolution analysis showing field additions, removals, and type changes across versions with compatibility impact assessment. It detects breaking changes that would violate BACKWARD, FORWARD, or FULL compatibility modes. The skill also integrates with schema governance by validating naming conventions, required field documentation, and namespace organization. Outputs include Markdown-formatted data dictionaries, Mermaid diagrams of schema relationships, and machine-readable catalogs compatible with DataHub and OpenMetadata ingestion.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kafka-schema-registry-extractor/)
