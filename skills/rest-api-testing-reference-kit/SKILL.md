---
title: "REST API Testing Reference Kit"
description: "Comprehensive REST API testing reference using Postman Collection SDK v2.1 and Newman CLI. Includes assertion libraries for JSON Schema validation with Ajv, response time benchmarking, and contract testing patterns."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/rest-api-testing-reference-kit/"
category:
  - "Library &amp; API Reference"
framework:
  - "Cursor"
---

# REST API Testing Reference Kit

The REST API Testing Reference Kit provides structured testing patterns and reusable test suites for REST API validation. Built on Postman Collection SDK v2.1 format with Newman CLI execution, it offers a comprehensive library of test patterns organized by HTTP method, authentication type, and response format.

Core testing capabilities include JSON Schema validation using Ajv with custom format validators, response time benchmarking with statistical analysis including p95 and p99 latency calculations, and header compliance checking for CORS, security headers, and caching directives. The agent maintains a library of assertion patterns for common API patterns like pagination, filtering, sorting, and error responses.

Advanced features include contract testing against OpenAPI specs to detect breaking changes, automated test generation from Swagger documentation, and environment-specific variable management for multi-stage deployment testing. The agent supports authentication flow testing for OAuth 2.0, JWT, and API key patterns, generates load testing scripts compatible with k6 and Artillery, and creates comprehensive API coverage reports mapping tested endpoints against the full specification.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rest-api-testing-reference-kit/)
