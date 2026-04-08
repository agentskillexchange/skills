---
title: GraphQL Schema Introspection Analyzer
description: 'The GraphQL Schema Introspection Analyzer skill performs deep analysis
  of GraphQL API schemas. It sends the standard introspection query (__schema with
  types, directives, subscriptions) and uses graphql-js utilities (buildClientSchema,
  printSchema, validate) for comprehensive type system analysis. Schema analysis includes:
  type coverage reports showing undocumented types and fields, circular reference
  detection in object type relationships, deprecated field usage tracking with @deprecated
  directive analysis, and input type complexity scoring for query cost estimation.
  Performance pattern detection identifies: potential N+1 query patterns in resolver
  chains (nested object types without @defer), unbounded list returns without pagination
  arguments (first/last/after/before), missing DataLoader opportunities in sibling
  field access patterns, and overly deep nesting possibilities without depth limiting.
  The skill generates: SDL (Schema Definition Language) diffs between versions for
  breaking change detection, client-side fragment suggestions for optimal query composition,
  TypeScript type definitions via graphql-codegen patterns, and complexity analysis
  for implementing query cost limits. It supports federation schemas (Apollo Federation
  v2 with @key, @shareable, @external directives), relay-style connections validation,
  and custom scalar documentation verification.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/graphql-schema-introspection-analyzer/
category:
- Library &amp; API Reference
framework:
- MCP
---

# GraphQL Schema Introspection Analyzer

The GraphQL Schema Introspection Analyzer skill performs deep analysis of GraphQL API schemas. It sends the standard introspection query (__schema with types, directives, subscriptions) and uses graphql-js utilities (buildClientSchema, printSchema, validate) for comprehensive type system analysis. Schema analysis includes: type coverage reports showing undocumented types and fields, circular reference detection in object type relationships, deprecated field usage tracking with @deprecated directive analysis, and input type complexity scoring for query cost estimation. Performance pattern detection identifies: potential N+1 query patterns in resolver chains (nested object types without @defer), unbounded list returns without pagination arguments (first/last/after/before), missing DataLoader opportunities in sibling field access patterns, and overly deep nesting possibilities without depth limiting. The skill generates: SDL (Schema Definition Language) diffs between versions for breaking change detection, client-side fragment suggestions for optimal query composition, TypeScript type definitions via graphql-codegen patterns, and complexity analysis for implementing query cost limits. It supports federation schemas (Apollo Federation v2 with @key, @shareable, @external directives), relay-style connections validation, and custom scalar documentation verification.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-introspection-analyzer/)
