---
title: "Swagger Codegen Orchestrator"
description: "Orchestrates OpenAPI 3.x code generation using swagger-codegen-cli and openapi-generator. Produces typed client SDKs for TypeScript, Python, and Go with custom Mustache templates."
verification: "security_reviewed"
source: "https://github.com/swagger-api/swagger-ui"
category:
  - "Templates & Workflows"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "swagger-api/swagger-ui"
  github_stars: 28751
  ase_npm_package: "swagger-ui"
  npm_weekly_downloads: 149194
  license: "Apache-2.0"
---

# Swagger Codegen Orchestrator

The Swagger Codegen Orchestrator streamlines API client generation from OpenAPI 3.x specifications. It wraps swagger-codegen-cli and openapi-generator to produce strongly typed client SDKs across TypeScript, Python, and Go targets. The tool supports custom Mustache template overrides for controlling generated code style, error handling patterns, and authentication flows. It reads OpenAPI specs from local files, URLs, or directly from Swagger Hub via the SwaggerHub API. For TypeScript targets, it generates axios-based clients with full type inference and automatic retry logic using axios-retry. Python clients use httpx with async support and Pydantic v2 models for request/response validation. Go clients leverage net/http with context propagation and structured error types. The orchestrator handles multi-spec scenarios where microservices expose separate APIs, merging them into a unified SDK with proper namespace isolation and shared model deduplication.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/swagger-codegen-orchestrator/)
