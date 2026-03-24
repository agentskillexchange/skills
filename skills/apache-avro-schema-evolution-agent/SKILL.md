---
name: "Apache Avro Schema Evolution Agent"
description: "Manages Apache Avro schema evolution with compatibility checking via Confluent Schema Registry API. Validates forward, backward, and full compatibility across schema versions automatically."
category: "Data Extraction & Transformation"
framework: "MCP-compatible"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/apache-avro-schema-evolution-agent/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "kafka"  # from ase_tool_match
  github_stars: 3987  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 2396148  # from ase_npm_downloads
  github_repo: "tulios/kafkajs"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: false  # from ase_tool_maintained
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
