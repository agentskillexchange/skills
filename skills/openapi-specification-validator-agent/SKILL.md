---
name: "OpenAPI Specification Validator"
description: "Validates and lints OpenAPI 3.x specifications using swagger-parser, spectral, and openapi-typescript. Generates type-safe client SDKs and detects breaking API changes via oasdiff."
category: "Library &amp; API Reference"
framework: "Cursor"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/openapi-specification-validator-agent/"
---
# OpenAPI Specification Validator

Validates and lints OpenAPI 3.x specifications using swagger-parser, spectral, and openapi-typescript. Generates type-safe client SDKs and detects breaking API changes via oasdiff.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill openapi-specification-validator-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill openapi-specification-validator-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill openapi-specification-validator-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill openapi-specification-validator-agent -a codex
```

### OpenClaw

```bash
clawhub install openapi-specification-validator-agent
```

## Details

The OpenAPI Specification Validator performs comprehensive validation of OpenAPI 3.0 and 3.1 documents using swagger-parser for structural validation and @stoplight/spectral for style and convention enforcement. It applies custom Spectral rulesets that enforce organizational API standards including naming conventions, pagination patterns, and error response schemas. The skill uses openapi-typescript to generate TypeScript type definitions from validated specs, ensuring frontend-backend type safety. It integrates oasdiff for detecting breaking changes between API versions, generating detailed compatibility reports that highlight removed endpoints, changed parameter types, and modified response schemas. The tool also leverages redocly/openapi-cli for spec bundling, splitting multi-file specs, and generating interactive API documentation. It supports validation of x-extension fields for custom metadata and ensures proper security scheme definitions across OAuth2, API key, and JWT bearer authentication patterns.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openapi-specification-validator-agent/)
