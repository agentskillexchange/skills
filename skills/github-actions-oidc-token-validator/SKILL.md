---
title: "GitHub Actions OIDC Token Validator"
description: "Validates GitHub Actions OIDC tokens for secure, secretless deployments. Uses the GitHub Actions id-token API and the jose JWT library to verify audience, issuer, and subject claims. Integrates with AWS STS AssumeRoleWithWebIdentity and GCP Workload Identity Federation for cloud access."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/github-actions-oidc-token-validator/"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
---

# GitHub Actions OIDC Token Validator

This skill provides a complete pipeline for validating GitHub Actions OIDC tokens to enable secretless deployments to cloud providers. Leveraging the GitHub Actions id-token API and the jose JWT library, it verifies the token’s audience, issuer, and subject claims against expected values. The skill integrates with AWS STS AssumeRoleWithWebIdentity, GCP Workload Identity Federation, and Azure AD federated identity credentials. It includes helper functions to decode the token payload, verify the signing key from the OIDC discovery endpoint, and return scoped cloud credentials. Error handling covers expired tokens, mismatched subjects, and unreachable discovery endpoints. This approach eliminates long-lived secrets from CI/CD pipelines and follows SLSA supply-chain security recommendations.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-oidc-token-validator/)
