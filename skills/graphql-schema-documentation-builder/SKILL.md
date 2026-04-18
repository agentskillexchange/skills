---
title: "GraphQL Schema Documentation Builder"
description: "Generates interactive API documentation from GraphQL schemas using graphql-js introspection queries and SpectaQL. Produces type relationship diagrams, query examples, and deprecation notices from SDL files."
verification: security_reviewed
source: "https://github.com/graphql/graphql-js"
category:
  - "Library & API Reference"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "graphql/graphql-js"
  github_stars: 20324
  ase_npm_package: "graphql"
  npm_weekly_downloads: 34200861
---

# GraphQL Schema Documentation Builder

The GraphQL Schema Documentation Builder skill transforms GraphQL Schema Definition Language files into comprehensive API documentation. It uses graphql-js introspection queries to extract the full type system including objects, interfaces, unions, enums, and input types with their field-level descriptions.

The skill integrates with SpectaQL for static documentation site generation and graphql-voyager for interactive schema visualization. It parses SDL files to detect @deprecated directives and generates migration guides for deprecated fields with suggested alternatives.

Key features include automatic query and mutation example generation with realistic fake data using faker.js, subscription documentation with WebSocket connection details, custom scalar documentation extraction, and relay-style pagination pattern detection. The skill also validates schemas against best practices including the Shopify GraphQL Design Tutorial guidelines and generates TypeScript type definitions using graphql-codegen for client SDK documentation.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/graphql-schema-documentation-builder
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/graphql-schema-documentation-builder` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-documentation-builder/)
