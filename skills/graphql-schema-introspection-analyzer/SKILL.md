---
name: "GraphQL Schema Introspection Analyzer"
description: "Introspects GraphQL APIs via the standard __schema query and analyzes type systems using graphql-js utilities (buildClientSchema, printSchema). Detects N+1 patterns, circular types, deprecated field usage, and missing nullability annotations."
category: "Library & API Reference"
framework: "MCP-compatible"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/graphql-schema-introspection-analyzer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "graphql"  # from ase_tool_match
  github_stars: 20335  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 32010306  # from ase_npm_downloads
  github_repo: "graphql/graphql-js"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# GraphQL Schema Introspection Analyzer

Introspects GraphQL APIs via the standard __schema query and analyzes type systems using graphql-js utilities (buildClientSchema, printSchema). Detects N+1 patterns, circular types, deprecated field usage, and missing nullability annotations.

## Overview

The GraphQL Schema Introspection Analyzer skill performs deep analysis of GraphQL API schemas. It sends the standard introspection query (__schema with types, directives, subscriptions) and uses graphql-js utilities (buildClientSchema, printSchema, validate) for comprehensive type system analysis.

Schema analysis includes: type coverage reports showing undocumented types and fields, circular reference detection in object type relationships, deprecated field usage tracking with @deprecated directive analysis, and input type complexity scoring for query cost estimation.

Performance pattern detection identifies: potential N+1 query patterns in resolver chains (nested object types without @defer), unbounded list returns without pagination arguments (first/last/after/before), missing DataLoader opportunities in sibling field access patterns, and overly deep nesting possibilities without depth limiting.

The skill generates: SDL (Schema Definition Language) diffs between versions for breaking change detection, client-side fragment suggestions for optimal query composition, TypeScript type definitions via graphql-codegen patterns, and complexity analysis for implementing query cost limits.

It supports federation schemas (Apollo Federation v2 with @key, @shareable, @external directives), relay-style connections validation, and custom scalar documentation verification.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-introspection-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-introspection-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-introspection-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-introspection-analyzer -a codex
```

### OpenClaw

```bash
clawhub install graphql-schema-introspection-analyzer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/graphql-schema-introspection-analyzer/
