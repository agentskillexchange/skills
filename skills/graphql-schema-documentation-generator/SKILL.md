---
name: "GraphQL Schema Documentation Generator"
description: "Generates interactive API documentation from GraphQL schemas using graphql-js introspection queries and SpectaQL. Annotates fields with usage analytics from Apollo Studio API."
category: "Library &amp; API Reference"
framework: "MCP"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/graphql-schema-documentation-generator/"
---
# GraphQL Schema Documentation Generator

Generates interactive API documentation from GraphQL schemas using graphql-js introspection queries and SpectaQL. Annotates fields with usage analytics from Apollo Studio API.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-documentation-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-documentation-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-documentation-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-documentation-generator -a codex
```

### OpenClaw

```bash
clawhub install graphql-schema-documentation-generator
```

## Details

The GraphQL Schema Documentation Generator skill produces comprehensive, interactive documentation for GraphQL APIs. It performs introspection queries using graphql-js to extract the complete type system including queries, mutations, subscriptions, input types, and custom scalars.

The skill uses SpectaQL to generate static HTML documentation with embedded search, type navigation, and example query generation. It enriches the schema documentation with field-level usage analytics retrieved from the Apollo Studio API, showing which fields are most queried and their average resolution times.

Using the graphql-voyager library integration, the skill produces interactive schema relationship diagrams that visualize type connections and field dependencies. It supports schema stitching documentation for federated architectures using Apollo Federation directives.

Additional features include automatic generation of example queries and mutations with realistic mock data via graphql-faker, deprecation tracking with migration guides, and schema change notifications via the GraphQL Inspector diff tool. Output formats include HTML, Markdown, and Notion-compatible exports.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-documentation-generator/)
