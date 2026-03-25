---
name: "GraphQL Schema Stitcher"
description: "Merges multiple GraphQL schemas into a unified federated gateway using Apollo Federation v2 and graphql-tools stitchSchemas. Validates composed schemas with rover graph check."
category: "Library & API Reference"
framework: "MCP-compatible"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/graphql-schema-stitcher/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "graphql"  # from ase_tool_match
  github_stars: 20335  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 32010306  # from ase_npm_downloads
  github_repo: "graphql/graphql-js"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# GraphQL Schema Stitcher

Merges multiple GraphQL schemas into a unified federated gateway using Apollo Federation v2 and graphql-tools stitchSchemas. Validates composed schemas with rover graph check.

## Overview

The GraphQL Schema Stitcher combines multiple GraphQL subgraph schemas into a unified federated API gateway. It implements Apollo Federation v2 composition using @apollo/composition to merge subgraph SDL definitions with proper entity resolution, @key directives, and shared type handling. The tool also supports legacy schema stitching via graphql-tools stitchSchemas for non-federated architectures, automatically generating type merging configuration and delegating resolvers. Before composition, it validates individual subgraph schemas using graphql-js validateSchema and checks federation compliance with rover graph check against Apollo Studio. The stitcher detects conflicting type definitions, missing entity resolvers, and circular reference issues across subgraphs. It generates a composition report showing type ownership, shared fields, and potential breaking changes. For development workflows, it supports hot-reloading of subgraph schemas from local SDL files or introspection endpoints, with automatic recomposition when changes are detected using chokidar file watchers.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-stitcher
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-stitcher -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-stitcher -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-stitcher -a codex
```

### OpenClaw

```bash
clawhub install graphql-schema-stitcher
```

## Source

- Marketplace: https://agentskillexchange.com/skills/graphql-schema-stitcher/
