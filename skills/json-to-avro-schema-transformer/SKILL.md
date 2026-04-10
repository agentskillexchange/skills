---
title: "JSON-to-Avro Schema Transformer"
description: "Transforms JSON Schema definitions into Apache Avro schema format using the jsonschema and fastavro Python libraries. Handles nested objects, arrays, optional fields, and $ref resolution. Registers the resulting Avro schema to Confluent Schema Registry via the Schema Registry REST API."
slug: "json-to-avro-schema-transformer"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/json-to-avro-schema-transformer/"
listed: true
---

# JSON-to-Avro Schema Transformer

Transforms JSON Schema definitions into Apache Avro schema format using the jsonschema and fastavro Python libraries. Handles nested objects, arrays, optional fields, and $ref resolution. Registers the resulting Avro schema to Confluent Schema Registry via the Schema Registry REST API.

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
clawhub install json-to-avro-schema-transformer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill accepts a JSON Schema document and converts it to an Apache Avro schema using custom mapping logic built on the jsonschema library for validation and fastavro for Avro serialization. It resolves $ref references recursively and maps JSON Schema types to Avro equivalents (string, int, long, float, boolean, null, array, record). Optional fields in JSON Schema (those not in required) are converted to Avro union types with null. The transformed Avro schema is validated by fastavro.parse_schema before registration. The skill then calls the Confluent Schema Registry REST API (POST /subjects/{subject}/versions) to register the schema under a configurable subject naming strategy (TopicNameStrategy or RecordNameStrategy). Dry-run mode outputs the Avro JSON without registration. Useful for migrating REST API payloads to Kafka event streams.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/json-to-avro-schema-transformer/)
