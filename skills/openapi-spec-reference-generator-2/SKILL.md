---
name: OpenAPI Spec Reference Generator
description: Generates interactive API reference documentation from OpenAPI 3.x specifications using swagger-parser for validation and redoc-cli for static HTML rendering. Supports $ref resolution across multi-fil
category: Library & API Reference
framework: Cursor
verification: security_reviewed
rating: 4.8
reviews: 64
source: https://agentskillexchange.com/skill/openapi-spec-reference-generator-2/
---

# OpenAPI Spec Reference Generator

Generates interactive API reference documentation from OpenAPI 3.x specifications using swagger-parser for validation and redoc-cli for static HTML rendering. Supports $ref resolution across multi-file specs.

## Overview

The OpenAPI Spec Reference Generator skill creates comprehensive API reference documentation from OpenAPI 3.0 and 3.1 specifications. It uses swagger-parser (npm: @apidevtools/swagger-parser) to validate and dereference specifications, resolving all $ref pointers across multi-file YAML and JSON definitions.
The skill generates multiple documentation formats: interactive HTML using redoc-cli with customizable themes and branding, static Markdown suitable for repository documentation, and Postman Collection v2.1 exports for API testing. It can also generate SDK client stubs using openapi-generator-cli for languages including TypeScript, Python, Go, and Ruby.
For validation, the skill checks beyond basic schema compliance to detect common API design issues: inconsistent error response schemas, missing pagination parameters on list endpoints, undocumented query parameters, and security scheme gaps. It cross-references path parameters with their schema definitions to ensure type consistency.
The skill supports specification composition by merging multiple partial OpenAPI files using swagger-merge, enabling teams to maintain per-service spec files that are combined into a unified API reference. It can also diff two spec versions using openapi-diff to generate changelogs and detect breaking changes.
Output includes SEO-optimized HTML with JSON-LD structured data for API endpoint discoverability.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill openapi-spec-reference-generator-2
```

### OpenClaw

```bash
openclaw install openapi-spec-reference-generator-2
```

### Manual

Download this `SKILL.md` file and place it in your agent's skills directory.

## Metadata

| Field | Value |
|-------|-------|
| Category | Library & API Reference |
| Framework | Cursor |
| Verification | Security Reviewed |
| Rating | ⭐⭐⭐⭐ 4.8/5.0 (64 reviews) |

---

*Published on [Agent Skill Exchange](https://agentskillexchange.com/skill/openapi-spec-reference-generator-2/)*
