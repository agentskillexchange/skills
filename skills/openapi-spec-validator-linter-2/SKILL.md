---
title: "OpenAPI Spec Validator & Linter"
description: "Validates OpenAPI 3.0/3.1 specifications using the @readme/openapi-parser and Spectral linter with custom rulesets. Detects missing descriptions, inconsistent naming conventions, and security scheme gaps in your API definitions."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/openapi-spec-validator-linter-2/"
category:
  - "Library &amp; API Reference"
framework:
  - "Custom Agents"
---

# OpenAPI Spec Validator & Linter

The OpenAPI Spec Validator & Linter skill provides comprehensive validation and linting for OpenAPI specifications. It uses @readme/openapi-parser for structural validation against the OpenAPI 3.0.x and 3.1.x JSON Schema, and Stoplight Spectral (@stoplight/spectral-core) for style and best-practice linting.

Structural validation catches: invalid $ref pointers, missing required fields (info, paths, responses), malformed schema compositions (allOf/oneOf/anyOf cycles), and discriminator mapping errors. The parser resolves external references and detects circular dependencies.

Spectral linting applies configurable rulesets including: oas3-api-servers (server URL validation), operation-description (missing endpoint docs), operation-operationId-valid-in-url (naming conventions), no-$ref-siblings (spec compliance), and typed-enum (enum value consistency). Custom rules detect company-specific patterns like missing rate-limit headers, inconsistent pagination parameters, and non-standard error response schemas.

The skill generates a prioritized report with: critical errors blocking code generation, warnings affecting developer experience, informational suggestions for API consistency, and auto-fix suggestions for common issues like adding missing operationIds or normalizing path parameter naming from camelCase to snake_case.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openapi-spec-validator-linter-2/)
