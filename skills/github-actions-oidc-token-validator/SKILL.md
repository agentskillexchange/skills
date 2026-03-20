---
name: GitHub Actions OIDC Token Validator
description: Validates GitHub Actions OIDC tokens for secure, secretless deployments. Uses the GitHub Actions id-token API and the jose JWT library to verify audience, issuer, and subject claims. Integrates with A
category: CI/CD Integrations
framework: Claude Code
verification: security_reviewed
rating: 4.9
reviews: 77
source: https://agentskillexchange.com/skill/github-actions-oidc-token-validator/
---

# GitHub Actions OIDC Token Validator

Validates GitHub Actions OIDC tokens for secure, secretless deployments. Uses the GitHub Actions id-token API and the jose JWT library to verify audience, issuer, and subject claims. Integrates with AWS STS AssumeRoleWithWebIdentity and GCP Workload Identity Federation for cloud access.

## Overview

This skill provides a complete pipeline for validating GitHub Actions OIDC tokens to enable secretless deployments to cloud providers. Leveraging the GitHub Actions id-token API and the jose JWT library, it verifies the token’s audience, issuer, and subject claims against expected values. The skill integrates with AWS STS AssumeRoleWithWebIdentity, GCP Workload Identity Federation, and Azure AD federated identity credentials. It includes helper functions to decode the token payload, verify the signing key from the OIDC discovery endpoint, and return scoped cloud credentials. Error handling covers expired tokens, mismatched subjects, and unreachable discovery endpoints. This approach eliminates long-lived secrets from CI/CD pipelines and follows SLSA supply-chain security recommendations.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill github-actions-oidc-token-validator
```

### OpenClaw

```bash
openclaw install github-actions-oidc-token-validator
```

### Manual

Download this `SKILL.md` file and place it in your agent's skills directory.

## Metadata

| Field | Value |
|-------|-------|
| Category | CI/CD Integrations |
| Framework | Claude Code |
| Verification | Security Reviewed |
| Rating | ⭐⭐⭐⭐ 4.9/5.0 (77 reviews) |

---

*Published on [Agent Skill Exchange](https://agentskillexchange.com/skill/github-actions-oidc-token-validator/)*
