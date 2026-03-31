---
name: "API Documentation Indexer"
description: "Indexes and searches API documentation from OpenAPI 3.0 specs using swagger-parser and lunr.js. Builds searchable indexes of endpoints, parameters, and response schemas for quick reference."
category: "Library &amp; API Reference"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/api-documentation-indexer/"
---
# API Documentation Indexer

Indexes and searches API documentation from OpenAPI 3.0 specs using swagger-parser and lunr.js. Builds searchable indexes of endpoints, parameters, and response schemas for quick reference.

## Overview

The API Documentation Indexer processes OpenAPI 3.0 and Swagger 2.0 specifications to create comprehensive, searchable reference databases. Using swagger-parser for spec validation and dereferencing, it resolves all $ref pointers and builds complete endpoint documentation with full parameter and schema details.

The agent creates search indexes with lunr.js, enabling instant full-text search across endpoint descriptions, parameter names, schema properties, and example values. It supports multi-spec indexing for microservice architectures, maintaining cross-references between related APIs and shared schema definitions.

Advanced features include automated SDK usage example generation from endpoint specs, breaking change detection between API versions by diffing schemas, and interactive API exploration with parameter validation. The agent generates markdown reference guides organized by resource, tag, or authentication requirement, and creates dependency graphs showing which endpoints reference shared schemas. It also supports GraphQL schema indexing via introspection queries.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill api-documentation-indexer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill api-documentation-indexer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill api-documentation-indexer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill api-documentation-indexer -a codex
```

### OpenClaw

```bash
clawhub install api-documentation-indexer
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/api-documentation-indexer/)
