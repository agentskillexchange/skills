---
title: API Documentation Indexer
description: The API Documentation Indexer processes OpenAPI 3.0 and Swagger 2.0 specifications
  to create comprehensive, searchable reference databases. Using swagger-parser for
  spec validation and dereferencing, it resolves all $ref pointers and builds complete
  endpoint documentation with full parameter and schema details. The agent creates
  search indexes with lunr.js, enabling instant full-text search across endpoint descriptions,
  parameter names, schema properties, and example values. It supports multi-spec indexing
  for microservice architectures, maintaining cross-references between related APIs
  and shared schema definitions. Advanced features include automated SDK usage example
  generation from endpoint specs, breaking change detection between API versions by
  diffing schemas, and interactive API exploration with parameter validation. The
  agent generates markdown reference guides organized by resource, tag, or authentication
  requirement, and creates dependency graphs showing which endpoints reference shared
  schemas. It also supports GraphQL schema indexing via introspection queries.
verification: security_reviewed
source: https://agentskillexchange.com/skills/api-documentation-indexer/
category:
- Library &amp; API Reference
framework:
- Claude Code
---

# API Documentation Indexer

The API Documentation Indexer processes OpenAPI 3.0 and Swagger 2.0 specifications to create comprehensive, searchable reference databases. Using swagger-parser for spec validation and dereferencing, it resolves all $ref pointers and builds complete endpoint documentation with full parameter and schema details. The agent creates search indexes with lunr.js, enabling instant full-text search across endpoint descriptions, parameter names, schema properties, and example values. It supports multi-spec indexing for microservice architectures, maintaining cross-references between related APIs and shared schema definitions. Advanced features include automated SDK usage example generation from endpoint specs, breaking change detection between API versions by diffing schemas, and interactive API exploration with parameter validation. The agent generates markdown reference guides organized by resource, tag, or authentication requirement, and creates dependency graphs showing which endpoints reference shared schemas. It also supports GraphQL schema indexing via introspection queries.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/api-documentation-indexer/)
