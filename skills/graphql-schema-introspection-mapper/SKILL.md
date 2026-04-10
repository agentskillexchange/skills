---
name: GraphQL Schema Introspection Mapper
description: Introspects GraphQL APIs via the __schema query and maps type relationships,
  deprecated fields, and circular references. Generates SDL exports, TypeScript types
  via graphql-codegen, and schema diff reports between versions.
verification: security_reviewed
source: https://agentskillexchange.com/skills/graphql-schema-introspection-mapper/
category:
- Data Extraction &amp; Transformation
framework:
- Cursor
- Multi-Framework
---
# GraphQL Schema Introspection Mapper

The GraphQL Schema Introspection Mapper skill provides comprehensive GraphQL API analysis through schema introspection and code generation. It executes the standard __schema introspection query to discover all types, fields, arguments, directives, and their relationships, building a complete type graph of the API surface.
Analysis capabilities include deprecated field inventory with usage tracking, circular reference detection in type relationships that could cause infinite query depth, input validation completeness checking for nullable vs non-null argument definitions, and interface/union type implementation verification. The skill generates visual schema diagrams showing type relationships and field connectivity.
Code generation features leverage graphql-codegen to produce TypeScript type definitions, React Apollo hooks, and urql typed document nodes from the introspected schema. Schema diff reports compare two schema versions to identify breaking changes (field removal, type changes, required argument additions) versus non-breaking additions. The skill supports schema stitching analysis for federated GraphQL architectures using Apollo Federation directives (@key, @external, @requires) and validates subgraph composition compatibility.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-introspection-mapper/)
