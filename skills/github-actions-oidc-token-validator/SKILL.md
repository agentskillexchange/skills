---
title: "GitHub Actions OIDC Token Validator"
description: "This skill provides a complete pipeline for validating GitHub Actions OIDC tokens to enable secretless deployments to cloud providers. Leveraging the GitHub Actions id-token API and the jose JWT library, it verifies the token&#8217;s audience, issuer, and subject claims against expected values. The skill integrates with AWS STS AssumeRoleWithWebIdentity, GCP Workload Identity Federation, and Azure AD federated identity credentials. It includes helper functions to decode the token payload, verify the signing key from the OIDC discovery endpoint, and return scoped cloud credentials. Error handling covers expired tokens, mismatched subjects, and unreachable discovery endpoints. This approach eliminates long-lived secrets from CI/CD pipelines and follows SLSA supply-chain security recommendations."
source: "https://docs.github.com/en/actions"
verification: "security_reviewed"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
---

# GitHub Actions OIDC Token Validator

This skill provides a complete pipeline for validating GitHub Actions OIDC tokens to enable secretless deployments to cloud providers. Leveraging the GitHub Actions id-token API and the jose JWT library, it verifies the token&#8217;s audience, issuer, and subject claims against expected values. The skill integrates with AWS STS AssumeRoleWithWebIdentity, GCP Workload Identity Federation, and Azure AD federated identity credentials. It includes helper functions to decode the token payload, verify the signing key from the OIDC discovery endpoint, and return scoped cloud credentials. Error handling covers expired tokens, mismatched subjects, and unreachable discovery endpoints. This approach eliminates long-lived secrets from CI/CD pipelines and follows SLSA supply-chain security recommendations.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-oidc-token-validator/)
