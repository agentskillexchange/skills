---
title: "Swagger Codegen Orchestrator"
description: "Orchestrates OpenAPI 3.x code generation using swagger-codegen-cli and openapi-generator. Produces typed client SDKs for TypeScript, Python, and Go with custom Mustache templates."
verification: security_reviewed
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
---

# Swagger Codegen Orchestrator

The Swagger Codegen Orchestrator streamlines API client generation from OpenAPI 3.x specifications. It wraps swagger-codegen-cli and openapi-generator to produce strongly typed client SDKs across TypeScript, Python, and Go targets. The tool supports custom Mustache template overrides for controlling generated code style, error handling patterns, and authentication flows. It reads OpenAPI specs from local files, URLs, or directly from Swagger Hub via the SwaggerHub API. For TypeScript targets, it generates axios-based clients with full type inference and automatic retry logic using axios-retry. Python clients use httpx with async support and Pydantic v2 models for request/response validation. Go clients leverage net/http with context propagation and structured error types. The orchestrator handles multi-spec scenarios where microservices expose separate APIs, merging them into a unified SDK with proper namespace isolation and shared model deduplication.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/swagger-codegen-orchestrator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/swagger-codegen-orchestrator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/swagger-codegen-orchestrator/)
