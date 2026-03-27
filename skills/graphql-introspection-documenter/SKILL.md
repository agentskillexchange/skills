---
name: "GraphQL Introspection Documenter"
description: "Introspects GraphQL endpoints using the __schema query and generates structured API documentation. Uses graphql-js type system to resolve interfaces, unions, and custom scalar descriptions."
category: "Library & API Reference"
framework: "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/graphql-introspection-documenter/"
tool_ecosystem:
  tool: graphql
  github_stars: 20332
  npm_weekly_downloads: 32010306
  github_repo: graphql/graphql-js
  license: MIT
  maintained: true
---

# GraphQL Introspection Documenter

Introspects GraphQL endpoints using the __schema query and generates structured API documentation. Uses graphql-js type system to resolve interfaces, unions, and custom scalar descriptions.

## Overview

The GraphQL Introspection Documenter connects to any GraphQL endpoint and runs the full introspection query to extract the complete type system. Using the graphql-js reference implementation, it resolves complex type hierarchies including interfaces, unions, input objects, and custom scalars. The skill generates human-readable documentation with type relationships visualized as dependency graphs. It supports schema diffing between environments (staging vs production) to catch unintended type changes. Query complexity analysis estimates the cost of operations based on field resolver depth and list cardinality annotations. The skill handles federated schemas from Apollo Federation, merging subgraph types and identifying entity boundaries. Documentation output formats include Markdown, HTML with syntax highlighting, and structured JSON suitable for import into Postman or Insomnia collections. Deprecated field tracking with sunset dates helps API consumers plan migrations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill graphql-introspection-documenter
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill graphql-introspection-documenter -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill graphql-introspection-documenter -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill graphql-introspection-documenter -a codex
```

### OpenClaw

```bash
clawhub install graphql-introspection-documenter
```

## Source

- Marketplace: https://agentskillexchange.com/skills/graphql-introspection-documenter/
