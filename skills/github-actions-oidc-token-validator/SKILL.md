---
title: "GitHub Actions OIDC Token Validator"
description: "Validates GitHub Actions OIDC tokens for secure, secretless deployments. Uses the GitHub Actions id-token API and the jose JWT library to verify audience, issuer, and subject claims. Integrates with AWS STS AssumeRoleWithWebIdentity and GCP Workload Identity Federation for cloud access."
slug: "github-actions-oidc-token-validator"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/github-actions-oidc-token-validator/"
listed: true
---

# GitHub Actions OIDC Token Validator

Validates GitHub Actions OIDC tokens for secure, secretless deployments. Uses the GitHub Actions id-token API and the jose JWT library to verify audience, issuer, and subject claims. Integrates with AWS STS AssumeRoleWithWebIdentity and GCP Workload Identity Federation for cloud access.

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
clawhub install github-actions-oidc-token-validator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill provides a complete pipeline for validating GitHub Actions OIDC tokens to enable secretless deployments to cloud providers. Leveraging the GitHub Actions id-token API and the jose JWT library, it verifies the token’s audience, issuer, and subject claims against expected values. The skill integrates with AWS STS AssumeRoleWithWebIdentity, GCP Workload Identity Federation, and Azure AD federated identity credentials. It includes helper functions to decode the token payload, verify the signing key from the OIDC discovery endpoint, and return scoped cloud credentials. Error handling covers expired tokens, mismatched subjects, and unreachable discovery endpoints. This approach eliminates long-lived secrets from CI/CD pipelines and follows SLSA supply-chain security recommendations.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-oidc-token-validator/)
