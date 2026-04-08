---
title: GraphQL Schema Drift Detector
description: The GraphQL Schema Drift Detector skill monitors GraphQL API schemas
  for breaking and dangerous changes between versions. It uses graphql-inspector for
  schema comparison and the standard GraphQL introspection query (__schema) to fetch
  live schema definitions from running endpoints. The detection engine performs full
  schema diff analysis covering object types, input types, enums, interfaces, unions,
  scalars, and directives. Breaking changes include removed fields, changed field
  types (narrowing output types or widening input types), removed enum values, and
  removed interface implementations. Dangerous changes include added required arguments,
  enum value additions to input enums, and type changes that may affect client codegen.
  The skill maintains a local schema version history, enabling comparison against
  any previous version, not just the immediately prior one. It integrates with schema
  registries like Apollo Studio via the Apollo Platform API and Hasura via the Hasura
  Metadata API. Diff reports include client impact analysis using operation documents
  from persisted query stores, identifying exactly which queries and mutations would
  break. Output formats include markdown changelogs, JSON machine-readable diffs,
  and Slack-formatted notifications.
verification: security_reviewed
source: https://agentskillexchange.com/skills/graphql-schema-drift-detector/
category:
- Library &amp; API Reference
framework:
- MCP
---

# GraphQL Schema Drift Detector

The GraphQL Schema Drift Detector skill monitors GraphQL API schemas for breaking and dangerous changes between versions. It uses graphql-inspector for schema comparison and the standard GraphQL introspection query (__schema) to fetch live schema definitions from running endpoints. The detection engine performs full schema diff analysis covering object types, input types, enums, interfaces, unions, scalars, and directives. Breaking changes include removed fields, changed field types (narrowing output types or widening input types), removed enum values, and removed interface implementations. Dangerous changes include added required arguments, enum value additions to input enums, and type changes that may affect client codegen. The skill maintains a local schema version history, enabling comparison against any previous version, not just the immediately prior one. It integrates with schema registries like Apollo Studio via the Apollo Platform API and Hasura via the Hasura Metadata API. Diff reports include client impact analysis using operation documents from persisted query stores, identifying exactly which queries and mutations would break. Output formats include markdown changelogs, JSON machine-readable diffs, and Slack-formatted notifications.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-drift-detector/)
