---
title: "GraphQL Schema Introspector"
description: "Performs GraphQL schema introspection using the graphql-js reference implementation and Apollo Client devtools protocol. Generates type documentation, query complexity analysis, and schema diff reports between API versions."
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

# GraphQL Schema Introspector

The GraphQL Schema Introspector skill provides deep analysis of GraphQL API schemas through standard introspection queries. It uses the graphql-js reference implementation for schema parsing, validation, and type system analysis.

The skill connects to GraphQL endpoints using standard introspection queries and the Apollo Client devtools protocol for enhanced metadata extraction. It generates comprehensive type documentation including object types, interfaces, unions, enums, and input types with field-level descriptions.

Query complexity analysis calculates estimated cost for GraphQL operations based on field depth, list cardinality estimates, and resolver complexity weights. This helps identify potentially expensive queries before execution against production APIs.

Schema diffing compares two schema versions to identify breaking changes, deprecated fields, and new additions. The diff report follows the graphql-inspector format, categorizing changes as breaking, dangerous, or safe. Output formats include markdown documentation, SDL schema files, and interactive GraphiQL-compatible exploration pages.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-introspector/)
