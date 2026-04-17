---
title: "GraphQL Schema Analyzer"
description: "Analyzes GraphQL schemas using graphql-js introspection and @graphql-tools/utils. Maps type relationships, detects N+1 query patterns, and generates DataLoader batching recommendations."
verification: security_reviewed
source: "https://github.com/graphql/graphql-js"
category:
  - "Library & API Reference"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "graphql/graphql-js"
  github_stars: 20324
  npm_package: "graphql"
  npm_weekly_downloads: 34200861
  license: "MIT"
---

# GraphQL Schema Analyzer

The GraphQL Schema Analyzer skill provides deep analysis of GraphQL schemas for performance optimization and documentation. It uses graphql-js introspectionFromSchema for complete type system extraction, @graphql-tools/utils for schema manipulation and merging, and generates comprehensive type relationship maps with field-level resolver dependency tracking.

The skill detects potential N+1 query patterns by analyzing resolver chains against database access patterns, identifying list fields that resolve individual items without batching. It generates DataLoader implementation recommendations with batch function signatures and cache key strategies using dataloader@2.x patterns. Connection-type analysis identifies Relay-style pagination implementations and validates cursor encoding schemes.

Advanced capabilities include query complexity estimation using graphql-query-complexity with field-level cost directives, depth limiting analysis for recursive types, and persisted query hash generation for APQ (Automatic Persisted Queries) with apollo-link-persisted-queries patterns. The skill generates TypeScript resolvers type definitions via @graphql-codegen/typescript-resolvers, produces schema change detection reports comparing SDL snapshots, and identifies breaking changes using @graphql-inspector/core for safe schema evolution.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/graphql-schema-analyzer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/graphql-schema-analyzer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-analyzer/)
