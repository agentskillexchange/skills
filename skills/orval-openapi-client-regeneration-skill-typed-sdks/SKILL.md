---
title: "Orval OpenAPI Client Regeneration Skill for Typed SDKs"
description: "Use this skill when an agent needs to regenerate a typed API client from an OpenAPI spec, keep fetch clients aligned with backend schema changes, and update generated hooks without hand-editing the output. It is a narrowly scoped Orval workflow skill, not a generic listing for the Orval project."
verification: security_reviewed
source: "https://github.com/orval-labs/orval"
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

This skill teaches an agent how to use Orval to regenerate typed API clients from an OpenAPI document, review the generated surface area, and keep downstream application code aligned after schema changes. The agent’s job is concrete: find the spec source, inspect the current Orval configuration, run regeneration, compare the generated client with the previous version, and point out breaking request or response changes that will affect callers. When the repository uses React Query, SWR, Axios, or fetch output modes, the agent can also update the matching generated hooks and note where custom overrides belong.

Invoke this skill when a user says things like “update the API client after backend changes,” “regenerate our SDK,” or “wire a new endpoint into the generated client.” In those cases the user does not want a general OpenAPI lecture, and they do not want the agent inventing manual client code that will drift later. They want a repeatable generation workflow around the real Orval toolchain.

The scope boundary matters. This is not a directory entry for Orval as a product, and it is not a broad OpenAPI design skill. It is specifically for operating Orval as a generation step: configuring inputs and outputs, running the generator, reviewing generated artifacts, and identifying safe places for handwritten code around generated files. Typical integration points include npm scripts, CI checks, monorepos that publish internal SDKs, and frontend apps that depend on consistent typed clients.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/orval-openapi-client-regeneration-skill-typed-sdks/)
