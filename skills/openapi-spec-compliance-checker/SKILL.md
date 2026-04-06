---
name: "OpenAPI Spec Compliance Checker"
description: "Validates REST APIs against their OpenAPI 3.x specifications using swagger-parser and Spectral linter rules. Checks response schemas, parameter types, authentication requirements, and generates compliance reports."
category: "Library & API Reference"
framework: "Cursor"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/openapi-spec-compliance-checker/"
---
# OpenAPI Spec Compliance Checker

Validates REST APIs against their OpenAPI 3.x specifications using swagger-parser and Spectral linter rules. Checks response schemas, parameter types, authentication requirements, and generates compliance reports.

The OpenAPI Spec Compliance Checker skill validates live REST API endpoints against their OpenAPI 3.0 and 3.1 specifications. It uses the swagger-parser library to resolve and dereference OpenAPI documents including remote $ref references, then applies Spectral custom rulesets for style and consistency checks.



The validation engine sends actual HTTP requests to documented endpoints using configurable authentication (Bearer tokens, API keys, OAuth2 client credentials) and compares responses against declared schemas using Ajv JSON Schema validator. It checks response status codes, content-type headers, response body structure, pagination headers, and error response formats.



Parameter validation covers path parameters, query parameters, header parameters, and request body schemas. The skill detects undocumented endpoints by comparing the spec against actual route registrations (supporting Express, FastAPI, and Spring Boot route discovery). It also validates security scheme configurations, checking that declared OAuth2 scopes match actual endpoint authorization requirements. Reports are generated in JUnit XML format for CI integration and HTML format for human review.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill openapi-spec-compliance-checker
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill openapi-spec-compliance-checker -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill openapi-spec-compliance-checker -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill openapi-spec-compliance-checker -a codex
```

### OpenClaw

```bash
clawhub install openapi-spec-compliance-checker
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openapi-spec-compliance-checker/)
