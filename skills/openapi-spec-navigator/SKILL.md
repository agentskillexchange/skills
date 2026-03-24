---
name: "OpenAPI Spec Navigator"
description: "Parses and navigates OpenAPI 3.1 specifications using swagger-parser and @apidevtools/json-schema-ref-parser. Resolves $ref chains, extracts endpoint signatures, and generates typed client stubs."
category: "Library & API Reference"
framework: "Cursor"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/openapi-spec-navigator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "swagger"  # from ase_tool_match
  github_stars: 28702  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 3219093  # from ase_npm_downloads
  github_repo: "swagger-api/swagger-ui"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# OpenAPI Spec Navigator

Parses and navigates OpenAPI 3.1 specifications using swagger-parser and @apidevtools/json-schema-ref-parser. Resolves $ref chains, extracts endpoint signatures, and generates typed client stubs.

## Overview

The OpenAPI Spec Navigator skill provides intelligent traversal and analysis of OpenAPI 3.1 specification documents. It uses swagger-parser for spec validation and dereferencing, @apidevtools/json-schema-ref-parser for resolving complex $ref chains including circular references, and generates comprehensive endpoint documentation from path items and operation objects.

The skill extracts complete endpoint signatures including HTTP methods, path parameters with style/explode serialization rules, query parameter schemas with allowReserved handling, and request body content type negotiation. It resolves discriminator-based polymorphic schemas with oneOf/anyOf compositions and generates TypeScript type definitions using json-schema-to-typescript.

Advanced capabilities include security scheme analysis for OAuth2 flows (authorizationCode, clientCredentials, implicit), API key placement detection (header, query, cookie), and server variable template resolution. The skill generates client stubs compatible with axios and node-fetch, handles pagination patterns (cursor, offset, keyset) from x-pagination extensions, and produces Postman collection exports via openapi-to-postmanv2 for interactive testing.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill openapi-spec-navigator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill openapi-spec-navigator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill openapi-spec-navigator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill openapi-spec-navigator -a codex
```

### OpenClaw

```bash
clawhub install openapi-spec-navigator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/openapi-spec-navigator/
