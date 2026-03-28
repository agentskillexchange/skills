---
name: "Swagger OpenAPI Schema Validator"
description: "Validates and lints OpenAPI 3.1 specifications using Spectral ruleset engine and swagger-parser. Detects breaking changes between API versions using oasdiff comparison tool."
category: "Library & API Reference"
framework: "Cursor"
verification: security_reviewed
source: "https://github.com/swagger-api/swagger-ui"
tool_ecosystem:
  tool: swagger
  github_stars: 28703
  npm_weekly_downloads: 3219093
  github_repo: swagger-api/swagger-ui
  license: Apache-2.0
  maintained: true
---

# Swagger OpenAPI Schema Validator

Validates and lints OpenAPI 3.1 specifications using Spectral ruleset engine and swagger-parser. Detects breaking changes between API versions using oasdiff comparison tool.

## Overview

The Swagger OpenAPI Schema Validator performs comprehensive validation of OpenAPI 3.0 and 3.1 specifications using the Spectral linting engine from Stoplight. It applies customizable rulesets covering naming conventions, security scheme requirements, pagination patterns, and error response schemas. The skill integrates swagger-parser for deep JSON Schema validation including $ref resolution across multi-file specifications. Breaking change detection uses oasdiff to compare two API versions, flagging removed endpoints, changed parameter types, narrowed enum values, and modified required fields. It generates detailed compatibility reports following semver conventions. The skill also validates example values against their schemas, checks for unused components, and ensures consistent use of tags and operationIds. Output includes a severity-ranked issue list with line numbers and fix suggestions, making it essential for API-first development workflows.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill swagger-openapi-schema-validator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill swagger-openapi-schema-validator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill swagger-openapi-schema-validator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill swagger-openapi-schema-validator -a codex
```

### OpenClaw

```bash
clawhub install swagger-openapi-schema-validator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/swagger-openapi-schema-validator/
