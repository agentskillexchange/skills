---
title: "OpenAPI Spec Validator"
description: "Validates and lints OpenAPI 3.0/3.1 specifications using Spectral CLI rules and the Swagger Parser library. Detects breaking changes between spec versions and generates migration guides."
verification: "security_reviewed"
source: "https://github.com/stoplightio/spectral"
category:
  - "Developer Tools"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "stoplightio/spectral"
  github_stars: 3084
  npm_package: "@stoplight/spectral-cli"
  npm_weekly_downloads: 1165411
---

# OpenAPI Spec Validator

The OpenAPI Spec Validator skill performs comprehensive validation of OpenAPI 3.0 and 3.1 specifications using the Spectral CLI linting engine with custom and built-in rulesets. It parses specifications using the Swagger Parser library to resolve $ref references, validate schema correctness, and detect circular references. The skill compares specification versions to identify breaking changes including removed endpoints, narrowed parameter types, and new required fields using the oasdiff library. Features include custom Spectral rule authoring for organization-specific API standards, security scheme validation against OWASP API Security Top 10, and automated SDK generation compatibility checking. Supports bulk validation across API gateway configurations, mock server generation from examples using Prism, and API documentation quality scoring based on description coverage and example completeness.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/openapi-spec-validator-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/openapi-spec-validator-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/openapi-spec-validator-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openapi-spec-validator-agent/)
