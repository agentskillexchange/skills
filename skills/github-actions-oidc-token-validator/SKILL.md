---
title: "GitHub Actions OIDC Token Validator"
description: "Validates GitHub Actions OIDC tokens for secure, secretless deployments. Uses the GitHub Actions id-token API and the jose JWT library to verify audience, issuer, and subject claims. Integrates with AWS STS AssumeRoleWithWebIdentity and GCP Workload Identity Federation for cloud access."
verification: "security_reviewed"
source: "https://docs.github.com/en/actions"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
---

# GitHub Actions OIDC Token Validator

This skill provides a complete pipeline for validating GitHub Actions OIDC tokens to enable secretless deployments to cloud providers. Leveraging the GitHub Actions id-token API and the jose JWT library, it verifies the token’s audience, issuer, and subject claims against expected values. The skill integrates with AWS STS AssumeRoleWithWebIdentity, GCP Workload Identity Federation, and Azure AD federated identity credentials. It includes helper functions to decode the token payload, verify the signing key from the OIDC discovery endpoint, and return scoped cloud credentials. Error handling covers expired tokens, mismatched subjects, and unreachable discovery endpoints. This approach eliminates long-lived secrets from CI/CD pipelines and follows SLSA supply-chain security recommendations.

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
