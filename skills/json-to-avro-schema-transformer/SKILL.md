---
title: "JSON-to-Avro Schema Transformer"
description: "Transforms JSON Schema definitions into Apache Avro schema format using the jsonschema and fastavro Python libraries. Handles nested objects, arrays, optional fields, and $ref resolution. Registers the resulting Avro schema to Confluent Schema Registry via the Schema Registry REST API."
verification: "security_reviewed"
source: "https://github.com/apache/avro"
author: "Apache Software Foundation"
category:
  - "Data Extraction & Transformation"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "apache/avro"
  github_stars: 3265
---

# JSON-to-Avro Schema Transformer

Transforms JSON Schema definitions into Apache Avro schema format using the jsonschema and fastavro Python libraries. Handles nested objects, arrays, optional fields, and $ref resolution. Registers the resulting Avro schema to Confluent Schema Registry via the Schema Registry REST API.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Documentation

- https://avro.apache.org/docs/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/json-to-avro-schema-transformer/)
