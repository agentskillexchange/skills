---
title: "OpenAPI Spec Validator"
description: "Validates and lints OpenAPI 3.0/3.1 specifications using Spectral CLI rules and the Swagger Parser library. Detects breaking changes between spec versions and generates migration guides."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/openapi-spec-validator-agent/"
category:
  - "Developer Tools"
framework:
  - "Custom Agents"
---

# OpenAPI Spec Validator

The OpenAPI Spec Validator skill performs comprehensive validation of OpenAPI 3.0 and 3.1 specifications using the Spectral CLI linting engine with custom and built-in rulesets. It parses specifications using the Swagger Parser library to resolve $ref references, validate schema correctness, and detect circular references. The skill compares specification versions to identify breaking changes including removed endpoints, narrowed parameter types, and new required fields using the oasdiff library. Features include custom Spectral rule authoring for organization-specific API standards, security scheme validation against OWASP API Security Top 10, and automated SDK generation compatibility checking. Supports bulk validation across API gateway configurations, mock server generation from examples using Prism, and API documentation quality scoring based on description coverage and example completeness.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/openapi-spec-validator-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/openapi-spec-validator-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openapi-spec-validator-agent/)
