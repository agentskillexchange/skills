---
name: "Apache Kafka Schema Registry Extractor"
description: "Extracts and transforms Avro/Protobuf schemas from Confluent Schema Registry using the REST API. Generates TypeScript interfaces, JSON Schema, and data contract documentation from registered subjects."
category: "Data Extraction & Transformation"
framework: "Claude Agents"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/kafka-schema-registry-extractor/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "kafka"  # from ase_tool_match
  github_stars: 3987  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 2396148  # from ase_npm_downloads
  github_repo: "tulios/kafkajs"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: false  # from ase_tool_maintained
---

# Apache Kafka Schema Registry Extractor

Extracts and transforms Avro/Protobuf schemas from Confluent Schema Registry using the REST API. Generates TypeScript interfaces, JSON Schema, and data contract documentation from registered subjects.

## Overview

The Apache Kafka Schema Registry Extractor skill connects to Confluent Schema Registry instances via the REST API (/subjects, /schemas/ids) to catalog, extract, and transform all registered Avro, Protobuf, and JSON Schema definitions. It provides a comprehensive view of your event-driven architecture’s data contracts.

The skill fetches all subject versions with compatibility metadata, resolves schema references and cross-subject dependencies, and generates a complete schema dependency graph. For each schema, it can produce TypeScript interfaces using avsc and protobufjs, JSON Schema drafts for API documentation, and Python dataclass stubs using dataclasses-avroschema.

Advanced features include schema evolution analysis showing field additions, removals, and type changes across versions with compatibility impact assessment. It detects breaking changes that would violate BACKWARD, FORWARD, or FULL compatibility modes. The skill also integrates with schema governance by validating naming conventions, required field documentation, and namespace organization. Outputs include Markdown-formatted data dictionaries, Mermaid diagrams of schema relationships, and machine-readable catalogs compatible with DataHub and OpenMetadata ingestion.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill kafka-schema-registry-extractor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill kafka-schema-registry-extractor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill kafka-schema-registry-extractor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill kafka-schema-registry-extractor -a codex
```

### OpenClaw

```bash
clawhub install kafka-schema-registry-extractor
```

## Source

- Marketplace: https://agentskillexchange.com/skills/kafka-schema-registry-extractor/
