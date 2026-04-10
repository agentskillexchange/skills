---
name: "Swagger OpenAPI Schema Validator"
description: "Validates and lints OpenAPI 3.1 specifications using Spectral ruleset engine and swagger-parser. Detects breaking changes between API versions using oasdiff comparison tool."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/swagger-openapi-schema-validator/"
category:
  - "Library &amp; API Reference"
framework:
  - "Cursor"
---

# Swagger OpenAPI Schema Validator

The Swagger OpenAPI Schema Validator performs comprehensive validation of OpenAPI 3.0 and 3.1 specifications using the Spectral linting engine from Stoplight. It applies customizable rulesets covering naming conventions, security scheme requirements, pagination patterns, and error response schemas. The skill integrates swagger-parser for deep JSON Schema validation including $ref resolution across multi-file specifications. Breaking change detection uses oasdiff to compare two API versions, flagging removed endpoints, changed parameter types, narrowed enum values, and modified required fields. It generates detailed compatibility reports following semver conventions. The skill also validates example values against their schemas, checks for unused components, and ensures consistent use of tags and operationIds. Output includes a severity-ranked issue list with line numbers and fix suggestions, making it essential for API-first development workflows.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/swagger-openapi-schema-validator/)
