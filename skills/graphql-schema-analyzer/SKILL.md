---
title: "GraphQL Schema Analyzer"
description: "Analyzes GraphQL schemas using graphql-js introspection and @graphql-tools/utils. Maps type relationships, detects N+1 query patterns, and generates DataLoader batching recommendations."
verification: security_reviewed
source: "https://github.com/graphql/graphql-js"
category:
  - "Library &amp; API Reference"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "graphql/graphql-js"
  github_stars: 20324
  npm_package: "graphql"
  npm_weekly_downloads: 34200861
---

# GraphQL Schema Analyzer

The GraphQL Schema Analyzer skill provides deep analysis of GraphQL schemas for performance optimization and documentation. It uses graphql-js introspectionFromSchema for complete type system extraction, @graphql-tools/utils for schema manipulation and merging, and generates comprehensive type relationship maps with field-level resolver dependency tracking.

The skill detects potential N+1 query patterns by analyzing resolver chains against database access patterns, identifying list fields that resolve individual items without batching. It generates DataLoader implementation recommendations with batch function signatures and cache key strategies using dataloader@2.x patterns. Connection-type analysis identifies Relay-style pagination implementations and validates cursor encoding schemes.

Advanced capabilities include query complexity estimation using graphql-query-complexity with field-level cost directives, depth limiting analysis for recursive types, and persisted query hash generation for APQ (Automatic Persisted Queries) with apollo-link-persisted-queries patterns. The skill generates TypeScript resolvers type definitions via @graphql-codegen/typescript-resolvers, produces schema change detection reports comparing SDL snapshots, and identifies breaking changes using @graphql-inspector/core for safe schema evolution.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-analyzer/)
