---
title: OpenAPI Spec Compliance Checker
description: The OpenAPI Spec Compliance Checker skill validates live REST API endpoints
  against their OpenAPI 3.0 and 3.1 specifications. It uses the swagger-parser library
  to resolve and dereference OpenAPI documents including remote $ref references, then
  applies Spectral custom rulesets for style and consistency checks. The validation
  engine sends actual HTTP requests to documented endpoints using configurable authentication
  (Bearer tokens, API keys, OAuth2 client credentials) and compares responses against
  declared schemas using Ajv JSON Schema validator. It checks response status codes,
  content-type headers, response body structure, pagination headers, and error response
  formats. Parameter validation covers path parameters, query parameters, header parameters,
  and request body schemas. The skill detects undocumented endpoints by comparing
  the spec against actual route registrations (supporting Express, FastAPI, and Spring
  Boot route discovery). It also validates security scheme configurations, checking
  that declared OAuth2 scopes match actual endpoint authorization requirements. Reports
  are generated in JUnit XML format for CI integration and HTML format for human review.
verification: security_reviewed
source: https://agentskillexchange.com/skills/openapi-spec-compliance-checker/
category:
- Library &amp; API Reference
framework:
- Cursor
---

# OpenAPI Spec Compliance Checker

The OpenAPI Spec Compliance Checker skill validates live REST API endpoints against their OpenAPI 3.0 and 3.1 specifications. It uses the swagger-parser library to resolve and dereference OpenAPI documents including remote $ref references, then applies Spectral custom rulesets for style and consistency checks. The validation engine sends actual HTTP requests to documented endpoints using configurable authentication (Bearer tokens, API keys, OAuth2 client credentials) and compares responses against declared schemas using Ajv JSON Schema validator. It checks response status codes, content-type headers, response body structure, pagination headers, and error response formats. Parameter validation covers path parameters, query parameters, header parameters, and request body schemas. The skill detects undocumented endpoints by comparing the spec against actual route registrations (supporting Express, FastAPI, and Spring Boot route discovery). It also validates security scheme configurations, checking that declared OAuth2 scopes match actual endpoint authorization requirements. Reports are generated in JUnit XML format for CI integration and HTML format for human review.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openapi-spec-compliance-checker/)
