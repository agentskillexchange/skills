---
title: "GraphQL Schema Registry Client"
description: "Manages GraphQL schema versions using Apollo Schema Registry API and graphql-inspector. Performs schema diffing, breaking change detection, and composition validation for federated GraphQL architectures."
slug: "graphql-schema-registry-client"
category:
  - "Library &amp; API Reference"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/graphql-schema-registry-client/"
---

# GraphQL Schema Registry Client

Manages GraphQL schema versions using Apollo Schema Registry API and graphql-inspector. Performs schema diffing, breaking change detection, and composition validation for federated GraphQL architectures.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install graphql-schema-registry-client
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The GraphQL Schema Registry Client skill manages GraphQL schema lifecycle through the Apollo Schema Registry API (Apollo Studio) and graphql-inspector CLI. It supports both monolithic and federated (Apollo Federation v2) GraphQL architectures with full schema versioning and compatibility checking.
The skill pushes schema versions to Apollo Schema Registry using rover subgraph publish for federated subgraphs and rover graph publish for monolithic schemas. It performs pre-publish validation using graphql-inspector diff to detect breaking changes including removed fields, changed nullability, removed enum values, and modified input types. Each change is categorized by severity (breaking, dangerous, non-breaking).
For federated architectures, the skill validates subgraph composition using rover supergraph compose, checking for entity reference resolution, key field compatibility, and @override directive correctness. It integrates with Apollo Schema Checks API for running composition and operation checks against real traffic data, ensuring that schema changes do not break existing client queries. The skill also generates schema changelogs and migration guides from diff outputs.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-registry-client/)
