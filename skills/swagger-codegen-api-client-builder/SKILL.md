---
title: "Swagger Codegen API Client Builder"
description: "Generates typed API client libraries from OpenAPI 3.x specifications using swagger-codegen and openapi-generator-cli. Produces clients for TypeScript-axios, Python-requests, and Go-http with custom mustache templates."
verification: security_reviewed
source: "https://github.com/swagger-api/swagger-ui"
category:
  - "Library &amp; API Reference"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "swagger-api/swagger-ui"
  github_stars: 28751
  npm_package: "swagger-ui"
  npm_weekly_downloads: 149194
---

# Swagger Codegen API Client Builder

The Swagger Codegen API Client Builder automates generation of strongly-typed API client libraries from OpenAPI 3.x and Swagger 2.0 specifications. It leverages both swagger-codegen and openapi-generator-cli to produce client SDKs for multiple languages including TypeScript with axios interceptors, Python with requests session management, and Go with net/http transport configuration. Custom mustache templates allow fine-tuning generated code to match your organization coding standards and patterns. The builder handles complex OpenAPI features including discriminator-based polymorphism, allOf/oneOf/anyOf compositions, and circular reference resolution. It generates proper error types from API error schemas, retry logic with exponential backoff, and request/response interceptor chains. Configuration profiles store generation settings per API, enabling consistent regeneration when specs change. The tool validates OpenAPI specs before generation using spectral linting rules, catching issues like missing operationIds, undocumented error responses, and inconsistent naming conventions.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/swagger-codegen-api-client-builder/)
