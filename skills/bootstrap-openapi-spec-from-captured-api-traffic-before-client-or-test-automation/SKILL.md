---
title: "Bootstrap an OpenAPI spec from captured API traffic before client or test automation starts"
description: "This skill uses mitmproxy2swagger as a bounded reverse-engineering workflow for undocumented HTTP APIs. The tool converts captured mitmproxy flow files or browser-exported HAR files into an OpenAPI 3.0 schema, which gives an agent a concrete starting point instead of a pile of ad hoc request logs. The valuable job here is not “use an API tool.” It is “bootstrap a usable contract from real traffic so later automation has something structured to work from.” Invoke this when a team has a live API, mobile app backend, or internal service that is already being called in the wild, but there is no trustworthy spec to generate a client, create mocks, write contract tests, or diff future changes. An agent can capture representative traffic, run the first pass, review and clean the generated x-path-templates , then rerun the tool to materialize endpoint descriptions and optional examples. That makes it useful before SDK generation, before Schemathesis or Prism-style testing, before documentation backfills, and before integration teams start guessing at request shapes. The scope boundary matters. This is not a generic API platform entry, a documentation portal, or a full lifecycle governance tool. It is specifically for creating a first-pass OpenAPI document from observed traffic. Its output becomes input for other systems, but the skill itself stops at traffic capture, schema generation, and targeted cleanup. Integration points include mitmproxy, browser DevTools HAR export, OpenAPI validators, client generators, mock servers, and CI pipelines that want a contract artifact to version and review."
source: "https://github.com/alufers/mitmproxy2swagger"
verification: "security_reviewed"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "alufers/mitmproxy2swagger"
  github_stars: 9347
---

# Bootstrap an OpenAPI spec from captured API traffic before client or test automation starts

This skill uses mitmproxy2swagger as a bounded reverse-engineering workflow for undocumented HTTP APIs. The tool converts captured mitmproxy flow files or browser-exported HAR files into an OpenAPI 3.0 schema, which gives an agent a concrete starting point instead of a pile of ad hoc request logs. The valuable job here is not “use an API tool.” It is “bootstrap a usable contract from real traffic so later automation has something structured to work from.” Invoke this when a team has a live API, mobile app backend, or internal service that is already being called in the wild, but there is no trustworthy spec to generate a client, create mocks, write contract tests, or diff future changes. An agent can capture representative traffic, run the first pass, review and clean the generated x-path-templates , then rerun the tool to materialize endpoint descriptions and optional examples. That makes it useful before SDK generation, before Schemathesis or Prism-style testing, before documentation backfills, and before integration teams start guessing at request shapes. The scope boundary matters. This is not a generic API platform entry, a documentation portal, or a full lifecycle governance tool. It is specifically for creating a first-pass OpenAPI document from observed traffic. Its output becomes input for other systems, but the skill itself stops at traffic capture, schema generation, and targeted cleanup. Integration points include mitmproxy, browser DevTools HAR export, OpenAPI validators, client generators, mock servers, and CI pipelines that want a contract artifact to version and review.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/bootstrap-openapi-spec-from-captured-api-traffic-before-client-or-test-automation/)
