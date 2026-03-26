---
name: "Apache Avro Schema Evolution Agent"
description: "Manages Apache Avro schema evolution with compatibility checking via Confluent Schema Registry API. Validates forward, backward, and full compatibility across schema versions automatically."
category: "Data Extraction & Transformation"
framework: "MCP"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/apache-avro-schema-evolution-agent/"
tool_ecosystem:
  tool: "kafka"
  github_stars: 3988
  npm_weekly_downloads: 2396148
  github_repo: "tulios/kafkajs"
  license: "MIT"
  maintained: false
---

# Apache Avro Schema Evolution Agent

Manages Apache Avro schema evolution with compatibility checking via Confluent Schema Registry API. Validates forward, backward, and full compatibility across schema versions automatically.

## Overview

The Apache Avro Schema Evolution Agent manages schema lifecycle for event-driven architectures by interfacing with the Confluent Schema Registry REST API. It validates schema changes against compatibility rules (backward, forward, full, and transitive variants) before registration, preventing breaking changes in production Kafka topics. The agent parses Avro IDL and JSON schema formats, detects field additions, removals, type promotions, and default value requirements. It generates migration code for schema transitions, handles union type evolution, and manages subject naming strategies for topic-key and topic-value schemas. The agent supports schema references for complex nested types, provides diff visualization between schema versions, and integrates with CI pipelines to enforce compatibility gates. Includes automatic documentation generation showing schema lineage and consumer impact analysis.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill apache-avro-schema-evolution-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill apache-avro-schema-evolution-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill apache-avro-schema-evolution-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill apache-avro-schema-evolution-agent -a codex
```

### OpenClaw

```bash
clawhub install apache-avro-schema-evolution-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/apache-avro-schema-evolution-agent/
