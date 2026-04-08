---
title: GraphQL Schema Introspector
description: The GraphQL Schema Introspector skill provides deep analysis of GraphQL
  API schemas through standard introspection queries. It uses the graphql-js reference
  implementation for schema parsing, validation, and type system analysis. The skill
  connects to GraphQL endpoints using standard introspection queries and the Apollo
  Client devtools protocol for enhanced metadata extraction. It generates comprehensive
  type documentation including object types, interfaces, unions, enums, and input
  types with field-level descriptions. Query complexity analysis calculates estimated
  cost for GraphQL operations based on field depth, list cardinality estimates, and
  resolver complexity weights. This helps identify potentially expensive queries before
  execution against production APIs. Schema diffing compares two schema versions to
  identify breaking changes, deprecated fields, and new additions. The diff report
  follows the graphql-inspector format, categorizing changes as breaking, dangerous,
  or safe. Output formats include markdown documentation, SDL schema files, and interactive
  GraphiQL-compatible exploration pages.
verification: security_reviewed
source: https://agentskillexchange.com/skills/graphql-schema-introspector/
category:
- Library &amp; API Reference
framework:
- MCP
---

# GraphQL Schema Introspector

The GraphQL Schema Introspector skill provides deep analysis of GraphQL API schemas through standard introspection queries. It uses the graphql-js reference implementation for schema parsing, validation, and type system analysis. The skill connects to GraphQL endpoints using standard introspection queries and the Apollo Client devtools protocol for enhanced metadata extraction. It generates comprehensive type documentation including object types, interfaces, unions, enums, and input types with field-level descriptions. Query complexity analysis calculates estimated cost for GraphQL operations based on field depth, list cardinality estimates, and resolver complexity weights. This helps identify potentially expensive queries before execution against production APIs. Schema diffing compares two schema versions to identify breaking changes, deprecated fields, and new additions. The diff report follows the graphql-inspector format, categorizing changes as breaking, dangerous, or safe. Output formats include markdown documentation, SDL schema files, and interactive GraphiQL-compatible exploration pages.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-introspector/)
