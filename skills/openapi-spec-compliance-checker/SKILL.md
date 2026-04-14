---
title: "OpenAPI Spec Compliance Checker"
description: "Validates REST APIs against their OpenAPI 3.x specifications using swagger-parser and Spectral linter rules. Checks response schemas, parameter types, authentication requirements, and generates compliance reports."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/openapi-spec-compliance-checker/"
category:
  - "Library &amp; API Reference"
framework:
  - "Cursor"
---

# OpenAPI Spec Compliance Checker

The OpenAPI Spec Compliance Checker skill validates live REST API endpoints against their OpenAPI 3.0 and 3.1 specifications. It uses the swagger-parser library to resolve and dereference OpenAPI documents including remote $ref references, then applies Spectral custom rulesets for style and consistency checks.

The validation engine sends actual HTTP requests to documented endpoints using configurable authentication (Bearer tokens, API keys, OAuth2 client credentials) and compares responses against declared schemas using Ajv JSON Schema validator. It checks response status codes, content-type headers, response body structure, pagination headers, and error response formats.

Parameter validation covers path parameters, query parameters, header parameters, and request body schemas. The skill detects undocumented endpoints by comparing the spec against actual route registrations (supporting Express, FastAPI, and Spring Boot route discovery). It also validates security scheme configurations, checking that declared OAuth2 scopes match actual endpoint authorization requirements. Reports are generated in JUnit XML format for CI integration and HTML format for human review.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openapi-spec-compliance-checker/)
