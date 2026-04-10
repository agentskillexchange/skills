---
name: "GraphQL Schema Registry Agent"
description: "Manages federated GraphQL schemas using Apollo Studio API and Hive Schema Registry. Validates schema composition, detects breaking changes, and enforces naming conventions across subgraph services."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/graphql-schema-registry-agent/"
category:
  - "Library &amp; API Reference"
framework:
  - "Codex"
---

# GraphQL Schema Registry Agent

The GraphQL Schema Registry Agent provides governance and lifecycle management for federated GraphQL architectures. It integrates with Apollo Studio's Schema Registry API and The Guild's Hive Schema Registry to validate, version, and publish subgraph schemas in Apollo Federation v2 environments.
Core capabilities include: composition validation that checks subgraph schemas for federation directive correctness (@key, @shareable, @external), breaking change detection that compares schema versions and categorizes field removals, type changes, and argument modifications by severity, and naming convention enforcement using configurable rules for types, fields, and enum values.
The agent supports schema proposal workflows where changes are validated in CI before merging, with detailed diff reports posted as GitHub PR comments. It can generate client-side operation documents from schema introspection, produce TypeScript types via GraphQL Code Generator, and maintain a schema changelog in Markdown format. Integration with Grafana allows visualization of schema evolution metrics, query complexity scores, and field usage analytics from Apollo Studio's operation traces.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-registry-agent/)
