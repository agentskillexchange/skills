---
title: GraphQL Schema Registry Client
description: The GraphQL Schema Registry Client skill manages GraphQL schema lifecycle
  through the Apollo Schema Registry API (Apollo Studio) and graphql-inspector CLI.
  It supports both monolithic and federated (Apollo Federation v2) GraphQL architectures
  with full schema versioning and compatibility checking. The skill pushes schema
  versions to Apollo Schema Registry using rover subgraph publish for federated subgraphs
  and rover graph publish for monolithic schemas. It performs pre-publish validation
  using graphql-inspector diff to detect breaking changes including removed fields,
  changed nullability, removed enum values, and modified input types. Each change
  is categorized by severity (breaking, dangerous, non-breaking). For federated architectures,
  the skill validates subgraph composition using rover supergraph compose, checking
  for entity reference resolution, key field compatibility, and @override directive
  correctness. It integrates with Apollo Schema Checks API for running composition
  and operation checks against real traffic data, ensuring that schema changes do
  not break existing client queries. The skill also generates schema changelogs and
  migration guides from diff outputs.
verification: security_reviewed
source: https://agentskillexchange.com/skills/graphql-schema-registry-client/
category:
- Library &amp; API Reference
framework:
- Custom Agents
---

# GraphQL Schema Registry Client

The GraphQL Schema Registry Client skill manages GraphQL schema lifecycle through the Apollo Schema Registry API (Apollo Studio) and graphql-inspector CLI. It supports both monolithic and federated (Apollo Federation v2) GraphQL architectures with full schema versioning and compatibility checking. The skill pushes schema versions to Apollo Schema Registry using rover subgraph publish for federated subgraphs and rover graph publish for monolithic schemas. It performs pre-publish validation using graphql-inspector diff to detect breaking changes including removed fields, changed nullability, removed enum values, and modified input types. Each change is categorized by severity (breaking, dangerous, non-breaking). For federated architectures, the skill validates subgraph composition using rover supergraph compose, checking for entity reference resolution, key field compatibility, and @override directive correctness. It integrates with Apollo Schema Checks API for running composition and operation checks against real traffic data, ensuring that schema changes do not break existing client queries. The skill also generates schema changelogs and migration guides from diff outputs.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-registry-client/)
