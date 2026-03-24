---
name: "GraphQL Schema Introspection Mapper"
description: "Introspects GraphQL APIs via the __schema query and maps type relationships, deprecated fields, and circular references. Generates SDL exports, TypeScript types via graphql-codegen, and schema diff reports between versions."
category: "Data Extraction & Transformation"
framework: "Cursor"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/graphql-schema-introspection-mapper/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "graphql"  # from ase_tool_match
  github_stars: 20335  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 32010306  # from ase_npm_downloads
  github_repo: "graphql/graphql-js"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# GraphQL Schema Introspection Mapper

Introspects GraphQL APIs via the __schema query and maps type relationships, deprecated fields, and circular references. Generates SDL exports, TypeScript types via graphql-codegen, and schema diff reports between versions.

## Overview

The GraphQL Schema Introspection Mapper skill provides comprehensive GraphQL API analysis through schema introspection and code generation. It executes the standard __schema introspection query to discover all types, fields, arguments, directives, and their relationships, building a complete type graph of the API surface.

Analysis capabilities include deprecated field inventory with usage tracking, circular reference detection in type relationships that could cause infinite query depth, input validation completeness checking for nullable vs non-null argument definitions, and interface/union type implementation verification. The skill generates visual schema diagrams showing type relationships and field connectivity.

Code generation features leverage graphql-codegen to produce TypeScript type definitions, React Apollo hooks, and urql typed document nodes from the introspected schema. Schema diff reports compare two schema versions to identify breaking changes (field removal, type changes, required argument additions) versus non-breaking additions. The skill supports schema stitching analysis for federated GraphQL architectures using Apollo Federation directives (@key, @external, @requires) and validates subgraph composition compatibility.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-introspection-mapper
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-introspection-mapper -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-introspection-mapper -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-introspection-mapper -a codex
```

### OpenClaw

```bash
clawhub install graphql-schema-introspection-mapper
```

## Source

- Marketplace: https://agentskillexchange.com/skills/graphql-schema-introspection-mapper/
