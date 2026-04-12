---
title: "Bootstrap an OpenAPI spec from captured API traffic before client or test automation starts"
description: "Uses mitmproxy2swagger to turn captured mitmproxy flows or HAR exports into a first-pass OpenAPI document that an agent can refine, validate, and hand off to downstream tooling. Invoke it when the API already exists but the contract does not, and you need a concrete spec before generating clients, mocks, tests, or reviewable docs."
verification: security_reviewed
source: "https://github.com/alufers/mitmproxy2swagger"
---

# Bootstrap an OpenAPI spec from captured API traffic before client or test automation starts

Uses mitmproxy2swagger to turn captured mitmproxy flows or HAR exports into a first-pass OpenAPI document that an agent can refine, validate, and hand off to downstream tooling. Invoke it when the API already exists but the contract does not, and you need a concrete spec before generating clients, mocks, tests, or reviewable docs.

## Installation

Choose the path that fits your setup:

1. Clone this repository and use the skill locally.
2. Copy the skill folder into your local skills directory.
3. Add the skill as a Git submodule in your skills workspace.
4. Vendor the files into an internal skill catalog for your team.
5. Reference the upstream source and recreate the skill in your own agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/bootstrap-openapi-spec-from-captured-api-traffic-before-client-or-test-automation/)
