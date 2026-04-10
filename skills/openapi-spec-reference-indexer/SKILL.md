---
name: OpenAPI Spec Reference Indexer
description: Indexes and cross-references OpenAPI 3.x specifications using swagger-parser
  and Redocly CLI. Builds searchable endpoint catalogs with schema resolution, authentication
  flow mapping, and SDK generation metadata.
verification: security_reviewed
source: https://agentskillexchange.com/skills/openapi-spec-reference-indexer/
category:
- Library &amp; API Reference
framework:
- MCP
---
# OpenAPI Spec Reference Indexer

The OpenAPI Spec Reference Indexer skill processes OpenAPI 3.0 and 3.1 specification files to create comprehensive, searchable API reference indexes. It uses swagger-parser for spec validation and $ref resolution, and Redocly CLI for linting against configurable rulesets.
The skill parses paths, operations, and components to build a structured catalog of all endpoints with their request/response schemas fully dereferenced. It maps authentication flows including OAuth2 authorization_code, client_credentials, and API key schemes to each endpoint based on security requirement objects.
Advanced features include automatic SDK generation metadata extraction compatible with openapi-generator-cli, webhook endpoint documentation, discriminator-based polymorphism resolution, and link object traversal for API workflow documentation. The skill also detects breaking changes between spec versions by comparing path parameters, required fields, and enum values using oasdiff.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openapi-spec-reference-indexer/)
