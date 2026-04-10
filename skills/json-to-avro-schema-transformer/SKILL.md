---
name: "JSON-to-Avro Schema Transformer"
description: "Transforms JSON Schema definitions into Apache Avro schema format using the jsonschema and fastavro Python libraries. Handles nested objects, arrays, optional fields, and $ref resolution. Registers the resulting Avro schema to Confluent Schema Registry via the Schema Registry REST API."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/json-to-avro-schema-transformer/"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "OpenClaw"
---

# JSON-to-Avro Schema Transformer

This skill accepts a JSON Schema document and converts it to an Apache Avro schema using custom mapping logic built on the jsonschema library for validation and fastavro for Avro serialization. It resolves $ref references recursively and maps JSON Schema types to Avro equivalents (string, int, long, float, boolean, null, array, record). Optional fields in JSON Schema (those not in required) are converted to Avro union types with null. The transformed Avro schema is validated by fastavro.parse_schema before registration. The skill then calls the Confluent Schema Registry REST API (POST /subjects/{subject}/versions) to register the schema under a configurable subject naming strategy (TopicNameStrategy or RecordNameStrategy). Dry-run mode outputs the Avro JSON without registration. Useful for migrating REST API payloads to Kafka event streams.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/json-to-avro-schema-transformer/)
