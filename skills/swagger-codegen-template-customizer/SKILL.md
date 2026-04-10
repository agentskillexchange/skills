---
name: Swagger Codegen Template Customizer
description: Extends Swagger Codegen and OpenAPI Generator with custom Mustache templates
  for client SDK generation. Supports Java (OkHttp/Retrofit), TypeScript (Axios/Fetch),
  and Python (httpx) output targets.
verification: security_reviewed
source: https://agentskillexchange.com/skills/swagger-codegen-template-customizer/
category:
- Library &amp; API Reference
framework:
- ChatGPT Agents
---
# Swagger Codegen Template Customizer

The Swagger Codegen Template Customizer streamlines client SDK generation by providing an intelligent layer on top of OpenAPI Generator CLI. It analyzes your OpenAPI 3.x specification and generates customized Mustache templates that produce production-ready client libraries tailored to your project's conventions and framework choices.
The customizer supports multiple language targets: Java with OkHttp or Retrofit adapters, TypeScript with Axios or native Fetch implementations, Python with httpx async support, and Go with configurable HTTP client backends. For each target, it generates proper error handling hierarchies, retry logic with exponential backoff, request/response interceptors for authentication, and type-safe model classes with JSON serialization annotations.
Advanced features include: automatic pagination helper generation for list endpoints, WebSocket client stubs for async API endpoints, multipart upload utilities with progress callbacks, and mock server generation using Prism for testing. The agent validates generated code against language-specific linters (ESLint, pylint, checkstyle) and can publish packages to npm, PyPI, or Maven Central via their respective APIs. Supports monorepo output with shared type definitions.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/swagger-codegen-template-customizer/)
