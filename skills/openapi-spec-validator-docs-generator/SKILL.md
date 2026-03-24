---
name: "OpenAPI Spec Validator & Docs Generator"
description: "Validates OpenAPI 3.0/3.1 specifications using Spectral linting rules and generates interactive API documentation with Redoc and Swagger UI. Supports custom ruleset definitions and CI integration."
category: "Library & API Reference"
framework: "MCP-compatible"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/openapi-spec-validator-docs-generator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "swagger"  # from ase_tool_match
  github_stars: 28702  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 3219093  # from ase_npm_downloads
  github_repo: "swagger-api/swagger-ui"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# OpenAPI Spec Validator & Docs Generator

Validates OpenAPI 3.0/3.1 specifications using Spectral linting rules and generates interactive API documentation with Redoc and Swagger UI. Supports custom ruleset definitions and CI integration.

## Overview

The OpenAPI Spec Validator and Docs Generator skill provides comprehensive validation of OpenAPI specifications and automated documentation generation. It uses Stoplight Spectral for linting with both built-in (oas) and custom rulesets, catching issues like missing descriptions, inconsistent error response schemas, and security scheme gaps.

The validation engine checks structural correctness against the OpenAPI 3.0.x and 3.1.x JSON Schema definitions, validates $ref resolution across multi-file specifications, and enforces API design guidelines through configurable Spectral rulesets. Custom rules can enforce naming conventions, pagination patterns, and versioning strategies specific to your organization.

For documentation generation, the skill produces both Redoc single-page HTML documentation and Swagger UI interactive explorers. It supports x-codeSamples extensions for embedding language-specific request examples, x-logo for branding, and webhook documentation for event-driven APIs. The skill integrates with CI pipelines by providing exit codes for lint severity levels and generating diff reports between specification versions using openapi-diff to track breaking changes.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill openapi-spec-validator-docs-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill openapi-spec-validator-docs-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill openapi-spec-validator-docs-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill openapi-spec-validator-docs-generator -a codex
```

### OpenClaw

```bash
clawhub install openapi-spec-validator-docs-generator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/openapi-spec-validator-docs-generator/
