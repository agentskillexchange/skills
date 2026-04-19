---
title: "API Documentation Indexer"
description: "The API Documentation Indexer processes OpenAPI 3.0 and Swagger 2.0 specifications to create comprehensive, searchable reference databases. Using swagger-parser for spec validation and dereferencing, it resolves all $ref pointers and builds complete endpoint documentation with full parameter and schema details. The agent creates search indexes with lunr.js, enabling instant full-text search across endpoint descriptions, parameter names, schema properties, and example values. It supports multi-spec indexing for microservice architectures, maintaining cross-references between related APIs and shared schema definitions. Advanced features include automated SDK usage example generation from endpoint specs, breaking change detection between API versions by diffing schemas, and interactive API exploration with parameter validation. The agent generates markdown reference guides organized by resource, tag, or authentication requirement, and creates dependency graphs showing which endpoints reference shared schemas. It also supports GraphQL schema indexing via introspection queries."
source: "https://agentskillexchange.com/skills/api-documentation-indexer/"
verification: "security_reviewed"
category:
  - "Library &amp; API Reference"
framework:
  - "Claude Code"
---

# API Documentation Indexer

The API Documentation Indexer processes OpenAPI 3.0 and Swagger 2.0 specifications to create comprehensive, searchable reference databases. Using swagger-parser for spec validation and dereferencing, it resolves all $ref pointers and builds complete endpoint documentation with full parameter and schema details. The agent creates search indexes with lunr.js, enabling instant full-text search across endpoint descriptions, parameter names, schema properties, and example values. It supports multi-spec indexing for microservice architectures, maintaining cross-references between related APIs and shared schema definitions. Advanced features include automated SDK usage example generation from endpoint specs, breaking change detection between API versions by diffing schemas, and interactive API exploration with parameter validation. The agent generates markdown reference guides organized by resource, tag, or authentication requirement, and creates dependency graphs showing which endpoints reference shared schemas. It also supports GraphQL schema indexing via introspection queries.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/api-documentation-indexer/)
