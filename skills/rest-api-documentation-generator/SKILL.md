---
name: REST API Documentation Generator
description: Generates interactive API documentation from code annotations using swagger-jsdoc for Express.js routes and the Redoc (@redocly/cli) renderer. Supports OpenAPI 3.1 output with JSON Schema $ref resolut
category: Library & API Reference
framework: Claude Code
verification: security_reviewed
rating: 4.9
reviews: 86
source: https://agentskillexchange.com/skill/rest-api-documentation-generator/
---

# REST API Documentation Generator

Generates interactive API documentation from code annotations using swagger-jsdoc for Express.js routes and the Redoc (@redocly/cli) renderer. Supports OpenAPI 3.1 output with JSON Schema $ref resolution via @apidevtools/json-schema-ref-parser.

## Overview

The REST API Documentation Generator skill automates the creation of comprehensive, interactive API documentation directly from source code. It uses swagger-jsdoc to extract OpenAPI annotations from Express.js route handlers, controller methods, and middleware definitions, producing valid OpenAPI 3.1 specification files.
Documentation rendering is handled by Redoc through the @redocly/cli tool, generating responsive single-page HTML documentation with three-panel layouts, code samples in multiple languages, and interactive try-it-out functionality. The skill configures Redoc theme customization including branding colors, logo placement, and navigation structure.
Schema management leverages @apidevtools/json-schema-ref-parser for resolving $ref chains across multiple schema files, supporting both local file references and remote URL schemas. The skill generates TypeScript interfaces alongside OpenAPI schemas to maintain consistency between documentation and implementation types.
Additional capabilities include automatic changelog generation by diffing OpenAPI specs between git commits, generating Postman collection exports for API testing, creating mock server configurations using Prism (@stoplight/prism-cli), and producing SDK stubs through OpenAPI Generator integration. The skill enforces documentation completeness by flagging undocumented endpoints and missing response examples.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill rest-api-documentation-generator
```

### OpenClaw

```bash
openclaw install rest-api-documentation-generator
```

### Manual

Download this `SKILL.md` file and place it in your agent's skills directory.

## Metadata

| Field | Value |
|-------|-------|
| Category | Library & API Reference |
| Framework | Claude Code |
| Verification | Security Reviewed |
| Rating | ⭐⭐⭐⭐ 4.9/5.0 (86 reviews) |

---

*Published on [Agent Skill Exchange](https://agentskillexchange.com/skill/rest-api-documentation-generator/)*
