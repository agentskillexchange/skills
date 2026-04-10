---
title: "OpenAPI Spec Validator"
description: "Validates and lints OpenAPI 3.0/3.1 specifications using Spectral CLI rules and the Swagger Parser library. Detects breaking changes between spec versions and generates migration guides."
slug: "openapi-spec-validator-agent"
category:
  - "Developer Tools"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/openapi-spec-validator-agent/"
---

# OpenAPI Spec Validator

Validates and lints OpenAPI 3.0/3.1 specifications using Spectral CLI rules and the Swagger Parser library. Detects breaking changes between spec versions and generates migration guides.

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
clawhub install openapi-spec-validator-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The OpenAPI Spec Validator skill performs comprehensive validation of OpenAPI 3.0 and 3.1 specifications using the Spectral CLI linting engine with custom and built-in rulesets. It parses specifications using the Swagger Parser library to resolve $ref references, validate schema correctness, and detect circular references. The skill compares specification versions to identify breaking changes including removed endpoints, narrowed parameter types, and new required fields using the oasdiff library. Features include custom Spectral rule authoring for organization-specific API standards, security scheme validation against OWASP API Security Top 10, and automated SDK generation compatibility checking. Supports bulk validation across API gateway configurations, mock server generation from examples using Prism, and API documentation quality scoring based on description coverage and example completeness.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openapi-spec-validator-agent/)
