---
name: "GraphQL Schema Drift Detector"
description: "Detects breaking changes in GraphQL schemas using graphql-inspector and the GraphQL introspection query. Compares schema versions, identifies removed fields, changed types, and deprecated directive usage."
category: "Library & API Reference"
framework: "MCP"
verification: security_reviewed
source: "https://github.com/graphql/graphql-js"
tool_ecosystem:
  tool: graphql
  github_stars: 20332
  npm_weekly_downloads: 32010306
  github_repo: graphql/graphql-js
  license: MIT
  maintained: true
---
# GraphQL Schema Drift Detector

Detects breaking changes in GraphQL schemas using graphql-inspector and the GraphQL introspection query. Compares schema versions, identifies removed fields, changed types, and deprecated directive usage.

## Overview

The GraphQL Schema Drift Detector skill monitors GraphQL API schemas for breaking and dangerous changes between versions. It uses graphql-inspector for schema comparison and the standard GraphQL introspection query (__schema) to fetch live schema definitions from running endpoints.

The detection engine performs full schema diff analysis covering object types, input types, enums, interfaces, unions, scalars, and directives. Breaking changes include removed fields, changed field types (narrowing output types or widening input types), removed enum values, and removed interface implementations. Dangerous changes include added required arguments, enum value additions to input enums, and type changes that may affect client codegen.

The skill maintains a local schema version history, enabling comparison against any previous version, not just the immediately prior one. It integrates with schema registries like Apollo Studio via the Apollo Platform API and Hasura via the Hasura Metadata API. Diff reports include client impact analysis using operation documents from persisted query stores, identifying exactly which queries and mutations would break. Output formats include markdown changelogs, JSON machine-readable diffs, and Slack-formatted notifications.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-drift-detector
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-drift-detector -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-drift-detector -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-drift-detector -a codex
```

### OpenClaw

```bash
clawhub install graphql-schema-drift-detector
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-drift-detector/)
