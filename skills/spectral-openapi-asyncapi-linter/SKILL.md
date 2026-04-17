---
title: "Spectral OpenAPI and AsyncAPI Linter"
description: "Spectral is a flexible, open-source linter from Stoplight designed for validating and enforcing style guides on JSON and YAML files, with first-class support for OpenAPI (v3.1, v3.0, v2.0), AsyncAPI v2.x, and Arazzo v1.0 specifications. With over 3,000 GitHub stars and an active npm package (@stoplight/spectral-cli), Spectral has become the industry standard for API governance and quality enforcement in CI/CD pipelines.\nThe tool works by applying rulesets — collections of rules defined in YAML, JSON, or JavaScript/TypeScript — against your API description files. Out of the box, Spectral ships with curated rulesets for OpenAPI and AsyncAPI that catch common mistakes like missing descriptions, invalid schema references, unused components, and non-standard status codes. You can extend these with your own custom rules and functions to enforce organization-specific API design standards, turning tribal knowledge into automated checks.\nSpectral is distributed as a CLI tool via npm, a Docker image, and a JavaScript/TypeScript library for programmatic use. Installation is straightforward with npm install -g @stoplight/spectral-cli, and linting is as simple as running spectral lint openapi.yaml. The tool integrates with VS Code via a dedicated extension, GitHub Actions for automated PR checks, and any CI system that runs Node.js. Jetbrains IDE plugins are also available.\nFor teams building API-first products, Spectral outputs machine-readable results in multiple formats (JSON, JUnit, HTML, SARIF) making it easy to integrate into existing quality gates. Custom functions written in JavaScript or TypeScript allow for advanced validation logic like checking naming conventions, enforcing pagination patterns, or validating security scheme configurations. The extensible ruleset system means rulesets can inherit from and extend others, enabling layered governance across teams and organizations."
verification: security_reviewed
source: "https://github.com/stoplightio/spectral"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "stoplightio/spectral"
  github_stars: 3057
---

# Spectral OpenAPI and AsyncAPI Linter

Spectral is a flexible, open-source linter from Stoplight designed for validating and enforcing style guides on JSON and YAML files, with first-class support for OpenAPI (v3.1, v3.0, v2.0), AsyncAPI v2.x, and Arazzo v1.0 specifications. With over 3,000 GitHub stars and an active npm package (@stoplight/spectral-cli), Spectral has become the industry standard for API governance and quality enforcement in CI/CD pipelines.
The tool works by applying rulesets — collections of rules defined in YAML, JSON, or JavaScript/TypeScript — against your API description files. Out of the box, Spectral ships with curated rulesets for OpenAPI and AsyncAPI that catch common mistakes like missing descriptions, invalid schema references, unused components, and non-standard status codes. You can extend these with your own custom rules and functions to enforce organization-specific API design standards, turning tribal knowledge into automated checks.
Spectral is distributed as a CLI tool via npm, a Docker image, and a JavaScript/TypeScript library for programmatic use. Installation is straightforward with npm install -g @stoplight/spectral-cli, and linting is as simple as running spectral lint openapi.yaml. The tool integrates with VS Code via a dedicated extension, GitHub Actions for automated PR checks, and any CI system that runs Node.js. Jetbrains IDE plugins are also available.
For teams building API-first products, Spectral outputs machine-readable results in multiple formats (JSON, JUnit, HTML, SARIF) making it easy to integrate into existing quality gates. Custom functions written in JavaScript or TypeScript allow for advanced validation logic like checking naming conventions, enforcing pagination patterns, or validating security scheme configurations. The extensible ruleset system means rulesets can inherit from and extend others, enabling layered governance across teams and organizations.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/spectral-openapi-asyncapi-linter
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/spectral-openapi-asyncapi-linter` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/spectral-openapi-asyncapi-linter/)
