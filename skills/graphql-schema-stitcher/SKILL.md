---
title: "GraphQL Schema Stitcher"
description: "Merges multiple GraphQL schemas into a unified federated gateway using Apollo Federation v2 and graphql-tools stitchSchemas. Validates composed schemas with rover graph check."
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

# GraphQL Schema Stitcher

The GraphQL Schema Stitcher combines multiple GraphQL subgraph schemas into a unified federated API gateway. It implements Apollo Federation v2 composition using @apollo/composition to merge subgraph SDL definitions with proper entity resolution, @key directives, and shared type handling. The tool also supports legacy schema stitching via graphql-tools stitchSchemas for non-federated architectures, automatically generating type merging configuration and delegating resolvers. Before composition, it validates individual subgraph schemas using graphql-js validateSchema and checks federation compliance with rover graph check against Apollo Studio. The stitcher detects conflicting type definitions, missing entity resolvers, and circular reference issues across subgraphs. It generates a composition report showing type ownership, shared fields, and potential breaking changes. For development workflows, it supports hot-reloading of subgraph schemas from local SDL files or introspection endpoints, with automatic recomposition when changes are detected using chokidar file watchers.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-stitcher/)
