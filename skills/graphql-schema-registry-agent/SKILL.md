---
title: "GraphQL Schema Registry Agent"
description: "Manages federated GraphQL schemas using Apollo Studio API and Hive Schema Registry. Validates schema composition, detects breaking changes, and enforces naming conventions across subgraph services."
verification: "security_reviewed"
source: "https://github.com/graphql/graphql-js"
category:
  - "Library &amp; API Reference"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "graphql/graphql-js"
  github_stars: 20324
  ase_npm_package: "graphql"
  npm_weekly_downloads: 34200861
  license: "MIT"
---

# GraphQL Schema Registry Agent

The GraphQL Schema Registry Agent provides governance and lifecycle management for federated GraphQL architectures. It integrates with Apollo Studio’s Schema Registry API and The Guild’s Hive Schema Registry to validate, version, and publish subgraph schemas in Apollo Federation v2 environments.

Core capabilities include: composition validation that checks subgraph schemas for federation directive correctness (@key, @shareable, @external), breaking change detection that compares schema versions and categorizes field removals, type changes, and argument modifications by severity, and naming convention enforcement using configurable rules for types, fields, and enum values.

The agent supports schema proposal workflows where changes are validated in CI before merging, with detailed diff reports posted as GitHub PR comments. It can generate client-side operation documents from schema introspection, produce TypeScript types via GraphQL Code Generator, and maintain a schema changelog in Markdown format. Integration with Grafana allows visualization of schema evolution metrics, query complexity scores, and field usage analytics from Apollo Studio’s operation traces.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-registry-agent/)
