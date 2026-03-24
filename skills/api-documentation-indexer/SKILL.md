---
name: "API Documentation Indexer"
description: "Indexes and searches API documentation from OpenAPI 3.0 specs using swagger-parser and lunr.js. Builds searchable indexes of endpoints, parameters, and response schemas for quick reference."
category: "Library & API Reference"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/api-documentation-indexer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "swagger"  # from ase_tool_match
  github_stars: 28702  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 3219093  # from ase_npm_downloads
  github_repo: "swagger-api/swagger-ui"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
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

- Marketplace: https://agentskillexchange.com/skills/api-documentation-indexer/
