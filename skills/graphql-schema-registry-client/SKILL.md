---
title: "GraphQL Schema Registry Client"
description: "Manages GraphQL schema versions using Apollo Schema Registry API and graphql-inspector. Performs schema diffing, breaking change detection, and composition validation for federated GraphQL architectures."
verification: security_reviewed
source: "https://github.com/graphql/graphql-js"
category:
  - "Library &amp; API Reference"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "graphql/graphql-js"
  github_stars: 20324
  npm_package: "graphql"
  npm_weekly_downloads: 34200861
---

# GraphQL Schema Registry Client

The GraphQL Schema Registry Client skill manages GraphQL schema lifecycle through the Apollo Schema Registry API (Apollo Studio) and graphql-inspector CLI. It supports both monolithic and federated (Apollo Federation v2) GraphQL architectures with full schema versioning and compatibility checking.

The skill pushes schema versions to Apollo Schema Registry using rover subgraph publish for federated subgraphs and rover graph publish for monolithic schemas. It performs pre-publish validation using graphql-inspector diff to detect breaking changes including removed fields, changed nullability, removed enum values, and modified input types. Each change is categorized by severity (breaking, dangerous, non-breaking).

For federated architectures, the skill validates subgraph composition using rover supergraph compose, checking for entity reference resolution, key field compatibility, and @override directive correctness. It integrates with Apollo Schema Checks API for running composition and operation checks against real traffic data, ensuring that schema changes do not break existing client queries. The skill also generates schema changelogs and migration guides from diff outputs.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-registry-client/)
