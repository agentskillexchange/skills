---
title: "OpenAPI Spec Validator"
description: "Validates and lints OpenAPI 3.0/3.1 specifications using Spectral CLI rules and the Swagger Parser library. Detects breaking changes between spec versions and generates migration guides."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/openapi-spec-validator-agent/"
category:
  - "Developer Tools"
framework:
  - "Custom Agents"
---

# OpenAPI Spec Validator

The OpenAPI Spec Validator skill performs comprehensive validation of OpenAPI 3.0 and 3.1 specifications using the Spectral CLI linting engine with custom and built-in rulesets. It parses specifications using the Swagger Parser library to resolve $ref references, validate schema correctness, and detect circular references. The skill compares specification versions to identify breaking changes including removed endpoints, narrowed parameter types, and new required fields using the oasdiff library. Features include custom Spectral rule authoring for organization-specific API standards, security scheme validation against OWASP API Security Top 10, and automated SDK generation compatibility checking. Supports bulk validation across API gateway configurations, mock server generation from examples using Prism, and API documentation quality scoring based on description coverage and example completeness.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openapi-spec-validator-agent/)
