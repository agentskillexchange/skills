---
title: "Run contract tests from API descriptions against live endpoints before integrations break with Dredd"
description: "Lets an agent execute OpenAPI or API Blueprint contract checks against a running service so spec drift is caught before release."
verification: listed
source: "https://github.com/apiaryio/dredd"
category:
  - "Library & API Reference"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "apiaryio/dredd"
  github_stars: 4227
  ase_npm_package: "dredd"
  npm_weekly_downloads: 53933
---

# Run contract tests from API descriptions against live endpoints before integrations break with Dredd

Use Dredd when an agent needs to verify that a live HTTP API still behaves like its published description. It fits integration review, release hardening, and contract drift investigations where a spec already exists and must be tested against reality.

Invoke this instead of using the API product normally when the agent must turn an API description into executable contract checks against a running service. This is skill-shaped because the boundary is narrow: spec-driven contract verification of live endpoints. It is not a generic API platform, SDK, or documentation server listing.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/run-contract-tests-from-api-descriptions-against-live-endpoints-before-integrations-break-with-dredd
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/run-contract-tests-from-api-descriptions-against-live-endpoints-before-integrations-break-with-dredd` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-contract-tests-from-api-descriptions-against-live-endpoints-before-integrations-break-with-dredd/)
