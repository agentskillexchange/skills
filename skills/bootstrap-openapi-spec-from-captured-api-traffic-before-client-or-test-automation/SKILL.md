---
title: "Bootstrap an OpenAPI spec from captured API traffic before client or test automation starts"
description: "Uses mitmproxy2swagger to turn captured mitmproxy flows or HAR exports into a first-pass OpenAPI document that an agent can refine, validate, and hand off to downstream tooling. Invoke it when the API already exists but the contract does not, and you need a concrete spec before generating clients, mocks, tests, or reviewable docs."
verification: security_reviewed
source: "https://github.com/alufers/mitmproxy2swagger"
category:
  - "Integrations &amp; Connectors"
---

# Bootstrap an OpenAPI spec from captured API traffic before client or test automation starts

Uses mitmproxy2swagger to turn captured mitmproxy flows or HAR exports into a first-pass OpenAPI document that an agent can refine, validate, and hand off to downstream tooling. Invoke it when the API already exists but the contract does not, and you need a concrete spec before generating clients, mocks, tests, or reviewable docs.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/bootstrap-openapi-spec-from-captured-api-traffic-before-client-or-test-automation/)
