---
title: GraphQL Introspection Documenter
description: The GraphQL Introspection Documenter connects to any GraphQL endpoint
  and runs the full introspection query to extract the complete type system. Using
  the graphql-js reference implementation, it resolves complex type hierarchies including
  interfaces, unions, input objects, and custom scalars. The skill generates human-readable
  documentation with type relationships visualized as dependency graphs. It supports
  schema diffing between environments (staging vs production) to catch unintended
  type changes. Query complexity analysis estimates the cost of operations based on
  field resolver depth and list cardinality annotations. The skill handles federated
  schemas from Apollo Federation, merging subgraph types and identifying entity boundaries.
  Documentation output formats include Markdown, HTML with syntax highlighting, and
  structured JSON suitable for import into Postman or Insomnia collections. Deprecated
  field tracking with sunset dates helps API consumers plan migrations.
verification: security_reviewed
source: https://agentskillexchange.com/skills/graphql-introspection-documenter/
category:
- Library &amp; API Reference
framework:
- Claude Agents
---

# GraphQL Introspection Documenter

The GraphQL Introspection Documenter connects to any GraphQL endpoint and runs the full introspection query to extract the complete type system. Using the graphql-js reference implementation, it resolves complex type hierarchies including interfaces, unions, input objects, and custom scalars. The skill generates human-readable documentation with type relationships visualized as dependency graphs. It supports schema diffing between environments (staging vs production) to catch unintended type changes. Query complexity analysis estimates the cost of operations based on field resolver depth and list cardinality annotations. The skill handles federated schemas from Apollo Federation, merging subgraph types and identifying entity boundaries. Documentation output formats include Markdown, HTML with syntax highlighting, and structured JSON suitable for import into Postman or Insomnia collections. Deprecated field tracking with sunset dates helps API consumers plan migrations.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-introspection-documenter/)
