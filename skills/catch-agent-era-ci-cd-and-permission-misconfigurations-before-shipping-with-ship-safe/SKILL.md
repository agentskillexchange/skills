---
title: "Catch agent-era CI/CD and permission misconfigurations before shipping with Ship Safe"
description: "Run Ship Safe before a release when an agent needs one pre-ship pass for CI/CD misconfigurations, permission risks, secrets exposure, MCP-related hazards, and dependency issues."
verification: "security_reviewed"
source: "https://github.com/asamassekou10/ship-safe"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "asamassekou10/ship-safe"
  github_stars: 521
  npm_package: "ship-safe"
  npm_weekly_downloads: 2762
---

# Catch agent-era CI/CD and permission misconfigurations before shipping with Ship Safe

Use Ship Safe when the agent needs a pre-ship release gate for repositories and delivery workflows. It scans for CI/CD misconfigurations, over-broad permissions, exposed secrets, risky dependency conditions, and agent-era issues such as unsafe MCP or automation wiring before code is trusted for rollout.

Invoke this instead of using the product normally when the task is release readiness, not general security tooling. The operator workflow is specific: run the scanner against the repo or pipeline configuration before merge or deploy, review the findings, and block or fix risky shipping conditions.

The scope boundary is clear enough to keep this skill-shaped. This is not a generic security platform card or a vague DevOps tool listing. It is the bounded workflow of running a pre-ship misconfiguration and permission audit right before code or automation changes go live.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/catch-agent-era-ci-cd-and-permission-misconfigurations-before-shipping-with-ship-safe/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/catch-agent-era-ci-cd-and-permission-misconfigurations-before-shipping-with-ship-safe
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/catch-agent-era-ci-cd-and-permission-misconfigurations-before-shipping-with-ship-safe`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/catch-agent-era-ci-cd-and-permission-misconfigurations-before-shipping-with-ship-safe/)
