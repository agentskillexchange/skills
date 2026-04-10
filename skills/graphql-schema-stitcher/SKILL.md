---
name: GraphQL Schema Stitcher
description: Merges multiple GraphQL schemas into a unified federated gateway using
  Apollo Federation v2 and graphql-tools stitchSchemas. Validates composed schemas
  with rover graph check.
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

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-stitcher/)
