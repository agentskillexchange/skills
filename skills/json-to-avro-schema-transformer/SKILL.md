---
title: JSON-to-Avro Schema Transformer
description: This skill accepts a JSON Schema document and converts it to an Apache
  Avro schema using custom mapping logic built on the jsonschema library for validation
  and fastavro for Avro serialization. It resolves $ref references recursively and
  maps JSON Schema types to Avro equivalents (string, int, long, float, boolean, null,
  array, record). Optional fields in JSON Schema (those not in required) are converted
  to Avro union types with null. The transformed Avro schema is validated by fastavro.parse_schema
  before registration. The skill then calls the Confluent Schema Registry REST API
  (POST /subjects/{subject}/versions) to register the schema under a configurable
  subject naming strategy (TopicNameStrategy or RecordNameStrategy). Dry-run mode
  outputs the Avro JSON without registration. Useful for migrating REST API payloads
  to Kafka event streams.
verification: security_reviewed
source: https://agentskillexchange.com/skills/json-to-avro-schema-transformer/
category:
- Data Extraction &amp; Transformation
framework:
- OpenClaw
---

# JSON-to-Avro Schema Transformer

This skill accepts a JSON Schema document and converts it to an Apache Avro schema using custom mapping logic built on the jsonschema library for validation and fastavro for Avro serialization. It resolves $ref references recursively and maps JSON Schema types to Avro equivalents (string, int, long, float, boolean, null, array, record). Optional fields in JSON Schema (those not in required) are converted to Avro union types with null. The transformed Avro schema is validated by fastavro.parse_schema before registration. The skill then calls the Confluent Schema Registry REST API (POST /subjects/{subject}/versions) to register the schema under a configurable subject naming strategy (TopicNameStrategy or RecordNameStrategy). Dry-run mode outputs the Avro JSON without registration. Useful for migrating REST API payloads to Kafka event streams.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/json-to-avro-schema-transformer/)
