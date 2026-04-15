---
title: "REST API Response Schema Validator"
description: "Validates live API responses against JSON Schema definitions using Ajv (Another JSON Schema Validator). Supports OpenAPI 3.x schema extraction and detects undocumented fields or type mismatches."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/rest-api-response-schema-validator/"
category:
  - "Library & API Reference"
framework:
  - "Claude Agents"
---

# REST API Response Schema Validator

The REST API Response Schema Validator uses Ajv (Another JSON Schema Validator) to validate live API endpoint responses against their documented JSON Schema definitions. It extracts response schemas from OpenAPI 3.x specification files, resolving component references and allOf/oneOf/anyOf compositions into flattened validation schemas. The skill makes HTTP requests to configured endpoints using axios with customizable authentication headers, then validates each response body against its expected schema. It detects type mismatches, missing required fields, undocumented extra fields (additionalProperties violations), format constraint failures (date-time, email, URI), and enum value deviations. The validator supports parameterized endpoint testing with variable substitution for path parameters and query strings. Results are compiled into a compatibility report showing schema compliance percentage per endpoint, with detailed error paths for failures. It integrates into CI pipelines as a contract testing step to catch API drift between documentation and implementation.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/rest-api-response-schema-validator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/rest-api-response-schema-validator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rest-api-response-schema-validator/)
