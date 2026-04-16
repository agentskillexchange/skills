---
title: "Apache Kafka Schema Registry Extractor"
description: "Extracts and transforms Avro/Protobuf schemas from Confluent Schema Registry using the REST API. Generates TypeScript interfaces, JSON Schema, and data contract documentation from registered subjects."
verification: "security_reviewed"
source: "https://github.com/tulios/kafkajs"
category:
  - "Data Extraction & Transformation"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "tulios/kafkajs"
  github_stars: 3992
  ase_npm_package: "kafkajs"
  npm_weekly_downloads: 2520588
  license: "MIT"
---

# Apache Kafka Schema Registry Extractor

The Apache Kafka Schema Registry Extractor skill connects to Confluent Schema Registry instances via the REST API (/subjects, /schemas/ids) to catalog, extract, and transform all registered Avro, Protobuf, and JSON Schema definitions. It provides a comprehensive view of your event-driven architecture’s data contracts.


The skill fetches all subject versions with compatibility metadata, resolves schema references and cross-subject dependencies, and generates a complete schema dependency graph. For each schema, it can produce TypeScript interfaces using avsc and protobufjs, JSON Schema drafts for API documentation, and Python dataclass stubs using dataclasses-avroschema.


Advanced features include schema evolution analysis showing field additions, removals, and type changes across versions with compatibility impact assessment. It detects breaking changes that would violate BACKWARD, FORWARD, or FULL compatibility modes. The skill also integrates with schema governance by validating naming conventions, required field documentation, and namespace organization. Outputs include Markdown-formatted data dictionaries, Mermaid diagrams of schema relationships, and machine-readable catalogs compatible with DataHub and OpenMetadata ingestion.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kafka-schema-registry-extractor/)
