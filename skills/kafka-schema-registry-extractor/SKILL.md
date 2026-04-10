---
title: "Apache Kafka Schema Registry Extractor"
description: "Extracts and transforms Avro/Protobuf schemas from Confluent Schema Registry using the REST API. Generates TypeScript interfaces, JSON Schema, and data contract documentation from registered subjects."
slug: "kafka-schema-registry-extractor"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/kafka-schema-registry-extractor/"
listed: true
---

# Apache Kafka Schema Registry Extractor

Extracts and transforms Avro/Protobuf schemas from Confluent Schema Registry using the REST API. Generates TypeScript interfaces, JSON Schema, and data contract documentation from registered subjects.

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
clawhub install kafka-schema-registry-extractor
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Apache Kafka Schema Registry Extractor skill connects to Confluent Schema Registry instances via the REST API (/subjects, /schemas/ids) to catalog, extract, and transform all registered Avro, Protobuf, and JSON Schema definitions. It provides a comprehensive view of your event-driven architecture’s data contracts.
The skill fetches all subject versions with compatibility metadata, resolves schema references and cross-subject dependencies, and generates a complete schema dependency graph. For each schema, it can produce TypeScript interfaces using avsc and protobufjs, JSON Schema drafts for API documentation, and Python dataclass stubs using dataclasses-avroschema.
Advanced features include schema evolution analysis showing field additions, removals, and type changes across versions with compatibility impact assessment. It detects breaking changes that would violate BACKWARD, FORWARD, or FULL compatibility modes. The skill also integrates with schema governance by validating naming conventions, required field documentation, and namespace organization. Outputs include Markdown-formatted data dictionaries, Mermaid diagrams of schema relationships, and machine-readable catalogs compatible with DataHub and OpenMetadata ingestion.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kafka-schema-registry-extractor/)
