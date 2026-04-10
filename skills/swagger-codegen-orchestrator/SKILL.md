---
title: "Swagger Codegen Orchestrator"
description: "Orchestrates OpenAPI 3.x code generation using swagger-codegen-cli and openapi-generator. Produces typed client SDKs for TypeScript, Python, and Go with custom Mustache templates."
slug: "swagger-codegen-orchestrator"
category:
  - "Templates &amp; Workflows"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/swagger-codegen-orchestrator/"
---

# Swagger Codegen Orchestrator

Orchestrates OpenAPI 3.x code generation using swagger-codegen-cli and openapi-generator. Produces typed client SDKs for TypeScript, Python, and Go with custom Mustache templates.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install swagger-codegen-orchestrator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Swagger Codegen Orchestrator streamlines API client generation from OpenAPI 3.x specifications. It wraps swagger-codegen-cli and openapi-generator to produce strongly typed client SDKs across TypeScript, Python, and Go targets. The tool supports custom Mustache template overrides for controlling generated code style, error handling patterns, and authentication flows. It reads OpenAPI specs from local files, URLs, or directly from Swagger Hub via the SwaggerHub API. For TypeScript targets, it generates axios-based clients with full type inference and automatic retry logic using axios-retry. Python clients use httpx with async support and Pydantic v2 models for request/response validation. Go clients leverage net/http with context propagation and structured error types. The orchestrator handles multi-spec scenarios where microservices expose separate APIs, merging them into a unified SDK with proper namespace isolation and shared model deduplication.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/swagger-codegen-orchestrator/)
