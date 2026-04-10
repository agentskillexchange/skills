---
title: "REST API Testing Reference Kit"
description: "Comprehensive REST API testing reference using Postman Collection SDK v2.1 and Newman CLI. Includes assertion libraries for JSON Schema validation with Ajv, response time benchmarking, and contract testing patterns."
slug: "rest-api-testing-reference-kit"
category:
  - "Library &amp; API Reference"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/rest-api-testing-reference-kit/"
listed: true
---

# REST API Testing Reference Kit

Comprehensive REST API testing reference using Postman Collection SDK v2.1 and Newman CLI. Includes assertion libraries for JSON Schema validation with Ajv, response time benchmarking, and contract testing patterns.

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
clawhub install rest-api-testing-reference-kit
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The REST API Testing Reference Kit provides structured testing patterns and reusable test suites for REST API validation. Built on Postman Collection SDK v2.1 format with Newman CLI execution, it offers a comprehensive library of test patterns organized by HTTP method, authentication type, and response format.
Core testing capabilities include JSON Schema validation using Ajv with custom format validators, response time benchmarking with statistical analysis including p95 and p99 latency calculations, and header compliance checking for CORS, security headers, and caching directives. The agent maintains a library of assertion patterns for common API patterns like pagination, filtering, sorting, and error responses.
Advanced features include contract testing against OpenAPI specs to detect breaking changes, automated test generation from Swagger documentation, and environment-specific variable management for multi-stage deployment testing. The agent supports authentication flow testing for OAuth 2.0, JWT, and API key patterns, generates load testing scripts compatible with k6 and Artillery, and creates comprehensive API coverage reports mapping tested endpoints against the full specification.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rest-api-testing-reference-kit/)
