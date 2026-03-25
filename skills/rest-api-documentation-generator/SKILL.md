---
name: "REST API Documentation Generator"
description: "Generates interactive API documentation from code annotations using swagger-jsdoc for Express.js routes and the Redoc (@redocly/cli) renderer. Supports OpenAPI 3.1 output with JSON Schema $ref resolution via @apidevtools/json-schema-ref-parser."
category: "Library & API Reference"
framework: "Claude Code"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/rest-api-documentation-generator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "express"  # from ase_tool_match
  github_stars: 68883  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 91687881  # from ase_npm_downloads
  github_repo: "expressjs/express"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# REST API Documentation Generator

Generates interactive API documentation from code annotations using swagger-jsdoc for Express.js routes and the Redoc (@redocly/cli) renderer. Supports OpenAPI 3.1 output with JSON Schema $ref resolution via @apidevtools/json-schema-ref-parser.

## Overview

The REST API Documentation Generator skill automates the creation of comprehensive, interactive API documentation directly from source code. It uses swagger-jsdoc to extract OpenAPI annotations from Express.js route handlers, controller methods, and middleware definitions, producing valid OpenAPI 3.1 specification files.

Documentation rendering is handled by Redoc through the @redocly/cli tool, generating responsive single-page HTML documentation with three-panel layouts, code samples in multiple languages, and interactive try-it-out functionality. The skill configures Redoc theme customization including branding colors, logo placement, and navigation structure.

Schema management leverages @apidevtools/json-schema-ref-parser for resolving $ref chains across multiple schema files, supporting both local file references and remote URL schemas. The skill generates TypeScript interfaces alongside OpenAPI schemas to maintain consistency between documentation and implementation types.

Additional capabilities include automatic changelog generation by diffing OpenAPI specs between git commits, generating Postman collection exports for API testing, creating mock server configurations using Prism (@stoplight/prism-cli), and producing SDK stubs through OpenAPI Generator integration. The skill enforces documentation completeness by flagging undocumented endpoints and missing response examples.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill rest-api-documentation-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill rest-api-documentation-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill rest-api-documentation-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill rest-api-documentation-generator -a codex
```

### OpenClaw

```bash
clawhub install rest-api-documentation-generator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/rest-api-documentation-generator/
