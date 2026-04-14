---
title: "Bootstrap an OpenAPI spec from captured API traffic before client or test automation starts"
description: "Uses mitmproxy2swagger to turn captured mitmproxy flows or HAR exports into a first-pass OpenAPI document that an agent can refine, validate, and hand off to downstream tooling. Invoke it when the API already exists but the contract does not, and you need a concrete spec before generating clients, mocks, tests, or reviewable docs."
verification: security_reviewed
source: "https://github.com/alufers/mitmproxy2swagger"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Multi-Framework"
---

# Bootstrap an OpenAPI spec from captured API traffic before client or test automation starts

This skill uses mitmproxy2swagger as a bounded reverse-engineering workflow for undocumented HTTP APIs. The tool converts captured mitmproxy flow files or browser-exported HAR files into an OpenAPI 3.0 schema, which gives an agent a concrete starting point instead of a pile of ad hoc request logs. The valuable job here is not “use an API tool.” It is “bootstrap a usable contract from real traffic so later automation has something structured to work from.”

Invoke this when a team has a live API, mobile app backend, or internal service that is already being called in the wild, but there is no trustworthy spec to generate a client, create mocks, write contract tests, or diff future changes. An agent can capture representative traffic, run the first pass, review and clean the generated x-path-templates, then rerun the tool to materialize endpoint descriptions and optional examples. That makes it useful before SDK generation, before Schemathesis or Prism-style testing, before documentation backfills, and before integration teams start guessing at request shapes.

The scope boundary matters. This is not a generic API platform entry, a documentation portal, or a full lifecycle governance tool. It is specifically for creating a first-pass OpenAPI document from observed traffic. Its output becomes input for other systems, but the skill itself stops at traffic capture, schema generation, and targeted cleanup. Integration points include mitmproxy, browser DevTools HAR export, OpenAPI validators, client generators, mock servers, and CI pipelines that want a contract artifact to version and review.

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
