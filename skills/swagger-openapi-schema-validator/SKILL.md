---
title: "Swagger OpenAPI Schema Validator"
description: "Validates and lints OpenAPI 3.1 specifications using Spectral ruleset engine and swagger-parser. Detects breaking changes between API versions using oasdiff comparison tool."
verification: "security_reviewed"
source: "https://github.com/swagger-api/swagger-ui"
category:
  - "Library &amp; API Reference"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "swagger-api/swagger-ui"
  github_stars: 28751
  ase_npm_package: "swagger-ui"
  npm_weekly_downloads: 149194
  license: "Apache-2.0"
---

# Swagger OpenAPI Schema Validator

The Swagger OpenAPI Schema Validator performs comprehensive validation of OpenAPI 3.0 and 3.1 specifications using the Spectral linting engine from Stoplight. It applies customizable rulesets covering naming conventions, security scheme requirements, pagination patterns, and error response schemas. The skill integrates swagger-parser for deep JSON Schema validation including $ref resolution across multi-file specifications. Breaking change detection uses oasdiff to compare two API versions, flagging removed endpoints, changed parameter types, narrowed enum values, and modified required fields. It generates detailed compatibility reports following semver conventions. The skill also validates example values against their schemas, checks for unused components, and ensures consistent use of tags and operationIds. Output includes a severity-ranked issue list with line numbers and fix suggestions, making it essential for API-first development workflows.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/swagger-openapi-schema-validator/)
