---
name: "Swagger Codegen Orchestrator"
description: "Orchestrates OpenAPI 3.x code generation using swagger-codegen-cli and openapi-generator. Produces typed client SDKs for TypeScript, Python, and Go with custom Mustache templates."
category: "Templates & Workflows"
framework: "Claude Code"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/swagger-codegen-orchestrator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "swagger"  # from ase_tool_match
  github_stars: 28702  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 3219093  # from ase_npm_downloads
  github_repo: "swagger-api/swagger-ui"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Swagger Codegen Orchestrator

Orchestrates OpenAPI 3.x code generation using swagger-codegen-cli and openapi-generator. Produces typed client SDKs for TypeScript, Python, and Go with custom Mustache templates.

## Overview

The Swagger Codegen Orchestrator streamlines API client generation from OpenAPI 3.x specifications. It wraps swagger-codegen-cli and openapi-generator to produce strongly typed client SDKs across TypeScript, Python, and Go targets. The tool supports custom Mustache template overrides for controlling generated code style, error handling patterns, and authentication flows. It reads OpenAPI specs from local files, URLs, or directly from Swagger Hub via the SwaggerHub API. For TypeScript targets, it generates axios-based clients with full type inference and automatic retry logic using axios-retry. Python clients use httpx with async support and Pydantic v2 models for request/response validation. Go clients leverage net/http with context propagation and structured error types. The orchestrator handles multi-spec scenarios where microservices expose separate APIs, merging them into a unified SDK with proper namespace isolation and shared model deduplication.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill swagger-codegen-orchestrator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill swagger-codegen-orchestrator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill swagger-codegen-orchestrator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill swagger-codegen-orchestrator -a codex
```

### OpenClaw

```bash
clawhub install swagger-codegen-orchestrator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/swagger-codegen-orchestrator/
