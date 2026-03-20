---
name: OpenAPI Spec Reference Generator
description: Converts OpenAPI 3.x specification files into browsable API reference documentation using swagger-parser and redoc-cli. Generates static HTML, markdown, and Postman collection exports from YAML/JSON s
category: Library & API Reference
framework: Cursor
verification: verified_metadata
rating: 4.9
reviews: 86
source: https://agentskillexchange.com/skill/openapi-spec-reference-generator/
---

# OpenAPI Spec Reference Generator

Converts OpenAPI 3.x specification files into browsable API reference documentation using swagger-parser and redoc-cli. Generates static HTML, markdown, and Postman collection exports from YAML/JSON spec files.

## Overview

The OpenAPI Spec Reference Generator transforms OpenAPI 3.x specifications into comprehensive, browsable API reference documentation. It uses the swagger-parser library for spec validation and dereferencing of $ref pointers.
Documentation generation leverages redoc-cli to produce responsive static HTML pages with interactive try-it-out panels, authentication configuration, and code sample generation in multiple languages. The skill also exports Postman Collection v2.1 format for direct import into Postman workspaces.
The generator supports multi-file spec resolution, automatically resolving external $ref references across split specification files. It validates specs against the OpenAPI 3.0 and 3.1 standards, reporting structural errors and suggesting fixes.
Additional output formats include markdown suitable for GitHub wiki pages, Docusaurus MDX components, and Slate-compatible documentation. The skill handles custom x-extensions, webhook definitions, and link objects for HATEOAS-style API documentation with navigable resource relationships.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill openapi-spec-reference-generator
```

### OpenClaw

```bash
openclaw install openapi-spec-reference-generator
```

### Manual

Download this `SKILL.md` file and place it in your agent's skills directory.

## Metadata

| Field | Value |
|-------|-------|
| Category | Library & API Reference |
| Framework | Cursor |
| Verification | Verified Metadata |
| Rating | ⭐⭐⭐⭐ 4.9/5.0 (86 reviews) |

---

*Published on [Agent Skill Exchange](https://agentskillexchange.com/skill/openapi-spec-reference-generator/)*
