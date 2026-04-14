---
title: "GraphQL Introspection Documenter"
description: "Introspects GraphQL endpoints using the __schema query and generates structured API documentation. Uses graphql-js type system to resolve interfaces, unions, and custom scalar descriptions."
verification: security_reviewed
source: "https://github.com/graphql/graphql-js"
category:
  - "Library &amp; API Reference"
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-introspection-documenter/)
