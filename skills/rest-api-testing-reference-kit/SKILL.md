---
name: "REST API Testing Reference Kit"
description: "Comprehensive REST API testing reference using Postman Collection SDK v2.1 and Newman CLI. Includes assertion libraries for JSON Schema validation with Ajv, response time benchmarking, and contract testing patterns."
category: "Library & API Reference"
framework: "Cursor"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/rest-api-testing-reference-kit/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "swagger"  # from ase_tool_match
  github_stars: 28702  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 3219093  # from ase_npm_downloads
  github_repo: "swagger-api/swagger-ui"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# REST API Testing Reference Kit

Comprehensive REST API testing reference using Postman Collection SDK v2.1 and Newman CLI. Includes assertion libraries for JSON Schema validation with Ajv, response time benchmarking, and contract testing patterns.

## Overview

The REST API Testing Reference Kit provides structured testing patterns and reusable test suites for REST API validation. Built on Postman Collection SDK v2.1 format with Newman CLI execution, it offers a comprehensive library of test patterns organized by HTTP method, authentication type, and response format.

Core testing capabilities include JSON Schema validation using Ajv with custom format validators, response time benchmarking with statistical analysis including p95 and p99 latency calculations, and header compliance checking for CORS, security headers, and caching directives. The agent maintains a library of assertion patterns for common API patterns like pagination, filtering, sorting, and error responses.

Advanced features include contract testing against OpenAPI specs to detect breaking changes, automated test generation from Swagger documentation, and environment-specific variable management for multi-stage deployment testing. The agent supports authentication flow testing for OAuth 2.0, JWT, and API key patterns, generates load testing scripts compatible with k6 and Artillery, and creates comprehensive API coverage reports mapping tested endpoints against the full specification.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill rest-api-testing-reference-kit
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill rest-api-testing-reference-kit -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill rest-api-testing-reference-kit -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill rest-api-testing-reference-kit -a codex
```

### OpenClaw

```bash
clawhub install rest-api-testing-reference-kit
```

## Source

- Marketplace: https://agentskillexchange.com/skills/rest-api-testing-reference-kit/
