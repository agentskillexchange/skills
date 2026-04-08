---
title: GraphQL Schema Stitcher
description: The GraphQL Schema Stitcher combines multiple GraphQL subgraph schemas
  into a unified federated API gateway. It implements Apollo Federation v2 composition
  using @apollo/composition to merge subgraph SDL definitions with proper entity resolution,
  @key directives, and shared type handling. The tool also supports legacy schema
  stitching via graphql-tools stitchSchemas for non-federated architectures, automatically
  generating type merging configuration and delegating resolvers. Before composition,
  it validates individual subgraph schemas using graphql-js validateSchema and checks
  federation compliance with rover graph check against Apollo Studio. The stitcher
  detects conflicting type definitions, missing entity resolvers, and circular reference
  issues across subgraphs. It generates a composition report showing type ownership,
  shared fields, and potential breaking changes. For development workflows, it supports
  hot-reloading of subgraph schemas from local SDL files or introspection endpoints,
  with automatic recomposition when changes are detected using chokidar file watchers.
verification: security_reviewed
source: https://agentskillexchange.com/skills/graphql-schema-stitcher/
category:
- Library &amp; API Reference
framework:
- MCP
---

# GraphQL Schema Stitcher

The GraphQL Schema Stitcher combines multiple GraphQL subgraph schemas into a unified federated API gateway. It implements Apollo Federation v2 composition using @apollo/composition to merge subgraph SDL definitions with proper entity resolution, @key directives, and shared type handling. The tool also supports legacy schema stitching via graphql-tools stitchSchemas for non-federated architectures, automatically generating type merging configuration and delegating resolvers. Before composition, it validates individual subgraph schemas using graphql-js validateSchema and checks federation compliance with rover graph check against Apollo Studio. The stitcher detects conflicting type definitions, missing entity resolvers, and circular reference issues across subgraphs. It generates a composition report showing type ownership, shared fields, and potential breaking changes. For development workflows, it supports hot-reloading of subgraph schemas from local SDL files or introspection endpoints, with automatic recomposition when changes are detected using chokidar file watchers.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-stitcher/)
