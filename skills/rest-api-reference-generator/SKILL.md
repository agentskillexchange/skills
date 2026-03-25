---
name: "REST API Reference Generator"
description: "Generates interactive API reference documentation from OpenAPI 3.x specs using Swagger Parser and Redoc. Validates schemas, produces code samples in multiple languages via OpenAPI Generator CLI."
category: "Library & API Reference"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/rest-api-reference-generator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "swagger"  # from ase_tool_match
  github_stars: 28703  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 3219093  # from ase_npm_downloads
  github_repo: "swagger-api/swagger-ui"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# REST API Reference Generator

Generates interactive API reference documentation from OpenAPI 3.x specs using Swagger Parser and Redoc. Validates schemas, produces code samples in multiple languages via OpenAPI Generator CLI.

## Overview

The REST API Reference Generator skill processes OpenAPI 3.0 and 3.1 specification files using Swagger Parser for validation and dereferencing. It resolves $ref pointers across multiple files, validates request/response schemas against JSON Schema Draft 2020-12, and detects common specification errors including circular references and missing required fields. The skill generates interactive documentation using the Redoc rendering engine with customizable theme configurations. Code sample generation leverages OpenAPI Generator CLI to produce working request examples in Python (requests/httpx), JavaScript (fetch/axios), Go (net/http), and curl. Authentication flow documentation is automatically generated from security scheme definitions including OAuth2 authorization code flows, API key injection patterns, and JWT bearer token configurations. The skill produces Postman Collection v2.1 exports and Bruno collection files for API testing. Schema diff analysis between specification versions highlights breaking changes following the OpenAPI breaking change detection rules.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill rest-api-reference-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill rest-api-reference-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill rest-api-reference-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill rest-api-reference-generator -a codex
```

### OpenClaw

```bash
clawhub install rest-api-reference-generator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/rest-api-reference-generator/
