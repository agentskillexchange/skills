---
title: "GraphQL Schema Introspection Analyzer"
description: "The GraphQL Schema Introspection Analyzer skill performs deep analysis of GraphQL API schemas. It sends the standard introspection query (__schema with types, directives, subscriptions) and uses graphql-js utilities (buildClientSchema, printSchema, validate) for comprehensive type system analysis. Schema analysis includes: type coverage reports showing undocumented types and fields, circular reference detection in object type relationships, deprecated field usage tracking with @deprecated directive analysis, and input type complexity scoring for query cost estimation. Performance pattern detection identifies: potential N+1 query patterns in resolver chains (nested object types without @defer), unbounded list returns without pagination arguments (first/last/after/before), missing DataLoader opportunities in sibling field access patterns, and overly deep nesting possibilities without depth limiting. The skill generates: SDL (Schema Definition Language) diffs between versions for breaking change detection, client-side fragment suggestions for optimal query composition, TypeScript type definitions via graphql-codegen patterns, and complexity analysis for implementing query cost limits. It supports federation schemas (Apollo Federation v2 with @key, @shareable, @external directives), relay-style connections validation, and custom scalar documentation verification."
source: "https://github.com/graphql/graphql-js"
verification: "security_reviewed"
category:
  - "Library &amp; API Reference"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "graphql/graphql-js"
  github_stars: 20324
  npm_package: "graphql"
  npm_weekly_downloads: 34200861
---

# GraphQL Schema Introspection Analyzer

The GraphQL Schema Introspection Analyzer skill performs deep analysis of GraphQL API schemas. It sends the standard introspection query (__schema with types, directives, subscriptions) and uses graphql-js utilities (buildClientSchema, printSchema, validate) for comprehensive type system analysis. Schema analysis includes: type coverage reports showing undocumented types and fields, circular reference detection in object type relationships, deprecated field usage tracking with @deprecated directive analysis, and input type complexity scoring for query cost estimation. Performance pattern detection identifies: potential N+1 query patterns in resolver chains (nested object types without @defer), unbounded list returns without pagination arguments (first/last/after/before), missing DataLoader opportunities in sibling field access patterns, and overly deep nesting possibilities without depth limiting. The skill generates: SDL (Schema Definition Language) diffs between versions for breaking change detection, client-side fragment suggestions for optimal query composition, TypeScript type definitions via graphql-codegen patterns, and complexity analysis for implementing query cost limits. It supports federation schemas (Apollo Federation v2 with @key, @shareable, @external directives), relay-style connections validation, and custom scalar documentation verification.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-introspection-analyzer/)
