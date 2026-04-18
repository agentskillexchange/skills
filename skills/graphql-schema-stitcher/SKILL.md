---
title: "GraphQL Schema Stitcher"
description: "Merges multiple GraphQL schemas into a unified federated gateway using Apollo Federation v2 and graphql-tools stitchSchemas. Validates composed schemas with rover graph check."
verification: security_reviewed
source: "https://github.com/graphql/graphql-js"
category:
  - "Library & API Reference"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "graphql/graphql-js"
  github_stars: 20324
  ase_npm_package: "graphql"
  npm_weekly_downloads: 34200861
---

# GraphQL Schema Stitcher

The GraphQL Schema Stitcher combines multiple GraphQL subgraph schemas into a unified federated API gateway. It implements Apollo Federation v2 composition using @apollo/composition to merge subgraph SDL definitions with proper entity resolution, @key directives, and shared type handling. The tool also supports legacy schema stitching via graphql-tools stitchSchemas for non-federated architectures, automatically generating type merging configuration and delegating resolvers. Before composition, it validates individual subgraph schemas using graphql-js validateSchema and checks federation compliance with rover graph check against Apollo Studio. The stitcher detects conflicting type definitions, missing entity resolvers, and circular reference issues across subgraphs. It generates a composition report showing type ownership, shared fields, and potential breaking changes. For development workflows, it supports hot-reloading of subgraph schemas from local SDL files or introspection endpoints, with automatic recomposition when changes are detected using chokidar file watchers.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/graphql-schema-stitcher
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/graphql-schema-stitcher` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-stitcher/)
