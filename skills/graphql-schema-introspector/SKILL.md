---
name: "GraphQL Schema Introspector"
description: "Performs GraphQL schema introspection using the graphql-js reference implementation and Apollo Client devtools protocol. Generates type documentation, query complexity analysis, and schema diff reports between API versions."
category: "Library & API Reference"
framework: "MCP-compatible"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/graphql-schema-introspector/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "graphql"  # from ase_tool_match
  github_stars: 20332  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 32010306  # from ase_npm_downloads
  github_repo: "graphql/graphql-js"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# GraphQL Schema Introspector

Performs GraphQL schema introspection using the graphql-js reference implementation and Apollo Client devtools protocol. Generates type documentation, query complexity analysis, and schema diff reports between API versions.

## Overview

The GraphQL Schema Introspector skill provides deep analysis of GraphQL API schemas through standard introspection queries. It uses the graphql-js reference implementation for schema parsing, validation, and type system analysis.

The skill connects to GraphQL endpoints using standard introspection queries and the Apollo Client devtools protocol for enhanced metadata extraction. It generates comprehensive type documentation including object types, interfaces, unions, enums, and input types with field-level descriptions.

Query complexity analysis calculates estimated cost for GraphQL operations based on field depth, list cardinality estimates, and resolver complexity weights. This helps identify potentially expensive queries before execution against production APIs.

Schema diffing compares two schema versions to identify breaking changes, deprecated fields, and new additions. The diff report follows the graphql-inspector format, categorizing changes as breaking, dangerous, or safe. Output formats include markdown documentation, SDL schema files, and interactive GraphiQL-compatible exploration pages.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-introspector
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-introspector -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-introspector -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-introspector -a codex
```

### OpenClaw

```bash
clawhub install graphql-schema-introspector
```

## Source

- Marketplace: https://agentskillexchange.com/skills/graphql-schema-introspector/
