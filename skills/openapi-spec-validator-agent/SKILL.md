---
name: "OpenAPI Spec Validator"
description: "Validates and lints OpenAPI 3.0/3.1 specifications using Spectral CLI rules and the Swagger Parser library. Detects breaking changes between spec versions and generates migration guides."
category: "Developer Tools"
framework: "Custom Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/openapi-spec-validator-agent/"
---
# OpenAPI Spec Validator

Validates and lints OpenAPI 3.0/3.1 specifications using Spectral CLI rules and the Swagger Parser library. Detects breaking changes between spec versions and generates migration guides.

## Overview

The OpenAPI Spec Validator skill performs comprehensive validation of OpenAPI 3.0 and 3.1 specifications using the Spectral CLI linting engine with custom and built-in rulesets. It parses specifications using the Swagger Parser library to resolve $ref references, validate schema correctness, and detect circular references. The skill compares specification versions to identify breaking changes including removed endpoints, narrowed parameter types, and new required fields using the oasdiff library. Features include custom Spectral rule authoring for organization-specific API standards, security scheme validation against OWASP API Security Top 10, and automated SDK generation compatibility checking. Supports bulk validation across API gateway configurations, mock server generation from examples using Prism, and API documentation quality scoring based on description coverage and example completeness.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill openapi-spec-validator-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill openapi-spec-validator-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill openapi-spec-validator-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill openapi-spec-validator-agent -a codex
```

### OpenClaw

```bash
clawhub install openapi-spec-validator-agent
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openapi-spec-validator-agent/)
