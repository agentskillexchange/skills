---
title: "GraphQL Schema Analyzer"
description: "Analyzes GraphQL schemas using graphql-js introspection and @graphql-tools/utils. Maps type relationships, detects N+1 query patterns, and generates DataLoader batching recommendations."
slug: "graphql-schema-analyzer"
category:
  - "Library &amp; API Reference"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/graphql-schema-analyzer/"
listed: true
---

# GraphQL Schema Analyzer

Analyzes GraphQL schemas using graphql-js introspection and @graphql-tools/utils. Maps type relationships, detects N+1 query patterns, and generates DataLoader batching recommendations.

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
clawhub install graphql-schema-analyzer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The GraphQL Schema Analyzer skill provides deep analysis of GraphQL schemas for performance optimization and documentation. It uses graphql-js introspectionFromSchema for complete type system extraction, @graphql-tools/utils for schema manipulation and merging, and generates comprehensive type relationship maps with field-level resolver dependency tracking.
The skill detects potential N+1 query patterns by analyzing resolver chains against database access patterns, identifying list fields that resolve individual items without batching. It generates DataLoader implementation recommendations with batch function signatures and cache key strategies using dataloader@2.x patterns. Connection-type analysis identifies Relay-style pagination implementations and validates cursor encoding schemes.
Advanced capabilities include query complexity estimation using graphql-query-complexity with field-level cost directives, depth limiting analysis for recursive types, and persisted query hash generation for APQ (Automatic Persisted Queries) with apollo-link-persisted-queries patterns. The skill generates TypeScript resolvers type definitions via @graphql-codegen/typescript-resolvers, produces schema change detection reports comparing SDL snapshots, and identifies breaking changes using @graphql-inspector/core for safe schema evolution.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-analyzer/)
