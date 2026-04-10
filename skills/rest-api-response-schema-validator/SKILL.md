---
title: "REST API Response Schema Validator"
description: "Validates live API responses against JSON Schema definitions using Ajv (Another JSON Schema Validator). Supports OpenAPI 3.x schema extraction and detects undocumented fields or type mismatches."
slug: "rest-api-response-schema-validator"
category:
  - "Library &amp; API Reference"
framework:
  - "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/rest-api-response-schema-validator/"
listed: true
---

# REST API Response Schema Validator

Validates live API responses against JSON Schema definitions using Ajv (Another JSON Schema Validator). Supports OpenAPI 3.x schema extraction and detects undocumented fields or type mismatches.

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
clawhub install rest-api-response-schema-validator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The REST API Response Schema Validator uses Ajv (Another JSON Schema Validator) to validate live API endpoint responses against their documented JSON Schema definitions. It extracts response schemas from OpenAPI 3.x specification files, resolving component references and allOf/oneOf/anyOf compositions into flattened validation schemas. The skill makes HTTP requests to configured endpoints using axios with customizable authentication headers, then validates each response body against its expected schema. It detects type mismatches, missing required fields, undocumented extra fields (additionalProperties violations), format constraint failures (date-time, email, URI), and enum value deviations. The validator supports parameterized endpoint testing with variable substitution for path parameters and query strings. Results are compiled into a compatibility report showing schema compliance percentage per endpoint, with detailed error paths for failures. It integrates into CI pipelines as a contract testing step to catch API drift between documentation and implementation.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rest-api-response-schema-validator/)
