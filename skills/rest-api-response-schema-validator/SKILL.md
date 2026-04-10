---
name: REST API Response Schema Validator
description: Validates live API responses against JSON Schema definitions using Ajv
  (Another JSON Schema Validator). Supports OpenAPI 3.x schema extraction and detects
  undocumented fields or type mismatches.
verification: security_reviewed
source: https://agentskillexchange.com/skills/rest-api-response-schema-validator/
category:
- Library &amp; API Reference
framework:
- Claude Agents
---
# REST API Response Schema Validator

The REST API Response Schema Validator uses Ajv (Another JSON Schema Validator) to validate live API endpoint responses against their documented JSON Schema definitions. It extracts response schemas from OpenAPI 3.x specification files, resolving component references and allOf/oneOf/anyOf compositions into flattened validation schemas. The skill makes HTTP requests to configured endpoints using axios with customizable authentication headers, then validates each response body against its expected schema. It detects type mismatches, missing required fields, undocumented extra fields (additionalProperties violations), format constraint failures (date-time, email, URI), and enum value deviations. The validator supports parameterized endpoint testing with variable substitution for path parameters and query strings. Results are compiled into a compatibility report showing schema compliance percentage per endpoint, with detailed error paths for failures. It integrates into CI pipelines as a contract testing step to catch API drift between documentation and implementation.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rest-api-response-schema-validator/)
