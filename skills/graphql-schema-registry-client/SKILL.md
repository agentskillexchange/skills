---
title: "GraphQL Schema Registry Client"
description: "The GraphQL Schema Registry Client skill manages GraphQL schema lifecycle through the Apollo Schema Registry API (Apollo Studio) and graphql-inspector CLI. It supports both monolithic and federated (Apollo Federation v2) GraphQL architectures with full schema versioning and compatibility checking.\nThe skill pushes schema versions to Apollo Schema Registry using rover subgraph publish for federated subgraphs and rover graph publish for monolithic schemas. It performs pre-publish validation using graphql-inspector diff to detect breaking changes including removed fields, changed nullability, removed enum values, and modified input types. Each change is categorized by severity (breaking, dangerous, non-breaking).\nFor federated architectures, the skill validates subgraph composition using rover supergraph compose, checking for entity reference resolution, key field compatibility, and @override directive correctness. It integrates with Apollo Schema Checks API for running composition and operation checks against real traffic data, ensuring that schema changes do not break existing client queries. The skill also generates schema changelogs and migration guides from diff outputs."
verification: security_reviewed
source: "https://github.com/graphql/graphql-js"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "graphql/graphql-js"
  github_stars: 20324
  ase_npm_package: "graphql"
  npm_weekly_downloads: 34200861
---

# GraphQL Schema Registry Client

The GraphQL Schema Registry Client skill manages GraphQL schema lifecycle through the Apollo Schema Registry API (Apollo Studio) and graphql-inspector CLI. It supports both monolithic and federated (Apollo Federation v2) GraphQL architectures with full schema versioning and compatibility checking.
The skill pushes schema versions to Apollo Schema Registry using rover subgraph publish for federated subgraphs and rover graph publish for monolithic schemas. It performs pre-publish validation using graphql-inspector diff to detect breaking changes including removed fields, changed nullability, removed enum values, and modified input types. Each change is categorized by severity (breaking, dangerous, non-breaking).
For federated architectures, the skill validates subgraph composition using rover supergraph compose, checking for entity reference resolution, key field compatibility, and @override directive correctness. It integrates with Apollo Schema Checks API for running composition and operation checks against real traffic data, ensuring that schema changes do not break existing client queries. The skill also generates schema changelogs and migration guides from diff outputs.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/graphql-schema-registry-client
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/graphql-schema-registry-client` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-registry-client/)
