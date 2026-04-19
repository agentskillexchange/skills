---
title: "GraphQL Schema Registry Agent"
description: "The GraphQL Schema Registry Agent provides governance and lifecycle management for federated GraphQL architectures. It integrates with Apollo Studio&#8217;s Schema Registry API and The Guild&#8217;s Hive Schema Registry to validate, version, and publish subgraph schemas in Apollo Federation v2 environments. Core capabilities include: composition validation that checks subgraph schemas for federation directive correctness (@key, @shareable, @external), breaking change detection that compares schema versions and categorizes field removals, type changes, and argument modifications by severity, and naming convention enforcement using configurable rules for types, fields, and enum values. The agent supports schema proposal workflows where changes are validated in CI before merging, with detailed diff reports posted as GitHub PR comments. It can generate client-side operation documents from schema introspection, produce TypeScript types via GraphQL Code Generator, and maintain a schema changelog in Markdown format. Integration with Grafana allows visualization of schema evolution metrics, query complexity scores, and field usage analytics from Apollo Studio&#8217;s operation traces."
source: "https://github.com/graphql/graphql-js"
verification: "security_reviewed"
category:
  - "Library &amp; API Reference"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "graphql/graphql-js"
  github_stars: 20324
  npm_package: "graphql"
  npm_weekly_downloads: 34200861
---

# GraphQL Schema Registry Agent

The GraphQL Schema Registry Agent provides governance and lifecycle management for federated GraphQL architectures. It integrates with Apollo Studio&#8217;s Schema Registry API and The Guild&#8217;s Hive Schema Registry to validate, version, and publish subgraph schemas in Apollo Federation v2 environments. Core capabilities include: composition validation that checks subgraph schemas for federation directive correctness (@key, @shareable, @external), breaking change detection that compares schema versions and categorizes field removals, type changes, and argument modifications by severity, and naming convention enforcement using configurable rules for types, fields, and enum values. The agent supports schema proposal workflows where changes are validated in CI before merging, with detailed diff reports posted as GitHub PR comments. It can generate client-side operation documents from schema introspection, produce TypeScript types via GraphQL Code Generator, and maintain a schema changelog in Markdown format. Integration with Grafana allows visualization of schema evolution metrics, query complexity scores, and field usage analytics from Apollo Studio&#8217;s operation traces.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-registry-agent/)
