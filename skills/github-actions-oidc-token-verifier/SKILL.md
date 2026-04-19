---
title: "GitHub Actions OIDC Token Verifier"
description: "The GitHub Actions OIDC Token Verifier skill provides comprehensive validation of OpenID Connect tokens issued by GitHub Actions workflows. It fetches the JWKS from GitHub&#8217;s OIDC provider (https://token.actions.githubusercontent.com/.well-known/jwks) and performs full JWT verification including signature validation, expiration checks, and claim assertions. The skill validates critical claims including sub (subject) patterns matching repository and environment constraints, aud (audience) restrictions for your cloud provider, and custom claims like job_workflow_ref for reusable workflow verification. It supports configuring claim policies that enforce organizational rules such as requiring specific repository owners, branch protections, or environment approvals. For cloud provider integration, the skill can test token acceptance against AWS STS AssumeRoleWithWebIdentity, GCP Workload Identity Federation, and Azure federated credentials endpoints without performing actual role assumption. It generates trust policy templates for each provider based on your repository structure. Additional features include token lifetime analysis, issuer certificate chain validation, and detection of overly permissive trust policies. Outputs include detailed validation reports, recommended trust policy configurations, and integration test scripts for CI/CD pipelines."
source: "https://docs.github.com/en/actions"
verification: "security_reviewed"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
---

# GitHub Actions OIDC Token Verifier

The GitHub Actions OIDC Token Verifier skill provides comprehensive validation of OpenID Connect tokens issued by GitHub Actions workflows. It fetches the JWKS from GitHub&#8217;s OIDC provider (https://token.actions.githubusercontent.com/.well-known/jwks) and performs full JWT verification including signature validation, expiration checks, and claim assertions. The skill validates critical claims including sub (subject) patterns matching repository and environment constraints, aud (audience) restrictions for your cloud provider, and custom claims like job_workflow_ref for reusable workflow verification. It supports configuring claim policies that enforce organizational rules such as requiring specific repository owners, branch protections, or environment approvals. For cloud provider integration, the skill can test token acceptance against AWS STS AssumeRoleWithWebIdentity, GCP Workload Identity Federation, and Azure federated credentials endpoints without performing actual role assumption. It generates trust policy templates for each provider based on your repository structure. Additional features include token lifetime analysis, issuer certificate chain validation, and detection of overly permissive trust policies. Outputs include detailed validation reports, recommended trust policy configurations, and integration test scripts for CI/CD pipelines.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-oidc-token-verifier/)
