---
title: "REST API Documentation Generator"
description: "Generates interactive API documentation from code annotations using swagger-jsdoc for Express.js routes and the Redoc (@redocly/cli) renderer. Supports OpenAPI 3.1 output with JSON Schema $ref resolution via @apidevtools/json-schema-ref-parser."
verification: "security_reviewed"
source: "https://swagger.io/docs/"
category:
  - "Library & API Reference"
framework:
  - "Claude Code"
---

# REST API Documentation Generator

The REST API Documentation Generator skill automates the creation of comprehensive, interactive API documentation directly from source code. It uses swagger-jsdoc to extract OpenAPI annotations from Express.js route handlers, controller methods, and middleware definitions, producing valid OpenAPI 3.1 specification files. Documentation rendering is handled by Redoc through the @redocly/cli tool, generating responsive single-page HTML documentation with three-panel layouts, code samples in multiple languages, and interactive try-it-out functionality. The skill configures Redoc theme customization including branding colors, logo placement, and navigation structure. Schema management leverages @apidevtools/json-schema-ref-parser for resolving $ref chains across multiple schema files, supporting both local file references and remote URL schemas. The skill generates TypeScript interfaces alongside OpenAPI schemas to maintain consistency between documentation and implementation types. Additional capabilities include automatic changelog generation by diffing OpenAPI specs between git commits, generating Postman collection exports for API testing, creating mock server configurations using Prism (@stoplight/prism-cli), and producing SDK stubs through OpenAPI Generator integration. The skill enforces documentation completeness by flagging undocumented endpoints and missing response examples.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/rest-api-documentation-generator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/rest-api-documentation-generator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/rest-api-documentation-generator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rest-api-documentation-generator/)
