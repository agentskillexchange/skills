---
title: "GraphQL Schema Introspector"
description: "The GraphQL Schema Introspector skill provides deep analysis of GraphQL API schemas through standard introspection queries. It uses the graphql-js reference implementation for schema parsing, validation, and type system analysis. The skill connects to GraphQL endpoints using standard introspection queries and the Apollo Client devtools protocol for enhanced metadata extraction. It generates comprehensive type documentation including object types, interfaces, unions, enums, and input types with field-level descriptions. Query complexity analysis calculates estimated cost for GraphQL operations based on field depth, list cardinality estimates, and resolver complexity weights. This helps identify potentially expensive queries before execution against production APIs. Schema diffing compares two schema versions to identify breaking changes, deprecated fields, and new additions. The diff report follows the graphql-inspector format, categorizing changes as breaking, dangerous, or safe. Output formats include markdown documentation, SDL schema files, and interactive GraphiQL-compatible exploration pages."
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

# GraphQL Schema Introspector

The GraphQL Schema Introspector skill provides deep analysis of GraphQL API schemas through standard introspection queries. It uses the graphql-js reference implementation for schema parsing, validation, and type system analysis. The skill connects to GraphQL endpoints using standard introspection queries and the Apollo Client devtools protocol for enhanced metadata extraction. It generates comprehensive type documentation including object types, interfaces, unions, enums, and input types with field-level descriptions. Query complexity analysis calculates estimated cost for GraphQL operations based on field depth, list cardinality estimates, and resolver complexity weights. This helps identify potentially expensive queries before execution against production APIs. Schema diffing compares two schema versions to identify breaking changes, deprecated fields, and new additions. The diff report follows the graphql-inspector format, categorizing changes as breaking, dangerous, or safe. Output formats include markdown documentation, SDL schema files, and interactive GraphiQL-compatible exploration pages.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-introspector/)
