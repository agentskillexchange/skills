---
name: OpenAPI Spec Linter &#038; Docs Generator
description: Validates OpenAPI 3.x specifications using Spectral rulesets and generates
  interactive API documentation with Redoc and Swagger UI. Detects breaking changes
  using oasdiff for versioned APIs.
verification: security_reviewed
source: https://agentskillexchange.com/skills/openapi-spec-linter-docs-generator/
category:
- Library &amp; API Reference
framework:
- Claude Agents
---
# OpenAPI Spec Linter & Docs Generator

The OpenAPI Spec Linter & Docs Generator provides comprehensive API specification management by combining validation, documentation generation, and breaking change detection. It processes OpenAPI 3.0 and 3.1 YAML/JSON specifications through Stoplight Spectral with customizable rulesets to enforce naming conventions, schema consistency, and security scheme requirements.
For documentation, the agent generates both Redoc single-page HTML and Swagger UI bundles, with custom theming support via CSS variables. It extracts code samples from x-code-samples extensions and generates SDK snippets for curl, Python (requests), JavaScript (fetch), and Go (net/http). The output includes a searchable, grouped endpoint reference with authentication flows documented inline.
The breaking change detection module uses oasdiff to compare specification versions, categorizing changes as breaking (removed endpoints, narrowed types), deprecated (sunset headers), or additive (new optional fields). It generates migration guides in Markdown format and can post change summaries as GitHub PR comments via the GitHub API. Integrates with Backstage catalog for automatic API entity registration.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openapi-spec-linter-docs-generator/)
