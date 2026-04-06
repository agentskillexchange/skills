---
name: "REST API Response Schema Validator"
description: "Validates live API responses against JSON Schema definitions using Ajv (Another JSON Schema Validator). Supports OpenAPI 3.x schema extraction and detects undocumented fields or type mismatches."
category: "Library &amp; API Reference"
framework: "Claude Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/rest-api-response-schema-validator/"
---
# REST API Response Schema Validator

Validates live API responses against JSON Schema definitions using Ajv (Another JSON Schema Validator). Supports OpenAPI 3.x schema extraction and detects undocumented fields or type mismatches.

The REST API Response Schema Validator uses Ajv (Another JSON Schema Validator) to validate live API endpoint responses against their documented JSON Schema definitions. It extracts response schemas from OpenAPI 3.x specification files, resolving component references and allOf/oneOf/anyOf compositions into flattened validation schemas. The skill makes HTTP requests to configured endpoints using axios with customizable authentication headers, then validates each response body against its expected schema. It detects type mismatches, missing required fields, undocumented extra fields (additionalProperties violations), format constraint failures (date-time, email, URI), and enum value deviations. The validator supports parameterized endpoint testing with variable substitution for path parameters and query strings. Results are compiled into a compatibility report showing schema compliance percentage per endpoint, with detailed error paths for failures. It integrates into CI pipelines as a contract testing step to catch API drift between documentation and implementation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill rest-api-response-schema-validator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill rest-api-response-schema-validator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill rest-api-response-schema-validator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill rest-api-response-schema-validator -a codex
```

### OpenClaw

```bash
clawhub install rest-api-response-schema-validator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rest-api-response-schema-validator/)
