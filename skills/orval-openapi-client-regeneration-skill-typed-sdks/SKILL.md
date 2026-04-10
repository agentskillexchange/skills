---
title: "Orval OpenAPI Client Regeneration Skill for Typed SDKs"
description: "Use this skill when an agent needs to regenerate a typed API client from an OpenAPI spec, keep fetch clients aligned with backend schema changes, and update generated hooks without hand-editing the output. It is a narrowly scoped Orval workflow skill, not a generic listing for the Orval project."
slug: "orval-openapi-client-regeneration-skill-typed-sdks"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/orval-labs/orval"
tool_ecosystem:
  github_repo: "orval-labs/orval"
  github_stars: 5657
  npm_package: "orval"
  npm_weekly_downloads: 1025981
---

# Orval OpenAPI Client Regeneration Skill for Typed SDKs

Use this skill when an agent needs to regenerate a typed API client from an OpenAPI spec, keep fetch clients aligned with backend schema changes, and update generated hooks without hand-editing the output. It is a narrowly scoped Orval workflow skill, not a generic listing for the Orval project.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install orval-openapi-client-regeneration-skill-typed-sdks
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill teaches an agent how to use Orval to regenerate typed API clients from an OpenAPI document, review the generated surface area, and keep downstream application code aligned after schema changes. The agent’s job is concrete: find the spec source, inspect the current Orval configuration, run regeneration, compare the generated client with the previous version, and point out breaking request or response changes that will affect callers. When the repository uses React Query, SWR, Axios, or fetch output modes, the agent can also update the matching generated hooks and note where custom overrides belong.
Invoke this skill when a user says things like “update the API client after backend changes,” “regenerate our SDK,” or “wire a new endpoint into the generated client.” In those cases the user does not want a general OpenAPI lecture, and they do not want the agent inventing manual client code that will drift later. They want a repeatable generation workflow around the real Orval toolchain.
The scope boundary matters. This is not a directory entry for Orval as a product, and it is not a broad OpenAPI design skill. It is specifically for operating Orval as a generation step: configuring inputs and outputs, running the generator, reviewing generated artifacts, and identifying safe places for handwritten code around generated files. Typical integration points include npm scripts, CI checks, monorepos that publish internal SDKs, and frontend apps that depend on consistent typed clients.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/orval-openapi-client-regeneration-skill-typed-sdks/)
