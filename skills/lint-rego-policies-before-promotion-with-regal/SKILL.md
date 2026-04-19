---
title: "Lint Rego Policies Before Promotion with Regal"
description: "This skill wraps Regal as a policy-authoring quality gate for Rego. The agent lints policy files, highlights correctness and maintainability issues, and gives teams a repeatable pre-promotion check before bundles move into enforcement environments. Invoke it when a repository contains Rego policies that need review before merge or bundle promotion. Use OPA itself normally for policy evaluation and runtime decisions. Use this skill when the job is specifically authoring-time linting and policy hygiene. The scope boundary is Rego linting and authoring feedback. It is not an OPA platform listing, policy engine card, or general compliance product entry."
source: "https://github.com/StyraInc/regal"
verification: "listed"
category:
  - "Security &amp; Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "StyraInc/regal"
  github_stars: 373
---

# Lint Rego Policies Before Promotion with Regal

This skill wraps Regal as a policy-authoring quality gate for Rego. The agent lints policy files, highlights correctness and maintainability issues, and gives teams a repeatable pre-promotion check before bundles move into enforcement environments. Invoke it when a repository contains Rego policies that need review before merge or bundle promotion. Use OPA itself normally for policy evaluation and runtime decisions. Use this skill when the job is specifically authoring-time linting and policy hygiene. The scope boundary is Rego linting and authoring feedback. It is not an OPA platform listing, policy engine card, or general compliance product entry.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-rego-policies-before-promotion-with-regal/)
