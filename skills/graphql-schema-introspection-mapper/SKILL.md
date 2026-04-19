---
title: "GraphQL Schema Introspection Mapper"
description: "The GraphQL Schema Introspection Mapper skill provides comprehensive GraphQL API analysis through schema introspection and code generation. It executes the standard __schema introspection query to discover all types, fields, arguments, directives, and their relationships, building a complete type graph of the API surface. Analysis capabilities include deprecated field inventory with usage tracking, circular reference detection in type relationships that could cause infinite query depth, input validation completeness checking for nullable vs non-null argument definitions, and interface/union type implementation verification. The skill generates visual schema diagrams showing type relationships and field connectivity. Code generation features leverage graphql-codegen to produce TypeScript type definitions, React Apollo hooks, and urql typed document nodes from the introspected schema. Schema diff reports compare two schema versions to identify breaking changes (field removal, type changes, required argument additions) versus non-breaking additions. The skill supports schema stitching analysis for federated GraphQL architectures using Apollo Federation directives (@key, @external, @requires) and validates subgraph composition compatibility."
source: "https://github.com/graphql/graphql-js"
verification: "security_reviewed"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Cursor"
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "graphql/graphql-js"
  github_stars: 20324
  npm_package: "graphql"
  npm_weekly_downloads: 34200861
---

# GraphQL Schema Introspection Mapper

The GraphQL Schema Introspection Mapper skill provides comprehensive GraphQL API analysis through schema introspection and code generation. It executes the standard __schema introspection query to discover all types, fields, arguments, directives, and their relationships, building a complete type graph of the API surface. Analysis capabilities include deprecated field inventory with usage tracking, circular reference detection in type relationships that could cause infinite query depth, input validation completeness checking for nullable vs non-null argument definitions, and interface/union type implementation verification. The skill generates visual schema diagrams showing type relationships and field connectivity. Code generation features leverage graphql-codegen to produce TypeScript type definitions, React Apollo hooks, and urql typed document nodes from the introspected schema. Schema diff reports compare two schema versions to identify breaking changes (field removal, type changes, required argument additions) versus non-breaking additions. The skill supports schema stitching analysis for federated GraphQL architectures using Apollo Federation directives (@key, @external, @requires) and validates subgraph composition compatibility.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-introspection-mapper/)
