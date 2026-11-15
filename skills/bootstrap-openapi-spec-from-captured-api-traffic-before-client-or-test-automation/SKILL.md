---
name: "Bootstrap an OpenAPI spec from captured API traffic before client or test automation starts"
slug: "bootstrap-openapi-spec-from-captured-api-traffic-before-client-or-test-automation"
description: "Uses mitmproxy2swagger to turn captured mitmproxy flows or HAR exports into a first-pass OpenAPI document that an agent can refine, validate, and hand off to downstream tooling. Invoke it when the API already exists but the contract does not, and you need a concrete spec before generating clients, mocks, tests, or reviewable docs."
github_stars: 9347
verification: "security_reviewed"
source: "https://github.com/alufers/mitmproxy2swagger"
author: "alufers"
publisher_type: "Individual Maintainer"
category: "Integrations & Connectors"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "alufers/mitmproxy2swagger"
  github_stars: 9347
---

# Bootstrap an OpenAPI spec from captured API traffic before client or test automation starts

Uses mitmproxy2swagger to turn captured mitmproxy flows or HAR exports into a first-pass OpenAPI document that an agent can refine, validate, and hand off to downstream tooling. Invoke it when the API already exists but the contract does not, and you need a concrete spec before generating clients, mocks, tests, or reviewable docs.

## Prerequisites

Python 3 and pip, plus mitmproxy flow captures or a HAR export from browser DevTools

## Installation

Use the upstream install or setup path that matches your environment:
- $ pip install mitmproxy2swagger
- $ git clone git@github.com:alufers/mitmproxy2swagger.git
- $ docker build -t mitmproxy2swagger .
- $ docker run -it -v $PWD:/app mitmproxy2swagger mitmproxy2swagger -i <path_to_mitmptoxy_flow> -o <path_to_output_schema> -p <api_prefix>

Requirements and caveats from upstream:
- [poetry](https://python-poetry.org/) for dependency management

Basic usage or getting-started notes:
- First you will need python3 and pip3.
- bash
- # ... or ...

- Source: https://github.com/alufers/mitmproxy2swagger
- Extracted from upstream docs: https://raw.githubusercontent.com/alufers/mitmproxy2swagger/HEAD/README.md

## Documentation

- https://github.com/alufers/mitmproxy2swagger

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/bootstrap-openapi-spec-from-captured-api-traffic-before-client-or-test-automation/)
