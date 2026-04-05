---
name: "Spectral OpenAPI and AsyncAPI Linter"
description: "Spectral is an open-source JSON/YAML linter by Stoplight with built-in support for OpenAPI 3.x, Swagger 2.0, AsyncAPI 2.x, and Arazzo 1.0. It enforces API style guides through custom and pre-built rulesets, ensuring consistency across all your API descriptions."
category: "Code Quality & Review"
framework: "Claude Code"
verification: security_reviewed
source: "https://github.com/stoplightio/spectral"
tool_ecosystem:
  tool: spectral
  github_repo: stoplightio/spectral
  github_stars: 3057
---
# Spectral OpenAPI and AsyncAPI Linter

Spectral is an open-source JSON/YAML linter by Stoplight with built-in support for OpenAPI 3.x, Swagger 2.0, AsyncAPI 2.x, and Arazzo 1.0. It enforces API style guides through custom and pre-built rulesets, ensuring consistency across all your API descriptions.

## Overview

Spectral is a flexible, open-source linter from Stoplight designed for validating and enforcing style guides on JSON and YAML files, with first-class support for OpenAPI (v3.1, v3.0, v2.0), AsyncAPI v2.x, and Arazzo v1.0 specifications. With over 3,000 GitHub stars and an active npm package (@stoplight/spectral-cli), Spectral has become the industry standard for API governance and quality enforcement in CI/CD pipelines.

The tool works by applying rulesets — collections of rules defined in YAML, JSON, or JavaScript/TypeScript — against your API description files. Out of the box, Spectral ships with curated rulesets for OpenAPI and AsyncAPI that catch common mistakes like missing descriptions, invalid schema references, unused components, and non-standard status codes. You can extend these with your own custom rules and functions to enforce organization-specific API design standards, turning tribal knowledge into automated checks.

Spectral is distributed as a CLI tool via npm, a Docker image, and a JavaScript/TypeScript library for programmatic use. Installation is straightforward with `npm install -g @stoplight/spectral-cli`, and linting is as simple as running `spectral lint openapi.yaml`. The tool integrates with VS Code via a dedicated extension, GitHub Actions for automated PR checks, and any CI system that runs Node.js. Jetbrains IDE plugins are also available.

For teams building API-first products, Spectral outputs machine-readable results in multiple formats (JSON, JUnit, HTML, SARIF) making it easy to integrate into existing quality gates. Custom functions written in JavaScript or TypeScript allow for advanced validation logic like checking naming conventions, enforcing pagination patterns, or validating security scheme configurations. The extensible ruleset system means rulesets can inherit from and extend others, enabling layered governance across teams and organizations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill spectral-openapi-asyncapi-linter
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill spectral-openapi-asyncapi-linter -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill spectral-openapi-asyncapi-linter -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill spectral-openapi-asyncapi-linter -a codex
```

### OpenClaw

```bash
clawhub install spectral-openapi-asyncapi-linter
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/spectral-openapi-asyncapi-linter/)
