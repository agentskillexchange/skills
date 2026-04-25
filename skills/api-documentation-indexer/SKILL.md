---
title: "API Documentation Indexer"
description: "Indexes and searches API documentation from OpenAPI 3.0 specs using swagger-parser and lunr.js. Builds searchable indexes of endpoints, parameters, and response schemas for quick reference."
verification: "security_reviewed"
source: "https://swagger.io/docs/"
category:
  - "Library & API Reference"
framework:
  - "Claude Code"
---

# API Documentation Indexer

The API Documentation Indexer processes OpenAPI 3.0 and Swagger 2.0 specifications to create comprehensive, searchable reference databases. Using swagger-parser for spec validation and dereferencing, it resolves all $ref pointers and builds complete endpoint documentation with full parameter and schema details. The agent creates search indexes with lunr.js, enabling instant full-text search across endpoint descriptions, parameter names, schema properties, and example values. It supports multi-spec indexing for microservice architectures, maintaining cross-references between related APIs and shared schema definitions. Advanced features include automated SDK usage example generation from endpoint specs, breaking change detection between API versions by diffing schemas, and interactive API exploration with parameter validation. The agent generates markdown reference guides organized by resource, tag, or authentication requirement, and creates dependency graphs showing which endpoints reference shared schemas. It also supports GraphQL schema indexing via introspection queries.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/api-documentation-indexer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/api-documentation-indexer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/api-documentation-indexer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/api-documentation-indexer/)
