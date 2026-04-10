---
title: "OpenAPI Spec Reference Generator"
description: "Converts OpenAPI 3.x specification files into browsable API reference documentation using swagger-parser and redoc-cli. Generates static HTML, markdown, and Postman collection exports from YAML/JSON spec files."
slug: "openapi-spec-reference-generator"
category:
  - "Library &amp; API Reference"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/openapi-spec-reference-generator/"
listed: true
---

# OpenAPI Spec Reference Generator

Converts OpenAPI 3.x specification files into browsable API reference documentation using swagger-parser and redoc-cli. Generates static HTML, markdown, and Postman collection exports from YAML/JSON spec files.

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
clawhub install openapi-spec-reference-generator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The OpenAPI Spec Reference Generator transforms OpenAPI 3.x specifications into comprehensive, browsable API reference documentation. It uses the swagger-parser library for spec validation and dereferencing of $ref pointers.
Documentation generation leverages redoc-cli to produce responsive static HTML pages with interactive try-it-out panels, authentication configuration, and code sample generation in multiple languages. The skill also exports Postman Collection v2.1 format for direct import into Postman workspaces.
The generator supports multi-file spec resolution, automatically resolving external $ref references across split specification files. It validates specs against the OpenAPI 3.0 and 3.1 standards, reporting structural errors and suggesting fixes.
Additional output formats include markdown suitable for GitHub wiki pages, Docusaurus MDX components, and Slate-compatible documentation. The skill handles custom x-extensions, webhook definitions, and link objects for HATEOAS-style API documentation with navigable resource relationships.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openapi-spec-reference-generator/)
