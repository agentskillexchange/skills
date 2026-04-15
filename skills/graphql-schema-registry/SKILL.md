---
title: "GraphQL Schema Registry"
description: "Manages GraphQL schema evolution using graphql-inspector for breaking change detection and Apollo Rover CLI for schema composition. Validates schemas against custom ESLint rules via @graphql-eslint/eslint-plugin."
verification: security_reviewed
source: "https://github.com/graphql/graphql-js"
category:
  - "Library & API Reference"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "graphql/graphql-js"
  github_stars: 20324
  npm_package: "graphql"
  npm_weekly_downloads: 34200861
---

# GraphQL Schema Registry

The GraphQL Schema Registry skill provides schema lifecycle management for GraphQL APIs, handling validation, evolution tracking, and federated composition. It uses graphql-inspector to compare schema versions and detect breaking changes including removed fields, changed argument types, and modified enum values.

For federated architectures, the skill leverages Apollo Rover CLI (rover supergraph compose) to compose subgraph schemas into a unified supergraph, validating that all entity references resolve correctly and that no naming conflicts exist across subgraphs. It supports both Apollo Federation v1 and v2 directives.

Schema quality is enforced through @graphql-eslint/eslint-plugin with configurable rule sets covering naming conventions (camelCase fields, PascalCase types), description requirements for public-facing fields, depth limiting rules to prevent abuse, and relay-style connection pagination patterns.

The skill generates comprehensive documentation including field-level usage analytics by integrating with Apollo Studio reporting API, deprecated field tracking with sunset timelines, and interactive schema explorer HTML pages using GraphiQL or GraphQL Playground embedded builds.

Migration support includes automatic generation of schema migration scripts for Prisma, TypeORM, and Hasura when GraphQL schema changes require underlying database modifications. The skill also validates that resolver implementations match schema definitions by analyzing TypeScript type coverage.

Compatible with any GraphQL server implementation (Apollo, Yoga, Mercurius, Helix).

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/graphql-schema-registry
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/graphql-schema-registry` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-registry/)
