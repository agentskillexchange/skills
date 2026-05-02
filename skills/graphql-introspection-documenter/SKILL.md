---
title: "GraphQL Introspection Documenter"
description: "Introspects GraphQL endpoints using the __schema query and generates structured API documentation. Uses graphql-js type system to resolve interfaces, unions, and custom scalar descriptions."
verification: "security_reviewed"
source: "https://github.com/graphql/graphql-js"
category:
  - "Library & API Reference"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "graphql/graphql-js"
  github_stars: 20324
  npm_package: "graphql"
  npm_weekly_downloads: 34200861
---

# GraphQL Introspection Documenter

The GraphQL Introspection Documenter connects to any GraphQL endpoint and runs the full introspection query to extract the complete type system. Using the graphql-js reference implementation, it resolves complex type hierarchies including interfaces, unions, input objects, and custom scalars. The skill generates human-readable documentation with type relationships visualized as dependency graphs. It supports schema diffing between environments (staging vs production) to catch unintended type changes. Query complexity analysis estimates the cost of operations based on field resolver depth and list cardinality annotations. The skill handles federated schemas from Apollo Federation, merging subgraph types and identifying entity boundaries. Documentation output formats include Markdown, HTML with syntax highlighting, and structured JSON suitable for import into Postman or Insomnia collections. Deprecated field tracking with sunset dates helps API consumers plan migrations.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/graphql-introspection-documenter/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/graphql-introspection-documenter
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/graphql-introspection-documenter`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-introspection-documenter/)
