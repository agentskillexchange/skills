---
name: "GraphQL Schema Documentation Builder"
description: "Generates interactive API documentation from GraphQL schemas using graphql-js introspection queries and SpectaQL. Produces type relationship diagrams, query examples, and deprecation notices from SDL files."
category: "Library & API Reference"
framework: "Gemini"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/graphql-schema-documentation-builder/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "graphql"  # from ase_tool_match
  github_stars: 20335  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 32010306  # from ase_npm_downloads
  github_repo: "graphql/graphql-js"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# GraphQL Schema Documentation Builder

Generates interactive API documentation from GraphQL schemas using graphql-js introspection queries and SpectaQL. Produces type relationship diagrams, query examples, and deprecation notices from SDL files.

## Overview

The GraphQL Schema Documentation Builder skill transforms GraphQL Schema Definition Language files into comprehensive API documentation. It uses graphql-js introspection queries to extract the full type system including objects, interfaces, unions, enums, and input types with their field-level descriptions.

The skill integrates with SpectaQL for static documentation site generation and graphql-voyager for interactive schema visualization. It parses SDL files to detect @deprecated directives and generates migration guides for deprecated fields with suggested alternatives.

Key features include automatic query and mutation example generation with realistic fake data using faker.js, subscription documentation with WebSocket connection details, custom scalar documentation extraction, and relay-style pagination pattern detection. The skill also validates schemas against best practices including the Shopify GraphQL Design Tutorial guidelines and generates TypeScript type definitions using graphql-codegen for client SDK documentation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-documentation-builder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-documentation-builder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-documentation-builder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-documentation-builder -a codex
```

### OpenClaw

```bash
clawhub install graphql-schema-documentation-builder
```

## Source

- Marketplace: https://agentskillexchange.com/skills/graphql-schema-documentation-builder/
