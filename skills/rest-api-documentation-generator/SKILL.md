---
title: "REST API Documentation Generator"
description: "Generates interactive API documentation from code annotations using swagger-jsdoc for Express.js routes and the Redoc (@redocly/cli) renderer. Supports OpenAPI 3.1 output with JSON Schema $ref resolution via @apidevtools/json-schema-ref-parser."
slug: "rest-api-documentation-generator"
category:
  - "Library &amp; API Reference"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/rest-api-documentation-generator/"
listed: true
---

# REST API Documentation Generator

Generates interactive API documentation from code annotations using swagger-jsdoc for Express.js routes and the Redoc (@redocly/cli) renderer. Supports OpenAPI 3.1 output with JSON Schema $ref resolution via @apidevtools/json-schema-ref-parser.

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
clawhub install rest-api-documentation-generator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The REST API Documentation Generator skill automates the creation of comprehensive, interactive API documentation directly from source code. It uses swagger-jsdoc to extract OpenAPI annotations from Express.js route handlers, controller methods, and middleware definitions, producing valid OpenAPI 3.1 specification files.
Documentation rendering is handled by Redoc through the @redocly/cli tool, generating responsive single-page HTML documentation with three-panel layouts, code samples in multiple languages, and interactive try-it-out functionality. The skill configures Redoc theme customization including branding colors, logo placement, and navigation structure.
Schema management leverages @apidevtools/json-schema-ref-parser for resolving $ref chains across multiple schema files, supporting both local file references and remote URL schemas. The skill generates TypeScript interfaces alongside OpenAPI schemas to maintain consistency between documentation and implementation types.
Additional capabilities include automatic changelog generation by diffing OpenAPI specs between git commits, generating Postman collection exports for API testing, creating mock server configurations using Prism (@stoplight/prism-cli), and producing SDK stubs through OpenAPI Generator integration. The skill enforces documentation completeness by flagging undocumented endpoints and missing response examples.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rest-api-documentation-generator/)
