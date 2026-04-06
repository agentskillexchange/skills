---
name: Swagger Codegen Orchestrator
description: Orchestrates OpenAPI 3.x code generation using swagger-codegen-cli and
  openapi-generator. Produces typed client SDKs for TypeScript, Python, and Go with
  custom Mustache templates.
category: "Templates &amp; Workflows"
framework: Claude Code
verification: security_reviewed
source: "https://agentskillexchange.com/skills/swagger-codegen-orchestrator/"
---
# Swagger Codegen Orchestrator

Orchestrates OpenAPI 3.x code generation using swagger-codegen-cli and openapi-generator. Produces typed client SDKs for TypeScript, Python, and Go with custom Mustache templates.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/swagger-codegen-orchestrator/)
