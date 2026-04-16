---
title: "OpenAPI Spec Validator & Linter"
description: "Validates OpenAPI 3.0/3.1 specifications using the @readme/openapi-parser and Spectral linter with custom rulesets. Detects missing descriptions, inconsistent naming conventions, and security scheme gaps in your API definitions."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/openapi-spec-validator-linter-2/"
category:
  - "Library & API Reference"
framework:
  - "Custom Agents"
---

# OpenAPI Spec Validator & Linter

The OpenAPI Spec Validator & Linter skill provides comprehensive validation and linting for OpenAPI specifications. It uses @readme/openapi-parser for structural validation against the OpenAPI 3.0.x and 3.1.x JSON Schema, and Stoplight Spectral (@stoplight/spectral-core) for style and best-practice linting.


Structural validation catches: invalid $ref pointers, missing required fields (info, paths, responses), malformed schema compositions (allOf/oneOf/anyOf cycles), and discriminator mapping errors. The parser resolves external references and detects circular dependencies.


Spectral linting applies configurable rulesets including: oas3-api-servers (server URL validation), operation-description (missing endpoint docs), operation-operationId-valid-in-url (naming conventions), no-$ref-siblings (spec compliance), and typed-enum (enum value consistency). Custom rules detect company-specific patterns like missing rate-limit headers, inconsistent pagination parameters, and non-standard error response schemas.


The skill generates a prioritized report with: critical errors blocking code generation, warnings affecting developer experience, informational suggestions for API consistency, and auto-fix suggestions for common issues like adding missing operationIds or normalizing path parameter naming from camelCase to snake_case.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openapi-spec-validator-linter-2/)
