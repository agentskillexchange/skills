---
name: "GraphQL Schema Registry Client"
description: "Manages GraphQL schema versions using Apollo Schema Registry API and graphql-inspector. Performs schema diffing, breaking change detection, and composition validation for federated GraphQL architectures."
category: "Library & API Reference"
framework: "Custom Agents"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/graphql-schema-registry-client/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "graphql"  # from ase_tool_match
  github_stars: 20332  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 32010306  # from ase_npm_downloads
  github_repo: "graphql/graphql-js"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# GraphQL Schema Registry Client

Manages GraphQL schema versions using Apollo Schema Registry API and graphql-inspector. Performs schema diffing, breaking change detection, and composition validation for federated GraphQL architectures.

## Overview

The GraphQL Schema Registry Client skill manages GraphQL schema lifecycle through the Apollo Schema Registry API (Apollo Studio) and graphql-inspector CLI. It supports both monolithic and federated (Apollo Federation v2) GraphQL architectures with full schema versioning and compatibility checking.

The skill pushes schema versions to Apollo Schema Registry using rover subgraph publish for federated subgraphs and rover graph publish for monolithic schemas. It performs pre-publish validation using graphql-inspector diff to detect breaking changes including removed fields, changed nullability, removed enum values, and modified input types. Each change is categorized by severity (breaking, dangerous, non-breaking).

For federated architectures, the skill validates subgraph composition using rover supergraph compose, checking for entity reference resolution, key field compatibility, and @override directive correctness. It integrates with Apollo Schema Checks API for running composition and operation checks against real traffic data, ensuring that schema changes do not break existing client queries. The skill also generates schema changelogs and migration guides from diff outputs.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-registry-client
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-registry-client -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-registry-client -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-registry-client -a codex
```

### OpenClaw

```bash
clawhub install graphql-schema-registry-client
```

## Source

- Marketplace: https://agentskillexchange.com/skills/graphql-schema-registry-client/
