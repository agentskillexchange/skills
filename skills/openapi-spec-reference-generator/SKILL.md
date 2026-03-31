---
name: "OpenAPI Spec Reference Generator"
description: "Converts OpenAPI 3.x specification files into browsable API reference documentation using swagger-parser and redoc-cli. Generates static HTML, markdown, and Postman collection exports from YAML/JSON spec files."
category: "Library &amp; API Reference"
framework: "Cursor"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/openapi-spec-reference-generator/"
---
# OpenAPI Spec Reference Generator

Converts OpenAPI 3.x specification files into browsable API reference documentation using swagger-parser and redoc-cli. Generates static HTML, markdown, and Postman collection exports from YAML/JSON spec files.

## Overview

The OpenAPI Spec Reference Generator transforms OpenAPI 3.x specifications into comprehensive, browsable API reference documentation. It uses the swagger-parser library for spec validation and dereferencing of $ref pointers.

Documentation generation leverages redoc-cli to produce responsive static HTML pages with interactive try-it-out panels, authentication configuration, and code sample generation in multiple languages. The skill also exports Postman Collection v2.1 format for direct import into Postman workspaces.

The generator supports multi-file spec resolution, automatically resolving external $ref references across split specification files. It validates specs against the OpenAPI 3.0 and 3.1 standards, reporting structural errors and suggesting fixes.

Additional output formats include markdown suitable for GitHub wiki pages, Docusaurus MDX components, and Slate-compatible documentation. The skill handles custom x-extensions, webhook definitions, and link objects for HATEOAS-style API documentation with navigable resource relationships.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill openapi-spec-reference-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill openapi-spec-reference-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill openapi-spec-reference-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill openapi-spec-reference-generator -a codex
```

### OpenClaw

```bash
clawhub install openapi-spec-reference-generator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openapi-spec-reference-generator/)
