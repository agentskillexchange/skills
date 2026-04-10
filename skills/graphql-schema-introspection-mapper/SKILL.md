---
title: "GraphQL Schema Introspection Mapper"
description: "Introspects GraphQL APIs via the __schema query and maps type relationships, deprecated fields, and circular references. Generates SDL exports, TypeScript types via graphql-codegen, and schema diff reports between versions."
slug: "graphql-schema-introspection-mapper"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Cursor"
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/graphql-schema-introspection-mapper/"
listed: true
---

# GraphQL Schema Introspection Mapper

Introspects GraphQL APIs via the __schema query and maps type relationships, deprecated fields, and circular references. Generates SDL exports, TypeScript types via graphql-codegen, and schema diff reports between versions.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install graphql-schema-introspection-mapper
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The GraphQL Schema Introspection Mapper skill provides comprehensive GraphQL API analysis through schema introspection and code generation. It executes the standard __schema introspection query to discover all types, fields, arguments, directives, and their relationships, building a complete type graph of the API surface.
Analysis capabilities include deprecated field inventory with usage tracking, circular reference detection in type relationships that could cause infinite query depth, input validation completeness checking for nullable vs non-null argument definitions, and interface/union type implementation verification. The skill generates visual schema diagrams showing type relationships and field connectivity.
Code generation features leverage graphql-codegen to produce TypeScript type definitions, React Apollo hooks, and urql typed document nodes from the introspected schema. Schema diff reports compare two schema versions to identify breaking changes (field removal, type changes, required argument additions) versus non-breaking additions. The skill supports schema stitching analysis for federated GraphQL architectures using Apollo Federation directives (@key, @external, @requires) and validates subgraph composition compatibility.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-introspection-mapper/)
