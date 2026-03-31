---
name: "GraphQL Schema Registry"
description: "Manages GraphQL schema evolution using graphql-inspector for breaking change detection and Apollo Rover CLI for schema composition. Validates schemas against custom ESLint rules via @graphql-eslint/eslint-plugin."
category: "Library &amp; API Reference"
framework: "Claude Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/graphql-schema-registry/"
---
# GraphQL Schema Registry

Manages GraphQL schema evolution using graphql-inspector for breaking change detection and Apollo Rover CLI for schema composition. Validates schemas against custom ESLint rules via @graphql-eslint/eslint-plugin.

## Overview

The GraphQL Schema Registry skill provides schema lifecycle management for GraphQL APIs, handling validation, evolution tracking, and federated composition. It uses graphql-inspector to compare schema versions and detect breaking changes including removed fields, changed argument types, and modified enum values.

For federated architectures, the skill leverages Apollo Rover CLI (rover supergraph compose) to compose subgraph schemas into a unified supergraph, validating that all entity references resolve correctly and that no naming conflicts exist across subgraphs. It supports both Apollo Federation v1 and v2 directives.

Schema quality is enforced through @graphql-eslint/eslint-plugin with configurable rule sets covering naming conventions (camelCase fields, PascalCase types), description requirements for public-facing fields, depth limiting rules to prevent abuse, and relay-style connection pagination patterns.

The skill generates comprehensive documentation including field-level usage analytics by integrating with Apollo Studio reporting API, deprecated field tracking with sunset timelines, and interactive schema explorer HTML pages using GraphiQL or GraphQL Playground embedded builds.

Migration support includes automatic generation of schema migration scripts for Prisma, TypeORM, and Hasura when GraphQL schema changes require underlying database modifications. The skill also validates that resolver implementations match schema definitions by analyzing TypeScript type coverage.

Compatible with any GraphQL server implementation (Apollo, Yoga, Mercurius, Helix).

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-registry
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-registry -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-registry -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-registry -a codex
```

### OpenClaw

```bash
clawhub install graphql-schema-registry
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-registry/)
