---
title: "GraphQL Schema Documentation Generator"
description: "The GraphQL Schema Documentation Generator skill produces comprehensive, interactive documentation for GraphQL APIs. It performs introspection queries using graphql-js to extract the complete type system including queries, mutations, subscriptions, input types, and custom scalars.\nThe skill uses SpectaQL to generate static HTML documentation with embedded search, type navigation, and example query generation. It enriches the schema documentation with field-level usage analytics retrieved from the Apollo Studio API, showing which fields are most queried and their average resolution times.\nUsing the graphql-voyager library integration, the skill produces interactive schema relationship diagrams that visualize type connections and field dependencies. It supports schema stitching documentation for federated architectures using Apollo Federation directives.\nAdditional features include automatic generation of example queries and mutations with realistic mock data via graphql-faker, deprecation tracking with migration guides, and schema change notifications via the GraphQL Inspector diff tool. Output formats include HTML, Markdown, and Notion-compatible exports."
verification: security_reviewed
source: "https://github.com/graphql/graphql-js"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "graphql/graphql-js"
  github_stars: 20324
  ase_npm_package: "graphql"
  npm_weekly_downloads: 34200861
---

# GraphQL Schema Documentation Generator

The GraphQL Schema Documentation Generator skill produces comprehensive, interactive documentation for GraphQL APIs. It performs introspection queries using graphql-js to extract the complete type system including queries, mutations, subscriptions, input types, and custom scalars.
The skill uses SpectaQL to generate static HTML documentation with embedded search, type navigation, and example query generation. It enriches the schema documentation with field-level usage analytics retrieved from the Apollo Studio API, showing which fields are most queried and their average resolution times.
Using the graphql-voyager library integration, the skill produces interactive schema relationship diagrams that visualize type connections and field dependencies. It supports schema stitching documentation for federated architectures using Apollo Federation directives.
Additional features include automatic generation of example queries and mutations with realistic mock data via graphql-faker, deprecation tracking with migration guides, and schema change notifications via the GraphQL Inspector diff tool. Output formats include HTML, Markdown, and Notion-compatible exports.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/graphql-schema-documentation-generator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/graphql-schema-documentation-generator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-documentation-generator/)
