---
name: "GitHub Actions OIDC Token Validator"
description: "Validates GitHub Actions OIDC tokens for secure, secretless deployments. Uses the GitHub Actions id-token API and the jose JWT library to verify audience, issuer, and subject claims. Integrates with AWS STS AssumeRoleWithWebIdentity and GCP Workload Identity Federation for cloud access."
category: "CI/CD Integrations"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/github-actions-oidc-token-validator/"
tool_ecosystem:
  tool: "aws"
  github_stars: 3594
  npm_weekly_downloads: 9204385
  github_repo: "aws/aws-sdk-js-v3"
  license: "Apache-2.0"
  maintained: true
---

# GitHub Actions OIDC Token Validator

Validates GitHub Actions OIDC tokens for secure, secretless deployments. Uses the GitHub Actions id-token API and the jose JWT library to verify audience, issuer, and subject claims. Integrates with AWS STS AssumeRoleWithWebIdentity and GCP Workload Identity Federation for cloud access.

## Overview

This skill provides a complete pipeline for validating GitHub Actions OIDC tokens to enable secretless deployments to cloud providers. Leveraging the GitHub Actions id-token API and the jose JWT library, it verifies the token’s audience, issuer, and subject claims against expected values. The skill integrates with AWS STS AssumeRoleWithWebIdentity, GCP Workload Identity Federation, and Azure AD federated identity credentials. It includes helper functions to decode the token payload, verify the signing key from the OIDC discovery endpoint, and return scoped cloud credentials. Error handling covers expired tokens, mismatched subjects, and unreachable discovery endpoints. This approach eliminates long-lived secrets from CI/CD pipelines and follows SLSA supply-chain security recommendations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill github-actions-oidc-token-validator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill github-actions-oidc-token-validator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill github-actions-oidc-token-validator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill github-actions-oidc-token-validator -a codex
```

### OpenClaw

```bash
clawhub install github-actions-oidc-token-validator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/github-actions-oidc-token-validator/
