---
title: "Lint Rego Policies Before Promotion with Regal"
description: "Analyze Rego policy files for style, correctness, and maintainability issues before policy bundles are promoted."
verification: "listed"
source: "https://github.com/StyraInc/regal"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "StyraInc/regal"
  github_stars: 373
---

# Lint Rego Policies Before Promotion with Regal

This skill wraps Regal as a policy-authoring quality gate for Rego. The agent lints policy files, highlights correctness and maintainability issues, and gives teams a repeatable pre-promotion check before bundles move into enforcement environments.

Invoke it when a repository contains Rego policies that need review before merge or bundle promotion. Use OPA itself normally for policy evaluation and runtime decisions. Use this skill when the job is specifically authoring-time linting and policy hygiene.

The scope boundary is Rego linting and authoring feedback. It is not an OPA platform listing, policy engine card, or general compliance product entry.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/lint-rego-policies-before-promotion-with-regal/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/lint-rego-policies-before-promotion-with-regal
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/lint-rego-policies-before-promotion-with-regal`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-rego-policies-before-promotion-with-regal/)
