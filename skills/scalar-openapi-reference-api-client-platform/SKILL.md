---
title: "Scalar OpenAPI Reference and API Client Platform"
description: "Scalar is an open-source API platform for publishing modern OpenAPI references and testing endpoints with a built-in API client. It fits agent workflows that need readable API docs, interactive request testing, and framework-friendly integrations across many stacks."
slug: "scalar-openapi-reference-api-client-platform"
category:
  - "Library &amp; API Reference"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/scalar/scalar"
listed: true
---

# Scalar OpenAPI Reference and API Client Platform

Scalar is an open-source API platform for publishing modern OpenAPI references and testing endpoints with a built-in API client. It fits agent workflows that need readable API docs, interactive request testing, and framework-friendly integrations across many stacks.

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
clawhub install scalar-openapi-reference-api-client-platform
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Scalar is an open-source API platform built around OpenAPI and Swagger documents. It gives teams a modern API reference UI, an offline-first API client, and a registry-style workflow for managing machine-readable specs. For agent builders and developers, the main job-to-be-done is straightforward: turn an OpenAPI document into a reference that humans can read, explore, and test without sending people into a cluttered legacy docs interface.
The project supports a broad integration surface. Its README documents HTML/JavaScript embedding plus integrations for ASP.NET Core, Django, Express, FastAPI, Laravel, NestJS, Next.js, React, Spring Boot, Vue, and more. That makes it useful when an agent needs to expose or consume an API contract in mixed environments instead of being locked to one framework. The quickstart uses the @scalar/api-reference package from jsDelivr and initializes the UI against an OpenAPI URL, which is simple to automate in CI, docs portals, or generated developer hubs.
Scalar also ships a browser-based API client and managed hosting options, so the same upstream tool can cover documentation publishing, request testing, and API onboarding. The upstream project is actively maintained on GitHub, carries an MIT license, and links to full product documentation at docs.scalar.com. For ASE, this skill is a strong fit for teams that want to publish polished API references, validate OpenAPI-driven workflows, and provide a better developer experience around existing REST services.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scalar-openapi-reference-api-client-platform/)
