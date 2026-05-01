---
title: "Swagger OpenAPI Schema Validator"
description: "Validates and lints OpenAPI 3.1 specifications using Spectral ruleset engine and swagger-parser. Detects breaking changes between API versions using oasdiff comparison tool."
verification: "security_reviewed"
source: "https://github.com/swagger-api/swagger-ui"
category:
  - "Library & API Reference"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "swagger-api/swagger-ui"
  github_stars: 28751
  npm_package: "swagger-ui"
  npm_weekly_downloads: 149194
---

# Swagger OpenAPI Schema Validator

The Swagger OpenAPI Schema Validator performs comprehensive validation of OpenAPI 3.0 and 3.1 specifications using the Spectral linting engine from Stoplight. It applies customizable rulesets covering naming conventions, security scheme requirements, pagination patterns, and error response schemas. The skill integrates swagger-parser for deep JSON Schema validation including $ref resolution across multi-file specifications. Breaking change detection uses oasdiff to compare two API versions, flagging removed endpoints, changed parameter types, narrowed enum values, and modified required fields. It generates detailed compatibility reports following semver conventions. The skill also validates example values against their schemas, checks for unused components, and ensures consistent use of tags and operationIds. Output includes a severity-ranked issue list with line numbers and fix suggestions, making it essential for API-first development workflows.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/swagger-openapi-schema-validator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/swagger-openapi-schema-validator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/swagger-openapi-schema-validator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/swagger-openapi-schema-validator/)
