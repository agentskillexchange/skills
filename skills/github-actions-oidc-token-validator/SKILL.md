---
title: GitHub Actions OIDC Token Validator
description: Validates GitHub Actions OIDC tokens for secure, secretless deployments.
  Uses the GitHub Actions id-token API and the jose JWT library to verify audience,
  issuer, and subject claims. Integrates with AWS STS AssumeRoleWithWebIdentity and
  GCP Workload Identity Federation for cloud access.
verification: security_reviewed
source: https://docs.github.com/en/actions
category:
- CI/CD Integrations
framework:
- Claude Code
---

# GitHub Actions OIDC Token Validator

Validates GitHub Actions OIDC tokens for secure, secretless deployments. Uses the GitHub Actions id-token API and the jose JWT library to verify audience, issuer, and subject claims. Integrates with AWS STS AssumeRoleWithWebIdentity and GCP Workload Identity Federation for cloud access.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/github-actions-oidc-token-validator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/github-actions-oidc-token-validator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/github-actions-oidc-token-validator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-oidc-token-validator/)
