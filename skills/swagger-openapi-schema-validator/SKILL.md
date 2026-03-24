---
name: "Swagger OpenAPI Schema Validator"
description: "Validates and lints OpenAPI 3.1 specifications using Spectral ruleset engine and swagger-parser. Detects breaking changes between API versions using oasdiff comparison tool."
category: "Library & API Reference"
framework: "Cursor"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/swagger-openapi-schema-validator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "swagger"  # from ase_tool_match
  github_stars: 28702  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 3219093  # from ase_npm_downloads
  github_repo: "swagger-api/swagger-ui"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
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
