---
name: OpenAPI SDK Generator Pipeline
description: Generates typed client SDKs from OpenAPI 3.x specifications using openapi-generator-cli.
  Produces TypeScript, Python, and Go clients with proper authentication interceptors
  and retry logic.
verification: security_reviewed
source: https://agentskillexchange.com/skills/openapi-sdk-generator-pipeline/
category:
- Library &amp; API Reference
framework:
- Custom Agents
---
# OpenAPI SDK Generator Pipeline

This skill transforms OpenAPI 3.0 and 3.1 specifications into production-ready client SDKs using the OpenAPI Generator CLI. It validates spec files against the OpenAPI JSON Schema, resolving external $ref references and circular dependencies. The generator produces typed client libraries for TypeScript (using fetch or axios), Python (using httpx or aiohttp), and Go (using net/http) with full model serialization support. Authentication interceptors handle OAuth2, API key, and Bearer token flows with automatic token refresh. Generated clients include exponential backoff retry logic with configurable attempt limits and jitter. Request and response validation middleware ensures runtime conformance to the API schema. The skill generates comprehensive test suites with mock server configurations using Prism or WireMock. Documentation is auto-generated as markdown API references with code examples for each endpoint. Package publishing configurations produce npm packages, PyPI wheels, and Go modules with semantic versioning derived from spec version fields.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openapi-sdk-generator-pipeline/)
