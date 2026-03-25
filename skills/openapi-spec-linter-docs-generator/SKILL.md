---
name: "OpenAPI Spec Linter & Docs Generator"
description: "Validates OpenAPI 3.x specifications using Spectral rulesets and generates interactive API documentation with Redoc and Swagger UI. Detects breaking changes using oasdiff for versioned APIs."
category: "Library & API Reference"
framework: "Claude Agents"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/openapi-spec-linter-docs-generator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "swagger"  # from ase_tool_match
  github_stars: 28703  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 3219093  # from ase_npm_downloads
  github_repo: "swagger-api/swagger-ui"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# OpenAPI Spec Linter & Docs Generator

Validates OpenAPI 3.x specifications using Spectral rulesets and generates interactive API documentation with Redoc and Swagger UI. Detects breaking changes using oasdiff for versioned APIs.

## Overview

The OpenAPI Spec Linter & Docs Generator provides comprehensive API specification management by combining validation, documentation generation, and breaking change detection. It processes OpenAPI 3.0 and 3.1 YAML/JSON specifications through Stoplight Spectral with customizable rulesets to enforce naming conventions, schema consistency, and security scheme requirements.

For documentation, the agent generates both Redoc single-page HTML and Swagger UI bundles, with custom theming support via CSS variables. It extracts code samples from x-code-samples extensions and generates SDK snippets for curl, Python (requests), JavaScript (fetch), and Go (net/http). The output includes a searchable, grouped endpoint reference with authentication flows documented inline.

The breaking change detection module uses oasdiff to compare specification versions, categorizing changes as breaking (removed endpoints, narrowed types), deprecated (sunset headers), or additive (new optional fields). It generates migration guides in Markdown format and can post change summaries as GitHub PR comments via the GitHub API. Integrates with Backstage catalog for automatic API entity registration.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill openapi-spec-linter-docs-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill openapi-spec-linter-docs-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill openapi-spec-linter-docs-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill openapi-spec-linter-docs-generator -a codex
```

### OpenClaw

```bash
clawhub install openapi-spec-linter-docs-generator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/openapi-spec-linter-docs-generator/
