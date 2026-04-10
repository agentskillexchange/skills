---
name: "REST API Reference Generator"
description: "Generates interactive API reference documentation from OpenAPI 3.x specs using Swagger Parser and Redoc. Validates schemas, produces code samples in multiple languages via OpenAPI Generator CLI."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/rest-api-reference-generator/"
category:
  - "Library &amp; API Reference"
framework:
  - "Claude Code"
---

# REST API Reference Generator

The REST API Reference Generator skill processes OpenAPI 3.0 and 3.1 specification files using Swagger Parser for validation and dereferencing. It resolves $ref pointers across multiple files, validates request/response schemas against JSON Schema Draft 2020-12, and detects common specification errors including circular references and missing required fields. The skill generates interactive documentation using the Redoc rendering engine with customizable theme configurations. Code sample generation leverages OpenAPI Generator CLI to produce working request examples in Python (requests/httpx), JavaScript (fetch/axios), Go (net/http), and curl. Authentication flow documentation is automatically generated from security scheme definitions including OAuth2 authorization code flows, API key injection patterns, and JWT bearer token configurations. The skill produces Postman Collection v2.1 exports and Bruno collection files for API testing. Schema diff analysis between specification versions highlights breaking changes following the OpenAPI breaking change detection rules.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rest-api-reference-generator/)
