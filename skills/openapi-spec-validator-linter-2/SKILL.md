---
title: OpenAPI Spec Validator & Linter
description: 'The OpenAPI Spec Validator & Linter skill provides comprehensive validation
  and linting for OpenAPI specifications. It uses @readme/openapi-parser for structural
  validation against the OpenAPI 3.0.x and 3.1.x JSON Schema, and Stoplight Spectral
  (@stoplight/spectral-core) for style and best-practice linting. Structural validation
  catches: invalid $ref pointers, missing required fields (info, paths, responses),
  malformed schema compositions (allOf/oneOf/anyOf cycles), and discriminator mapping
  errors. The parser resolves external references and detects circular dependencies.
  Spectral linting applies configurable rulesets including: oas3-api-servers (server
  URL validation), operation-description (missing endpoint docs), operation-operationId-valid-in-url
  (naming conventions), no-$ref-siblings (spec compliance), and typed-enum (enum value
  consistency). Custom rules detect company-specific patterns like missing rate-limit
  headers, inconsistent pagination parameters, and non-standard error response schemas.
  The skill generates a prioritized report with: critical errors blocking code generation,
  warnings affecting developer experience, informational suggestions for API consistency,
  and auto-fix suggestions for common issues like adding missing operationIds or normalizing
  path parameter naming from camelCase to snake_case.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/openapi-spec-validator-linter-2/
category:
- Library &amp; API Reference
framework:
- Custom Agents
---

# OpenAPI Spec Validator & Linter

The OpenAPI Spec Validator & Linter skill provides comprehensive validation and linting for OpenAPI specifications. It uses @readme/openapi-parser for structural validation against the OpenAPI 3.0.x and 3.1.x JSON Schema, and Stoplight Spectral (@stoplight/spectral-core) for style and best-practice linting. Structural validation catches: invalid $ref pointers, missing required fields (info, paths, responses), malformed schema compositions (allOf/oneOf/anyOf cycles), and discriminator mapping errors. The parser resolves external references and detects circular dependencies. Spectral linting applies configurable rulesets including: oas3-api-servers (server URL validation), operation-description (missing endpoint docs), operation-operationId-valid-in-url (naming conventions), no-$ref-siblings (spec compliance), and typed-enum (enum value consistency). Custom rules detect company-specific patterns like missing rate-limit headers, inconsistent pagination parameters, and non-standard error response schemas. The skill generates a prioritized report with: critical errors blocking code generation, warnings affecting developer experience, informational suggestions for API consistency, and auto-fix suggestions for common issues like adding missing operationIds or normalizing path parameter naming from camelCase to snake_case.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openapi-spec-validator-linter-2/)
