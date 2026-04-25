---
title: "OpenAPI Spec Reference Indexer"
description: "Indexes and cross-references OpenAPI 3.x specifications using swagger-parser and Redocly CLI. Builds searchable endpoint catalogs with schema resolution, authentication flow mapping, and SDK generation metadata."
verification: "security_reviewed"
source: "https://swagger.io/docs/"
category:
  - "Library & API Reference"
framework:
  - "MCP"
---

# OpenAPI Spec Reference Indexer

The OpenAPI Spec Reference Indexer skill processes OpenAPI 3.0 and 3.1 specification files to create comprehensive, searchable API reference indexes. It uses swagger-parser for spec validation and $ref resolution, and Redocly CLI for linting against configurable rulesets.

The skill parses paths, operations, and components to build a structured catalog of all endpoints with their request/response schemas fully dereferenced. It maps authentication flows including OAuth2 authorization_code, client_credentials, and API key schemes to each endpoint based on security requirement objects.

Advanced features include automatic SDK generation metadata extraction compatible with openapi-generator-cli, webhook endpoint documentation, discriminator-based polymorphism resolution, and link object traversal for API workflow documentation. The skill also detects breaking changes between spec versions by comparing path parameters, required fields, and enum values using oasdiff.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/openapi-spec-reference-indexer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/openapi-spec-reference-indexer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/openapi-spec-reference-indexer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openapi-spec-reference-indexer/)
