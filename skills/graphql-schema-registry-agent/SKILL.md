---
name: "GraphQL Schema Registry Agent"
description: "Manages federated GraphQL schemas using Apollo Studio API and Hive Schema Registry. Validates schema composition, detects breaking changes, and enforces naming conventions across subgraph services."
category: "Library & API Reference"
framework: "Codex"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/graphql-schema-registry-agent/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "graphql"  # from ase_tool_match
  github_stars: 20335  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 32010306  # from ase_npm_downloads
  github_repo: "graphql/graphql-js"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# GraphQL Schema Registry Agent

Manages federated GraphQL schemas using Apollo Studio API and Hive Schema Registry. Validates schema composition, detects breaking changes, and enforces naming conventions across subgraph services.

## Overview

The GraphQL Schema Registry Agent provides governance and lifecycle management for federated GraphQL architectures. It integrates with Apollo Studio’s Schema Registry API and The Guild’s Hive Schema Registry to validate, version, and publish subgraph schemas in Apollo Federation v2 environments.

Core capabilities include: composition validation that checks subgraph schemas for federation directive correctness (@key, @shareable, @external), breaking change detection that compares schema versions and categorizes field removals, type changes, and argument modifications by severity, and naming convention enforcement using configurable rules for types, fields, and enum values.

The agent supports schema proposal workflows where changes are validated in CI before merging, with detailed diff reports posted as GitHub PR comments. It can generate client-side operation documents from schema introspection, produce TypeScript types via GraphQL Code Generator, and maintain a schema changelog in Markdown format. Integration with Grafana allows visualization of schema evolution metrics, query complexity scores, and field usage analytics from Apollo Studio’s operation traces.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-registry-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-registry-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-registry-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill graphql-schema-registry-agent -a codex
```

### OpenClaw

```bash
clawhub install graphql-schema-registry-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/graphql-schema-registry-agent/
