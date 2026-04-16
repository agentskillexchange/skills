---
title: "Bootstrap an OpenAPI spec from captured API traffic before client or test automation starts"
description: "Uses mitmproxy2swagger to turn captured mitmproxy flows or HAR exports into a first-pass OpenAPI document that an agent can refine, validate, and hand off to downstream tooling. Invoke it when the API already exists but the contract does not, and you need a concrete spec before generating clients, mocks, tests, or reviewable docs."
verification: "security_reviewed"
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

This skill uses mitmproxy2swagger as a bounded reverse-engineering workflow for undocumented HTTP APIs. The tool converts captured mitmproxy flow files or browser-exported HAR files into an OpenAPI 3.0 schema, which gives an agent a concrete starting point instead of a pile of ad hoc request logs. The valuable job here is not “use an API tool.” It is “bootstrap a usable contract from real traffic so later automation has something structured to work from.”

Invoke this when a team has a live API, mobile app backend, or internal service that is already being called in the wild, but there is no trustworthy spec to generate a client, create mocks, write contract tests, or diff future changes. An agent can capture representative traffic, run the first pass, review and clean the generated x-path-templates, then rerun the tool to materialize endpoint descriptions and optional examples. That makes it useful before SDK generation, before Schemathesis or Prism-style testing, before documentation backfills, and before integration teams start guessing at request shapes.

The scope boundary matters. This is not a generic API platform entry, a documentation portal, or a full lifecycle governance tool. It is specifically for creating a first-pass OpenAPI document from observed traffic. Its output becomes input for other systems, but the skill itself stops at traffic capture, schema generation, and targeted cleanup. Integration points include mitmproxy, browser DevTools HAR export, OpenAPI validators, client generators, mock servers, and CI pipelines that want a contract artifact to version and review.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/bootstrap-openapi-spec-from-captured-api-traffic-before-client-or-test-automation/)
