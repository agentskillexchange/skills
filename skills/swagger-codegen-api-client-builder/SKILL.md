---
name: "Swagger Codegen API Client Builder"
description: "Generates typed API client libraries from OpenAPI 3.x specifications using swagger-codegen and openapi-generator-cli. Produces clients for TypeScript-axios, Python-requests, and Go-http with custom mustache templates."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/swagger-codegen-api-client-builder/"
category:
  - "Library &amp; API Reference"
framework:
  - "Claude Code"
---

# Swagger Codegen API Client Builder

The Swagger Codegen API Client Builder automates generation of strongly-typed API client libraries from OpenAPI 3.x and Swagger 2.0 specifications. It leverages both swagger-codegen and openapi-generator-cli to produce client SDKs for multiple languages including TypeScript with axios interceptors, Python with requests session management, and Go with net/http transport configuration. Custom mustache templates allow fine-tuning generated code to match your organization coding standards and patterns. The builder handles complex OpenAPI features including discriminator-based polymorphism, allOf/oneOf/anyOf compositions, and circular reference resolution. It generates proper error types from API error schemas, retry logic with exponential backoff, and request/response interceptor chains. Configuration profiles store generation settings per API, enabling consistent regeneration when specs change. The tool validates OpenAPI specs before generation using spectral linting rules, catching issues like missing operationIds, undocumented error responses, and inconsistent naming conventions.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/swagger-codegen-api-client-builder/)
