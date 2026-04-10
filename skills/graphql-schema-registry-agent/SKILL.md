---
title: "GraphQL Schema Registry Agent"
description: "Manages federated GraphQL schemas using Apollo Studio API and Hive Schema Registry. Validates schema composition, detects breaking changes, and enforces naming conventions across subgraph services."
slug: "graphql-schema-registry-agent"
category:
  - "Library &amp; API Reference"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/graphql-schema-registry-agent/"
listed: true
---

# GraphQL Schema Registry Agent

Manages federated GraphQL schemas using Apollo Studio API and Hive Schema Registry. Validates schema composition, detects breaking changes, and enforces naming conventions across subgraph services.

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
clawhub install graphql-schema-registry-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The GraphQL Schema Registry Agent provides governance and lifecycle management for federated GraphQL architectures. It integrates with Apollo Studio’s Schema Registry API and The Guild’s Hive Schema Registry to validate, version, and publish subgraph schemas in Apollo Federation v2 environments.
Core capabilities include: composition validation that checks subgraph schemas for federation directive correctness (@key, @shareable, @external), breaking change detection that compares schema versions and categorizes field removals, type changes, and argument modifications by severity, and naming convention enforcement using configurable rules for types, fields, and enum values.
The agent supports schema proposal workflows where changes are validated in CI before merging, with detailed diff reports posted as GitHub PR comments. It can generate client-side operation documents from schema introspection, produce TypeScript types via GraphQL Code Generator, and maintain a schema changelog in Markdown format. Integration with Grafana allows visualization of schema evolution metrics, query complexity scores, and field usage analytics from Apollo Studio’s operation traces.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-registry-agent/)
