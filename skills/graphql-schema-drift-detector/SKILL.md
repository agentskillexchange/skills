---
title: "GraphQL Schema Drift Detector"
description: "Detects breaking changes in GraphQL schemas using graphql-inspector and the GraphQL introspection query. Compares schema versions, identifies removed fields, changed types, and deprecated directive usage."
slug: "graphql-schema-drift-detector"
category:
  - "Library &amp; API Reference"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/graphql-schema-drift-detector/"
---

# GraphQL Schema Drift Detector

Detects breaking changes in GraphQL schemas using graphql-inspector and the GraphQL introspection query. Compares schema versions, identifies removed fields, changed types, and deprecated directive usage.

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
clawhub install graphql-schema-drift-detector
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The GraphQL Schema Drift Detector skill monitors GraphQL API schemas for breaking and dangerous changes between versions. It uses graphql-inspector for schema comparison and the standard GraphQL introspection query (__schema) to fetch live schema definitions from running endpoints.
The detection engine performs full schema diff analysis covering object types, input types, enums, interfaces, unions, scalars, and directives. Breaking changes include removed fields, changed field types (narrowing output types or widening input types), removed enum values, and removed interface implementations. Dangerous changes include added required arguments, enum value additions to input enums, and type changes that may affect client codegen.
The skill maintains a local schema version history, enabling comparison against any previous version, not just the immediately prior one. It integrates with schema registries like Apollo Studio via the Apollo Platform API and Hasura via the Hasura Metadata API. Diff reports include client impact analysis using operation documents from persisted query stores, identifying exactly which queries and mutations would break. Output formats include markdown changelogs, JSON machine-readable diffs, and Slack-formatted notifications.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-drift-detector/)
