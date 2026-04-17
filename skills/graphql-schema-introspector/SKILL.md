---
title: "GraphQL Schema Introspector"
description: "The GraphQL Schema Introspector skill provides deep analysis of GraphQL API schemas through standard introspection queries. It uses the graphql-js reference implementation for schema parsing, validation, and type system analysis.\nThe skill connects to GraphQL endpoints using standard introspection queries and the Apollo Client devtools protocol for enhanced metadata extraction. It generates comprehensive type documentation including object types, interfaces, unions, enums, and input types with field-level descriptions.\nQuery complexity analysis calculates estimated cost for GraphQL operations based on field depth, list cardinality estimates, and resolver complexity weights. This helps identify potentially expensive queries before execution against production APIs.\nSchema diffing compares two schema versions to identify breaking changes, deprecated fields, and new additions. The diff report follows the graphql-inspector format, categorizing changes as breaking, dangerous, or safe. Output formats include markdown documentation, SDL schema files, and interactive GraphiQL-compatible exploration pages."
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

# GraphQL Schema Introspector

The GraphQL Schema Introspector skill provides deep analysis of GraphQL API schemas through standard introspection queries. It uses the graphql-js reference implementation for schema parsing, validation, and type system analysis.
The skill connects to GraphQL endpoints using standard introspection queries and the Apollo Client devtools protocol for enhanced metadata extraction. It generates comprehensive type documentation including object types, interfaces, unions, enums, and input types with field-level descriptions.
Query complexity analysis calculates estimated cost for GraphQL operations based on field depth, list cardinality estimates, and resolver complexity weights. This helps identify potentially expensive queries before execution against production APIs.
Schema diffing compares two schema versions to identify breaking changes, deprecated fields, and new additions. The diff report follows the graphql-inspector format, categorizing changes as breaking, dangerous, or safe. Output formats include markdown documentation, SDL schema files, and interactive GraphiQL-compatible exploration pages.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/graphql-schema-introspector
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/graphql-schema-introspector` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-introspector/)
