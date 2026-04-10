---
title: "OpenAPI Spec Validator & Linter"
description: "Validates OpenAPI 3.0/3.1 specifications using the @readme/openapi-parser and Spectral linter with custom rulesets. Detects missing descriptions, inconsistent naming conventions, and security scheme gaps in your API definitions."
slug: "openapi-spec-validator-linter-2"
category:
  - "Library &amp; API Reference"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/openapi-spec-validator-linter-2/"
listed: true
---

# OpenAPI Spec Validator & Linter

Validates OpenAPI 3.0/3.1 specifications using the @readme/openapi-parser and Spectral linter with custom rulesets. Detects missing descriptions, inconsistent naming conventions, and security scheme gaps in your API definitions.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install openapi-spec-validator-linter-2
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The OpenAPI Spec Validator & Linter skill provides comprehensive validation and linting for OpenAPI specifications. It uses @readme/openapi-parser for structural validation against the OpenAPI 3.0.x and 3.1.x JSON Schema, and Stoplight Spectral (@stoplight/spectral-core) for style and best-practice linting.
Structural validation catches: invalid $ref pointers, missing required fields (info, paths, responses), malformed schema compositions (allOf/oneOf/anyOf cycles), and discriminator mapping errors. The parser resolves external references and detects circular dependencies.
Spectral linting applies configurable rulesets including: oas3-api-servers (server URL validation), operation-description (missing endpoint docs), operation-operationId-valid-in-url (naming conventions), no-$ref-siblings (spec compliance), and typed-enum (enum value consistency). Custom rules detect company-specific patterns like missing rate-limit headers, inconsistent pagination parameters, and non-standard error response schemas.
The skill generates a prioritized report with: critical errors blocking code generation, warnings affecting developer experience, informational suggestions for API consistency, and auto-fix suggestions for common issues like adding missing operationIds or normalizing path parameter naming from camelCase to snake_case.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openapi-spec-validator-linter-2/)
