---
title: "GraphQL Schema Drift Detector"
description: "The GraphQL Schema Drift Detector skill monitors GraphQL API schemas for breaking and dangerous changes between versions. It uses graphql-inspector for schema comparison and the standard GraphQL introspection query (__schema) to fetch live schema definitions from running endpoints.\nThe detection engine performs full schema diff analysis covering object types, input types, enums, interfaces, unions, scalars, and directives. Breaking changes include removed fields, changed field types (narrowing output types or widening input types), removed enum values, and removed interface implementations. Dangerous changes include added required arguments, enum value additions to input enums, and type changes that may affect client codegen.\nThe skill maintains a local schema version history, enabling comparison against any previous version, not just the immediately prior one. It integrates with schema registries like Apollo Studio via the Apollo Platform API and Hasura via the Hasura Metadata API. Diff reports include client impact analysis using operation documents from persisted query stores, identifying exactly which queries and mutations would break. Output formats include markdown changelogs, JSON machine-readable diffs, and Slack-formatted notifications."
verification: security_reviewed
source: "https://github.com/graphql/graphql-js"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "graphql/graphql-js"
  github_stars: 20324
  ase_npm_package: "graphql"
  npm_weekly_downloads: 34200861
---

# GraphQL Schema Drift Detector

The GraphQL Schema Drift Detector skill monitors GraphQL API schemas for breaking and dangerous changes between versions. It uses graphql-inspector for schema comparison and the standard GraphQL introspection query (__schema) to fetch live schema definitions from running endpoints.
The detection engine performs full schema diff analysis covering object types, input types, enums, interfaces, unions, scalars, and directives. Breaking changes include removed fields, changed field types (narrowing output types or widening input types), removed enum values, and removed interface implementations. Dangerous changes include added required arguments, enum value additions to input enums, and type changes that may affect client codegen.
The skill maintains a local schema version history, enabling comparison against any previous version, not just the immediately prior one. It integrates with schema registries like Apollo Studio via the Apollo Platform API and Hasura via the Hasura Metadata API. Diff reports include client impact analysis using operation documents from persisted query stores, identifying exactly which queries and mutations would break. Output formats include markdown changelogs, JSON machine-readable diffs, and Slack-formatted notifications.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/graphql-schema-drift-detector
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/graphql-schema-drift-detector` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-drift-detector/)
