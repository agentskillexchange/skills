---
title: "Scalar OpenAPI Reference and API Client Platform"
description: "Scalar is an open-source API platform for publishing modern OpenAPI references and testing endpoints with a built-in API client. It fits agent workflows that need readable API docs, interactive request testing, and framework-friendly integrations across many stacks."
verification: "security_reviewed"
source: "https://github.com/scalar/scalar"
category:
  - "Library & API Reference"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "scalar/scalar"
  github_stars: 14624
  license: "MIT"
---

# Scalar OpenAPI Reference and API Client Platform

Scalar is an open-source API platform built around OpenAPI and Swagger documents. It gives teams a modern API reference UI, an offline-first API client, and a registry-style workflow for managing machine-readable specs. For agent builders and developers, the main job-to-be-done is straightforward: turn an OpenAPI document into a reference that humans can read, explore, and test without sending people into a cluttered legacy docs interface.


The project supports a broad integration surface. Its README documents HTML/JavaScript embedding plus integrations for ASP.NET Core, Django, Express, FastAPI, Laravel, NestJS, Next.js, React, Spring Boot, Vue, and more. That makes it useful when an agent needs to expose or consume an API contract in mixed environments instead of being locked to one framework. The quickstart uses the @scalar/api-reference package from jsDelivr and initializes the UI against an OpenAPI URL, which is simple to automate in CI, docs portals, or generated developer hubs.


Scalar also ships a browser-based API client and managed hosting options, so the same upstream tool can cover documentation publishing, request testing, and API onboarding. The upstream project is actively maintained on GitHub, carries an MIT license, and links to full product documentation at docs.scalar.com. For ASE, this skill is a strong fit for teams that want to publish polished API references, validate OpenAPI-driven workflows, and provide a better developer experience around existing REST services.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scalar-openapi-reference-api-client-platform/)
