---
name: "OpenAPI Spec Linter & Docs Generator"
description: "Validates OpenAPI 3.x specifications using Spectral rulesets and generates interactive API documentation with Redoc and Swagger UI. Detects breaking changes using oasdiff for versioned APIs."
category: "Library &amp; API Reference"
framework: "Claude Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/openapi-spec-linter-docs-generator/"
---
# OpenAPI Spec Linter & Docs Generator

Validates OpenAPI 3.x specifications using Spectral rulesets and generates interactive API documentation with Redoc and Swagger UI. Detects breaking changes using oasdiff for versioned APIs.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openapi-spec-linter-docs-generator/)
