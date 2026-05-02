---
title: "Bootstrap an OpenAPI spec from captured API traffic before client or test automation starts"
description: "Uses mitmproxy2swagger to turn captured mitmproxy flows or HAR exports into a first-pass OpenAPI document that an agent can refine, validate, and hand off to downstream tooling. Invoke it when the API already exists but the contract does not, and you need a concrete spec before generating clients, mocks, tests, or reviewable docs."
verification: "security_reviewed"
source: "https://github.com/alufers/mitmproxy2swagger"
author: "alufers"
publisher_type: "Individual Maintainer"
category:
  - "Integrations & Connectors"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "alufers/mitmproxy2swagger"
  github_stars: 9347
---

# Bootstrap an OpenAPI spec from captured API traffic before client or test automation starts

Uses mitmproxy2swagger to turn captured mitmproxy flows or HAR exports into a first-pass OpenAPI document that an agent can refine, validate, and hand off to downstream tooling. Invoke it when the API already exists but the contract does not, and you need a concrete spec before generating clients, mocks, tests, or reviewable docs.

## Prerequisites

Python 3 and pip, plus mitmproxy flow captures or a HAR export from browser DevTools

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
pip install mitmproxy2swagger
```

## Documentation

- https://github.com/alufers/mitmproxy2swagger

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/bootstrap-openapi-spec-from-captured-api-traffic-before-client-or-test-automation/)
