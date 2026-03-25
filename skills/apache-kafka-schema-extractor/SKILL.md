---
name: "Apache Kafka Schema Extractor"
description: "Extracts and transforms Avro, Protobuf, and JSON Schema definitions from Confluent Schema Registry. Generates typed data models and validates schema compatibility using the Schema Registry REST API."
category: "Data Extraction & Transformation"
framework: "Codex"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/apache-kafka-schema-extractor/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "kafka"  # from ase_tool_match
  github_stars: 3987  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 2396148  # from ase_npm_downloads
  github_repo: "tulios/kafkajs"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: false  # from ase_tool_maintained
---

# Apache Kafka Schema Extractor

Extracts and transforms Avro, Protobuf, and JSON Schema definitions from Confluent Schema Registry. Generates typed data models and validates schema compatibility using the Schema Registry REST API.

## Overview

The Apache Kafka Schema Extractor skill interfaces with the Confluent Schema Registry REST API to discover, extract, and transform message schemas across Kafka topics. It retrieves Avro, Protobuf, and JSON Schema definitions and generates typed data models in Python, TypeScript, and Go. The skill performs schema compatibility validation using the compatibility checker endpoints, supporting BACKWARD, FORWARD, FULL, and NONE compatibility modes. Features include automatic schema evolution tracking with diff visualization, dead letter queue schema mismatch detection, and bulk schema export for migration between registries. Integrates with Kafka Connect REST API for connector schema alignment verification and supports schema context management for multi-tenant environments. Provides schema documentation generation in Markdown format.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill apache-kafka-schema-extractor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill apache-kafka-schema-extractor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill apache-kafka-schema-extractor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill apache-kafka-schema-extractor -a codex
```

### OpenClaw

```bash
clawhub install apache-kafka-schema-extractor
```

## Source

- Marketplace: https://agentskillexchange.com/skills/apache-kafka-schema-extractor/
