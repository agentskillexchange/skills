---
name: "GraphQL Schema Analyzer"
description: "Analyzes GraphQL schemas using graphql-js introspection and @graphql-tools/utils. Maps type relationships, detects N+1 query patterns, and generates DataLoader batching recommendations."
category: "Library & API Reference"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/graphql-schema-analyzer/"
---
# GraphQL Schema Analyzer

Analyzes GraphQL schemas using graphql-js introspection and @graphql-tools/utils. Maps type relationships, detects N+1 query patterns, and generates DataLoader batching recommendations.

## Overview

The GraphQL Schema Analyzer skill provides deep analysis of GraphQL schemas for performance optimization and documentation. It uses graphql-js introspectionFromSchema for complete type system extraction, @graphql-tools/utils for schema manipulation and merging, and generates comprehensive type relationship maps with field-level resolver dependency tracking.

The skill detects potential N+1 query patterns by analyzing resolver chains against database access patterns, identifying list fields that resolve individual items without batching. It generates DataLoader implementation recommendations with batch function signatures and cache key strategies using dataloader@2.x patterns. Connection-type analysis identifies Relay-style pagination implementations and validates cursor encoding schemes.

Advanced capabilities include query complexity estimation using graphql-query-complexity with field-level cost directives, depth limiting analysis for recursive types, and persisted query hash generation for APQ (Automatic Persisted Queries) with apollo-link-persisted-queries patterns. The skill generates TypeScript resolvers type definitions via @graphql-codegen/typescript-resolvers, produces schema change detection reports comparing SDL snapshots, and identifies breaking changes using @graphql-inspector/core for safe schema evolution.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-analyzer -a codex
```

### OpenClaw

```bash
clawhub install graphql-schema-analyzer
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-analyzer/)
