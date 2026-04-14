---
title: "Bootstrap an OpenAPI spec from captured API traffic before client or test automation starts"
slug: "bootstrap-openapi-spec-from-captured-api-traffic-before-client-or-test-automation"
verification: security_reviewed
source: "https://github.com/alufers/mitmproxy2swagger"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "alufers/mitmproxy2swagger"
  github_stars: 9347
---
# Bootstrap an OpenAPI spec from captured API traffic before client or test automation starts

Uses mitmproxy2swagger to turn captured mitmproxy flows or HAR exports into a first-pass OpenAPI document that an agent can refine, validate, and hand off to downstream tooling. Invoke it when the API already exists but the contract does not, and you need a concrete spec before generating clients, mocks, tests, or reviewable docs.

## Installation

Choose the method that fits your setup:

1. Install from Agent Skill Exchange
2. Clone or download the upstream project
3. Install with the upstream package manager
4. Add the skill to your local skills directory
5. Follow the upstream documentation for environment-specific setup

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/bootstrap-openapi-spec-from-captured-api-traffic-before-client-or-test-automation/)
