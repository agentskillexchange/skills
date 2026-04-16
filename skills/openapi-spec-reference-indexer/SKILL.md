---
title: "OpenAPI Spec Reference Indexer"
description: "Indexes and cross-references OpenAPI 3.x specifications using swagger-parser and Redocly CLI. Builds searchable endpoint catalogs with schema resolution, authentication flow mapping, and SDK generation metadata."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/openapi-spec-reference-indexer/"
category:
  - "Library &amp; API Reference"
framework:
  - "MCP"
---

# OpenAPI Spec Reference Indexer

The OpenAPI Spec Reference Indexer skill processes OpenAPI 3.0 and 3.1 specification files to create comprehensive, searchable API reference indexes. It uses swagger-parser for spec validation and $ref resolution, and Redocly CLI for linting against configurable rulesets.

The skill parses paths, operations, and components to build a structured catalog of all endpoints with their request/response schemas fully dereferenced. It maps authentication flows including OAuth2 authorization_code, client_credentials, and API key schemes to each endpoint based on security requirement objects.

Advanced features include automatic SDK generation metadata extraction compatible with openapi-generator-cli, webhook endpoint documentation, discriminator-based polymorphism resolution, and link object traversal for API workflow documentation. The skill also detects breaking changes between spec versions by comparing path parameters, required fields, and enum values using oasdiff.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openapi-spec-reference-indexer/)
