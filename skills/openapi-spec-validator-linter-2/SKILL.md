---
name: "OpenAPI Spec Validator & Linter"
description: "Validates OpenAPI 3.0/3.1 specifications using the @readme/openapi-parser and Spectral linter with custom rulesets. Detects missing descriptions, inconsistent naming conventions, and security scheme gaps in your API definitions."
category: "Library & API Reference"
framework: "Custom Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/openapi-spec-validator-linter-2/"
---
# OpenAPI Spec Validator & Linter

Validates OpenAPI 3.0/3.1 specifications using the @readme/openapi-parser and Spectral linter with custom rulesets. Detects missing descriptions, inconsistent naming conventions, and security scheme gaps in your API definitions.

## Overview

The OpenAPI Spec Validator & Linter skill provides comprehensive validation and linting for OpenAPI specifications. It uses @readme/openapi-parser for structural validation against the OpenAPI 3.0.x and 3.1.x JSON Schema, and Stoplight Spectral (@stoplight/spectral-core) for style and best-practice linting.

Structural validation catches: invalid $ref pointers, missing required fields (info, paths, responses), malformed schema compositions (allOf/oneOf/anyOf cycles), and discriminator mapping errors. The parser resolves external references and detects circular dependencies.

Spectral linting applies configurable rulesets including: oas3-api-servers (server URL validation), operation-description (missing endpoint docs), operation-operationId-valid-in-url (naming conventions), no-$ref-siblings (spec compliance), and typed-enum (enum value consistency). Custom rules detect company-specific patterns like missing rate-limit headers, inconsistent pagination parameters, and non-standard error response schemas.

The skill generates a prioritized report with: critical errors blocking code generation, warnings affecting developer experience, informational suggestions for API consistency, and auto-fix suggestions for common issues like adding missing operationIds or normalizing path parameter naming from camelCase to snake_case.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill openapi-spec-validator-linter-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill openapi-spec-validator-linter-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill openapi-spec-validator-linter-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill openapi-spec-validator-linter-2 -a codex
```

### OpenClaw

```bash
clawhub install openapi-spec-validator-linter-2
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openapi-spec-validator-linter-2/)
