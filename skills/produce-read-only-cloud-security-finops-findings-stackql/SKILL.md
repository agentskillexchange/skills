---
name: "Produce read-only cloud security and FinOps findings with StackQL"
slug: "produce-read-only-cloud-security-finops-findings-stackql"
description: "Run StackQL’s pinned Docker audit against approved cloud scopes and return security findings, waste estimates and coverage gaps from its JSON artifact."
github_stars: 1080
verification: "security_reviewed"
source: "https://github.com/stackql/stackql"
author: "StackQL"
publisher_type: "open_source"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "stackql/stackql"
  github_stars: 1080
---

# Produce read-only cloud security and FinOps findings with StackQL

Run StackQL’s pinned Docker audit against approved cloud scopes and return security findings, waste estimates and coverage gaps from its JSON artifact.

## Prerequisites

Docker; Docker Compose; StackQL repository checkout; read-only cloud credentials; network access for images, providers and the pinned audit engine

## Installation

Install or set up from the source-backed instructions:

Obtain the StackQL repository at inspected commit da44f4d5d341f6ed8e8a5293377cd6df8eaa721c and install Docker with Compose. Follow docs/audit.md: copy cicd/audit/.env.audit.example to cicd/audit/.env.audit and configure read-only credentials only for the approved cloud scope. Preserve AUDIT_ENGINE_REF=4d02dccad5d9b9a79d04c4c48af88e1fb4149aff and provider version pins. Select a compatible verified STACKQL_IMAGE tag or digest rather than assuming latest is reproducible. Run docker compose -f docker-compose.audit.yaml pull, then docker compose -f docker-compose.audit.yaml run --rm audit. Inspect cicd/audit/output/findings.json. Commands are documented, not installation-tested in this review.

- Source: https://github.com/stackql/stackql

## Documentation

- https://github.com/stackql/stackql/blob/da44f4d5d341f6ed8e8a5293377cd6df8eaa721c/docs/audit.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/produce-read-only-cloud-security-finops-findings-stackql/)
