---
title: "Gate pull requests on OpenAPI breaking changes"
description: "This skill uses oasdiff , the open source OpenAPI diff engine, to compare two API specifications and classify the changes that matter for compatibility. An agent invokes it when reviewing a pull request, release branch, or generated spec artifact and needs to answer a focused question: did this change introduce a breaking contract change, and if so, where? The boundary here matters. This is not a generic OpenAPI viewer, SDK generator, or documentation platform entry. The agent is carrying out a specific CI and code review job: collect a baseline spec and a candidate spec, run a diff, interpret the breaking-change rules, and surface only the compatibility-impacting results. If the user simply wants to browse or author an OpenAPI file, that is outside this skill. Use it in release gates, API governance workflows, and repository automation where compatibility promises matter. Integration points include the oasdiff CLI, Go package usage, GitHub pull request checks, and any pipeline that stores a previous spec snapshot. The output is valuable to agents because it is already scoped to reviewable decisions: added or removed operations, parameter changes, response schema drift, enum tightening, security requirement changes, and other contract deltas. An agent can attach the report to a review, fail CI on configured rules, or request a version bump when the API surface changed in a non-backward-compatible way."
source: "https://github.com/oasdiff/oasdiff"
verification: "security_reviewed"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "oasdiff/oasdiff"
  github_stars: 1160
---

# Gate pull requests on OpenAPI breaking changes

This skill uses oasdiff , the open source OpenAPI diff engine, to compare two API specifications and classify the changes that matter for compatibility. An agent invokes it when reviewing a pull request, release branch, or generated spec artifact and needs to answer a focused question: did this change introduce a breaking contract change, and if so, where? The boundary here matters. This is not a generic OpenAPI viewer, SDK generator, or documentation platform entry. The agent is carrying out a specific CI and code review job: collect a baseline spec and a candidate spec, run a diff, interpret the breaking-change rules, and surface only the compatibility-impacting results. If the user simply wants to browse or author an OpenAPI file, that is outside this skill. Use it in release gates, API governance workflows, and repository automation where compatibility promises matter. Integration points include the oasdiff CLI, Go package usage, GitHub pull request checks, and any pipeline that stores a previous spec snapshot. The output is valuable to agents because it is already scoped to reviewable decisions: added or removed operations, parameter changes, response schema drift, enum tightening, security requirement changes, and other contract deltas. An agent can attach the report to a review, fail CI on configured rules, or request a version bump when the API surface changed in a non-backward-compatible way.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gate-pull-requests-on-openapi-breaking-changes/)
