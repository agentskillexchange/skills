---
title: "Orval OpenAPI Client Regeneration Skill for Typed SDKs"
description: "This skill teaches an agent how to use Orval to regenerate typed API clients from an OpenAPI document, review the generated surface area, and keep downstream application code aligned after schema changes. The agent’s job is concrete: find the spec source, inspect the current Orval configuration, run regeneration, compare the generated client with the previous version, and point out breaking request or response changes that will affect callers. When the repository uses React Query, SWR, Axios, or fetch output modes, the agent can also update the matching generated hooks and note where custom overrides belong. Invoke this skill when a user says things like “update the API client after backend changes,” “regenerate our SDK,” or “wire a new endpoint into the generated client.” In those cases the user does not want a general OpenAPI lecture, and they do not want the agent inventing manual client code that will drift later. They want a repeatable generation workflow around the real Orval toolchain. The scope boundary matters. This is not a directory entry for Orval as a product, and it is not a broad OpenAPI design skill. It is specifically for operating Orval as a generation step: configuring inputs and outputs, running the generator, reviewing generated artifacts, and identifying safe places for handwritten code around generated files. Typical integration points include npm scripts, CI checks, monorepos that publish internal SDKs, and frontend apps that depend on consistent typed clients."
source: "https://github.com/orval-labs/orval"
verification: "security_reviewed"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "orval-labs/orval"
  github_stars: 5675
  npm_package: "orval"
  npm_weekly_downloads: 1102606
---

# Orval OpenAPI Client Regeneration Skill for Typed SDKs

This skill teaches an agent how to use Orval to regenerate typed API clients from an OpenAPI document, review the generated surface area, and keep downstream application code aligned after schema changes. The agent’s job is concrete: find the spec source, inspect the current Orval configuration, run regeneration, compare the generated client with the previous version, and point out breaking request or response changes that will affect callers. When the repository uses React Query, SWR, Axios, or fetch output modes, the agent can also update the matching generated hooks and note where custom overrides belong. Invoke this skill when a user says things like “update the API client after backend changes,” “regenerate our SDK,” or “wire a new endpoint into the generated client.” In those cases the user does not want a general OpenAPI lecture, and they do not want the agent inventing manual client code that will drift later. They want a repeatable generation workflow around the real Orval toolchain. The scope boundary matters. This is not a directory entry for Orval as a product, and it is not a broad OpenAPI design skill. It is specifically for operating Orval as a generation step: configuring inputs and outputs, running the generator, reviewing generated artifacts, and identifying safe places for handwritten code around generated files. Typical integration points include npm scripts, CI checks, monorepos that publish internal SDKs, and frontend apps that depend on consistent typed clients.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/orval-openapi-client-regeneration-skill-typed-sdks/)
