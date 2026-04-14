---
title: "GraphQL Schema Documentation Generator"
description: "Generates interactive API documentation from GraphQL schemas using graphql-js introspection queries and SpectaQL. Annotates fields with usage analytics from Apollo Studio API."
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

# GraphQL Schema Documentation Generator

The GraphQL Schema Documentation Generator skill produces comprehensive, interactive documentation for GraphQL APIs. It performs introspection queries using graphql-js to extract the complete type system including queries, mutations, subscriptions, input types, and custom scalars.

The skill uses SpectaQL to generate static HTML documentation with embedded search, type navigation, and example query generation. It enriches the schema documentation with field-level usage analytics retrieved from the Apollo Studio API, showing which fields are most queried and their average resolution times.

Using the graphql-voyager library integration, the skill produces interactive schema relationship diagrams that visualize type connections and field dependencies. It supports schema stitching documentation for federated architectures using Apollo Federation directives.

Additional features include automatic generation of example queries and mutations with realistic mock data via graphql-faker, deprecation tracking with migration guides, and schema change notifications via the GraphQL Inspector diff tool. Output formats include HTML, Markdown, and Notion-compatible exports.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-documentation-generator/)
