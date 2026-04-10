---
title: "Swagger Codegen Template Customizer"
description: "Extends Swagger Codegen and OpenAPI Generator with custom Mustache templates for client SDK generation. Supports Java (OkHttp/Retrofit), TypeScript (Axios/Fetch), and Python (httpx) output targets."
slug: "swagger-codegen-template-customizer"
category:
  - "Library &amp; API Reference"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/swagger-codegen-template-customizer/"
---

# Swagger Codegen Template Customizer

Extends Swagger Codegen and OpenAPI Generator with custom Mustache templates for client SDK generation. Supports Java (OkHttp/Retrofit), TypeScript (Axios/Fetch), and Python (httpx) output targets.

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
clawhub install swagger-codegen-template-customizer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Swagger Codegen Template Customizer streamlines client SDK generation by providing an intelligent layer on top of OpenAPI Generator CLI. It analyzes your OpenAPI 3.x specification and generates customized Mustache templates that produce production-ready client libraries tailored to your project’s conventions and framework choices.
The customizer supports multiple language targets: Java with OkHttp or Retrofit adapters, TypeScript with Axios or native Fetch implementations, Python with httpx async support, and Go with configurable HTTP client backends. For each target, it generates proper error handling hierarchies, retry logic with exponential backoff, request/response interceptors for authentication, and type-safe model classes with JSON serialization annotations.
Advanced features include: automatic pagination helper generation for list endpoints, WebSocket client stubs for async API endpoints, multipart upload utilities with progress callbacks, and mock server generation using Prism for testing. The agent validates generated code against language-specific linters (ESLint, pylint, checkstyle) and can publish packages to npm, PyPI, or Maven Central via their respective APIs. Supports monorepo output with shared type definitions.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/swagger-codegen-template-customizer/)
