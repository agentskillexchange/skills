---
title: "GraphQL Schema Introspection Analyzer"
description: "Introspects GraphQL APIs via the standard __schema query and analyzes type systems using graphql-js utilities (buildClientSchema, printSchema). Detects N+1 patterns, circular types, deprecated field usage, and missing nullability annotations."
verification: security_reviewed
source: "https://github.com/graphql/graphql-js"
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

The GraphQL Schema Introspection Analyzer skill performs deep analysis of GraphQL API schemas. It sends the standard introspection query (__schema with types, directives, subscriptions) and uses graphql-js utilities (buildClientSchema, printSchema, validate) for comprehensive type system analysis.

Schema analysis includes: type coverage reports showing undocumented types and fields, circular reference detection in object type relationships, deprecated field usage tracking with @deprecated directive analysis, and input type complexity scoring for query cost estimation.

Performance pattern detection identifies: potential N+1 query patterns in resolver chains (nested object types without @defer), unbounded list returns without pagination arguments (first/last/after/before), missing DataLoader opportunities in sibling field access patterns, and overly deep nesting possibilities without depth limiting.

The skill generates: SDL (Schema Definition Language) diffs between versions for breaking change detection, client-side fragment suggestions for optimal query composition, TypeScript type definitions via graphql-codegen patterns, and complexity analysis for implementing query cost limits.

It supports federation schemas (Apollo Federation v2 with @key, @shareable, @external directives), relay-style connections validation, and custom scalar documentation verification.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-introspection-analyzer/)
