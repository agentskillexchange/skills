---
name: "Validate a managed JSON Goal deliverable in MateClaw"
slug: "validate-a-managed-json-goal-deliverable-in-mateclaw"
description: "Publish a scoped JSON report to a user-selected Goal slot, bind required-field checks to its exact version, and reconcile conflicts before completion."
github_stars: 1209
verification: "security_reviewed"
source: "https://github.com/mateaix/mateclaw"
author: "mateaix"
publisher_type: "organization"
category: "Templates & Workflows"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "mateaix/mateclaw"
  github_stars: 1209
---

# Validate a managed JSON Goal deliverable in MateClaw

Publish a scoped JSON report to a user-selected Goal slot, bind required-field checks to its exact version, and reconcile conflicts before completion.

## Prerequisites

Existing configured MateClaw native-runtime employee and Goal; authenticated Goal owner; getManagedGoalJsonSlots, publishManagedGoalJson, checkManagedGoalJson; Goal status/completion tools

## Installation

Install or set up from the source-backed instructions:

Use an existing MateClaw deployment with managed JSON Goal acceptance. For initial setup follow the pinned official README: clone mateaix/mateclaw, configure the documented JWT/database secrets in .env from .env.example, and use docker compose up -d, or use the documented Java 21/Maven source setup. Complete account and model configuration before this workflow. In the intended conversation select the native runtime and have the authenticated owner enable managed JSON acceptance with named slots and required fields. Confirm the three managed JSON tools are exposed; stop if unavailable. No installation or authentication was performed during intake.

- Source: https://github.com/mateaix/mateclaw

## Documentation

- https://github.com/mateaix/mateclaw/blob/f457f6659f776fa0b74ea9cab5f0158ae9000517/mateclaw-server/src/main/resources/docs/en/goals.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/validate-a-managed-json-goal-deliverable-in-mateclaw/)
