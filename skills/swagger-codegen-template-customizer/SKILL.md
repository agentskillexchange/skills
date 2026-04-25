---
title: "Swagger Codegen Template Customizer"
description: "Extends Swagger Codegen and OpenAPI Generator with custom Mustache templates for client SDK generation. Supports Java (OkHttp/Retrofit), TypeScript (Axios/Fetch), and Python (httpx) output targets."
verification: "security_reviewed"
source: "https://github.com/swagger-api/swagger-ui"
category:
  - "Library & API Reference"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "swagger-api/swagger-ui"
  github_stars: 28751
  npm_package: "swagger-ui"
  npm_weekly_downloads: 149194
---

# Swagger Codegen Template Customizer

The Swagger Codegen Template Customizer streamlines client SDK generation by providing an intelligent layer on top of OpenAPI Generator CLI. It analyzes your OpenAPI 3.x specification and generates customized Mustache templates that produce production-ready client libraries tailored to your project’s conventions and framework choices. The customizer supports multiple language targets: Java with OkHttp or Retrofit adapters, TypeScript with Axios or native Fetch implementations, Python with httpx async support, and Go with configurable HTTP client backends. For each target, it generates proper error handling hierarchies, retry logic with exponential backoff, request/response interceptors for authentication, and type-safe model classes with JSON serialization annotations. Advanced features include: automatic pagination helper generation for list endpoints, WebSocket client stubs for async API endpoints, multipart upload utilities with progress callbacks, and mock server generation using Prism for testing. The agent validates generated code against language-specific linters (ESLint, pylint, checkstyle) and can publish packages to npm, PyPI, or Maven Central via their respective APIs. Supports monorepo output with shared type definitions.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/swagger-codegen-template-customizer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/swagger-codegen-template-customizer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/swagger-codegen-template-customizer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/swagger-codegen-template-customizer/)
