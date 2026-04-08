---
title: GitHub Actions OIDC Token Validator
description: This skill provides a complete pipeline for validating GitHub Actions
  OIDC tokens to enable secretless deployments to cloud providers. Leveraging the
  GitHub Actions id-token API and the jose JWT library, it verifies the token’s audience,
  issuer, and subject claims against expected values. The skill integrates with AWS
  STS AssumeRoleWithWebIdentity, GCP Workload Identity Federation, and Azure AD federated
  identity credentials. It includes helper functions to decode the token payload,
  verify the signing key from the OIDC discovery endpoint, and return scoped cloud
  credentials. Error handling covers expired tokens, mismatched subjects, and unreachable
  discovery endpoints. This approach eliminates long-lived secrets from CI/CD pipelines
  and follows SLSA supply-chain security recommendations.
verification: security_reviewed
source: https://agentskillexchange.com/skills/github-actions-oidc-token-validator/
category:
- CI/CD Integrations
framework:
- Claude Code
---

# GitHub Actions OIDC Token Validator

This skill provides a complete pipeline for validating GitHub Actions OIDC tokens to enable secretless deployments to cloud providers. Leveraging the GitHub Actions id-token API and the jose JWT library, it verifies the token’s audience, issuer, and subject claims against expected values. The skill integrates with AWS STS AssumeRoleWithWebIdentity, GCP Workload Identity Federation, and Azure AD federated identity credentials. It includes helper functions to decode the token payload, verify the signing key from the OIDC discovery endpoint, and return scoped cloud credentials. Error handling covers expired tokens, mismatched subjects, and unreachable discovery endpoints. This approach eliminates long-lived secrets from CI/CD pipelines and follows SLSA supply-chain security recommendations.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-oidc-token-validator/)
