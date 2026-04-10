---
name: "OpenAPI Specification Validator"
description: "Validates and lints OpenAPI 3.x specifications using swagger-parser, spectral, and openapi-typescript. Generates type-safe client SDKs and detects breaking API changes via oasdiff."
verification: security_reviewed
source: "https://github.com/APIDevTools/swagger-parser"
category:
  - "Library &amp; API Reference"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "APIDevTools/swagger-parser"
  github_stars: 1194
  ase_npm_package: "@apidevtools/swagger-parser"
  npm_weekly_downloads: 3732285
---

# OpenAPI Specification Validator

The OpenAPI Specification Validator performs comprehensive validation of OpenAPI 3.0 and 3.1 documents using swagger-parser for structural validation and @stoplight/spectral for style and convention enforcement. It applies custom Spectral rulesets that enforce organizational API standards including naming conventions, pagination patterns, and error response schemas. The skill uses openapi-typescript to generate TypeScript type definitions from validated specs, ensuring frontend-backend type safety. It integrates oasdiff for detecting breaking changes between API versions, generating detailed compatibility reports that highlight removed endpoints, changed parameter types, and modified response schemas. The tool also leverages redocly/openapi-cli for spec bundling, splitting multi-file specs, and generating interactive API documentation. It supports validation of x-extension fields for custom metadata and ensures proper security scheme definitions across OAuth2, API key, and JWT bearer authentication patterns.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openapi-specification-validator-agent/)
