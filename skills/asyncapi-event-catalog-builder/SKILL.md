---
name: "AsyncAPI Event Catalog Builder"
description: "Generates event-driven architecture documentation from AsyncAPI 3.0 specifications. Uses the AsyncAPI parser-js library to extract channels, message schemas, and server bindings for Kafka and RabbitMQ."
category: "Library & API Reference"
framework: "Gemini"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/asyncapi-event-catalog-builder/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "kafka"  # from ase_tool_match
  github_stars: 3987  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 2396148  # from ase_npm_downloads
  github_repo: "tulios/kafkajs"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: false  # from ase_tool_maintained
---

# AsyncAPI Event Catalog Builder

Generates event-driven architecture documentation from AsyncAPI 3.0 specifications. Uses the AsyncAPI parser-js library to extract channels, message schemas, and server bindings for Kafka and RabbitMQ.

## Overview

The AsyncAPI Event Catalog Builder parses AsyncAPI 3.0 specification files to generate comprehensive event-driven architecture documentation. Using the official @asyncapi/parser library, it extracts channel definitions, message payload schemas (JSON Schema and Avro), server bindings, and operation traits. The skill generates catalog pages for each event type showing producers, consumers, schema evolution history, and payload examples. Kafka-specific bindings are resolved to show topic configurations, partition key strategies, and consumer group assignments. RabbitMQ bindings map exchanges, routing keys, and queue configurations. The skill supports schema registry integration for Confluent Schema Registry and AWS Glue, tracking schema compatibility levels (BACKWARD, FORWARD, FULL). Cross-reference analysis identifies event chains and saga patterns across multiple AsyncAPI specs. Output includes an interactive HTML catalog with search, filtering by domain, and dependency visualization between services.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill asyncapi-event-catalog-builder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill asyncapi-event-catalog-builder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill asyncapi-event-catalog-builder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill asyncapi-event-catalog-builder -a codex
```

### OpenClaw

```bash
clawhub install asyncapi-event-catalog-builder
```

## Source

- Marketplace: https://agentskillexchange.com/skills/asyncapi-event-catalog-builder/
