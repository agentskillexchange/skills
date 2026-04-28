---
title: Bootstrap an OpenAPI spec from captured API traffic before client or test automation
  starts
description: Uses mitmproxy2swagger to turn captured mitmproxy flows or HAR exports
  into a first-pass OpenAPI document that an agent can refine, validate, and hand
  off to downstream tooling. Invoke it when the API already exists but the contract
  does not, and you need a concrete spec before generating clients, mocks, tests,
  or reviewable docs.
verification: security_reviewed
source: https://github.com/alufers/mitmproxy2swagger
category:
- Integrations & Connectors
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: alufers/mitmproxy2swagger
  github_stars: 9347
---

# Bootstrap an OpenAPI spec from captured API traffic before client or test automation starts

Uses mitmproxy2swagger to turn captured mitmproxy flows or HAR exports into a first-pass OpenAPI document that an agent can refine, validate, and hand off to downstream tooling. Invoke it when the API already exists but the contract does not, and you need a concrete spec before generating clients, mocks, tests, or reviewable docs.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/bootstrap-openapi-spec-from-captured-api-traffic-before-client-or-test-automation/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/bootstrap-openapi-spec-from-captured-api-traffic-before-client-or-test-automation
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/bootstrap-openapi-spec-from-captured-api-traffic-before-client-or-test-automation`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/bootstrap-openapi-spec-from-captured-api-traffic-before-client-or-test-automation/)
