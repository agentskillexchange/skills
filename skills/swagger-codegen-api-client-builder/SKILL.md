---
title: "Swagger Codegen API Client Builder"
description: "Generates typed API client libraries from OpenAPI 3.x specifications using swagger-codegen and openapi-generator-cli. Produces clients for TypeScript-axios, Python-requests, and Go-http with custom mustache templates."
verification: "security_reviewed"
source: "https://github.com/swagger-api/swagger-ui"
category:
  - "Library &amp; API Reference"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "swagger-api/swagger-ui"
  github_stars: 28751
  ase_npm_package: "swagger-ui"
  npm_weekly_downloads: 149194
  license: "Apache-2.0"
---

# Swagger Codegen API Client Builder

The Swagger Codegen API Client Builder automates generation of strongly-typed API client libraries from OpenAPI 3.x and Swagger 2.0 specifications. It leverages both swagger-codegen and openapi-generator-cli to produce client SDKs for multiple languages including TypeScript with axios interceptors, Python with requests session management, and Go with net/http transport configuration. Custom mustache templates allow fine-tuning generated code to match your organization coding standards and patterns. The builder handles complex OpenAPI features including discriminator-based polymorphism, allOf/oneOf/anyOf compositions, and circular reference resolution. It generates proper error types from API error schemas, retry logic with exponential backoff, and request/response interceptor chains. Configuration profiles store generation settings per API, enabling consistent regeneration when specs change. The tool validates OpenAPI specs before generation using spectral linting rules, catching issues like missing operationIds, undocumented error responses, and inconsistent naming conventions.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/swagger-codegen-api-client-builder/)
