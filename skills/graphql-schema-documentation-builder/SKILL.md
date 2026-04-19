---
title: "GraphQL Schema Documentation Builder"
description: "The GraphQL Schema Documentation Builder skill transforms GraphQL Schema Definition Language files into comprehensive API documentation. It uses graphql-js introspection queries to extract the full type system including objects, interfaces, unions, enums, and input types with their field-level descriptions. The skill integrates with SpectaQL for static documentation site generation and graphql-voyager for interactive schema visualization. It parses SDL files to detect @deprecated directives and generates migration guides for deprecated fields with suggested alternatives. Key features include automatic query and mutation example generation with realistic fake data using faker.js, subscription documentation with WebSocket connection details, custom scalar documentation extraction, and relay-style pagination pattern detection. The skill also validates schemas against best practices including the Shopify GraphQL Design Tutorial guidelines and generates TypeScript type definitions using graphql-codegen for client SDK documentation."
source: "https://github.com/graphql/graphql-js"
verification: "security_reviewed"
category:
  - "Library &amp; API Reference"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "graphql/graphql-js"
  github_stars: 20324
  npm_package: "graphql"
  npm_weekly_downloads: 34200861
---

# GraphQL Schema Documentation Builder

The GraphQL Schema Documentation Builder skill transforms GraphQL Schema Definition Language files into comprehensive API documentation. It uses graphql-js introspection queries to extract the full type system including objects, interfaces, unions, enums, and input types with their field-level descriptions. The skill integrates with SpectaQL for static documentation site generation and graphql-voyager for interactive schema visualization. It parses SDL files to detect @deprecated directives and generates migration guides for deprecated fields with suggested alternatives. Key features include automatic query and mutation example generation with realistic fake data using faker.js, subscription documentation with WebSocket connection details, custom scalar documentation extraction, and relay-style pagination pattern detection. The skill also validates schemas against best practices including the Shopify GraphQL Design Tutorial guidelines and generates TypeScript type definitions using graphql-codegen for client SDK documentation.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/graphql-schema-documentation-builder/)
