---
title: "GraphQL Introspection Documenter"
description: "Introspects GraphQL endpoints using the __schema query and generates structured API documentation. Uses graphql-js type system to resolve interfaces, unions, and custom scalar descriptions."
slug: "graphql-introspection-documenter"
category:
  - "Library &amp; API Reference"
framework:
  - "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/graphql-introspection-documenter/"
listed: true
---

# GraphQL Introspection Documenter

Introspects GraphQL endpoints using the __schema query and generates structured API documentation. Uses graphql-js type system to resolve interfaces, unions, and custom scalar descriptions.

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
clawhub install graphql-introspection-documenter
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The GraphQL Introspection Documenter connects to any GraphQL endpoint and runs the full introspection query to extract the complete type system. Using the graphql-js reference implementation, it resolves complex type hierarchies including interfaces, unions, input objects, and custom scalars. The skill generates human-readable documentation with type relationships visualized as dependency graphs. It supports schema diffing between environments (staging vs production) to catch unintended type changes. Query complexity analysis estimates the cost of operations based on field resolver depth and list cardinality annotations. The skill handles federated schemas from Apollo Federation, merging subgraph types and identifying entity boundaries. Documentation output formats include Markdown, HTML with syntax highlighting, and structured JSON suitable for import into Postman or Insomnia collections. Deprecated field tracking with sunset dates helps API consumers plan migrations.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-introspection-documenter/)
