---
title: "OpenAPI Spec Linter & Docs Generator"
description: "Validates OpenAPI 3.x specifications using Spectral rulesets and generates interactive API documentation with Redoc and Swagger UI. Detects breaking changes using oasdiff for versioned APIs."
slug: "openapi-spec-linter-docs-generator"
category:
  - "Library &amp; API Reference"
framework:
  - "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/openapi-spec-linter-docs-generator/"
listed: true
---

# OpenAPI Spec Linter & Docs Generator

Validates OpenAPI 3.x specifications using Spectral rulesets and generates interactive API documentation with Redoc and Swagger UI. Detects breaking changes using oasdiff for versioned APIs.

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
clawhub install openapi-spec-linter-docs-generator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The OpenAPI Spec Linter & Docs Generator provides comprehensive API specification management by combining validation, documentation generation, and breaking change detection. It processes OpenAPI 3.0 and 3.1 YAML/JSON specifications through Stoplight Spectral with customizable rulesets to enforce naming conventions, schema consistency, and security scheme requirements.
For documentation, the agent generates both Redoc single-page HTML and Swagger UI bundles, with custom theming support via CSS variables. It extracts code samples from x-code-samples extensions and generates SDK snippets for curl, Python (requests), JavaScript (fetch), and Go (net/http). The output includes a searchable, grouped endpoint reference with authentication flows documented inline.
The breaking change detection module uses oasdiff to compare specification versions, categorizing changes as breaking (removed endpoints, narrowed types), deprecated (sunset headers), or additive (new optional fields). It generates migration guides in Markdown format and can post change summaries as GitHub PR comments via the GitHub API. Integrates with Backstage catalog for automatic API entity registration.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openapi-spec-linter-docs-generator/)
