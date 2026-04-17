---
title: "GitHub Actions OIDC Token Verifier"
description: "The GitHub Actions OIDC Token Verifier skill provides comprehensive validation of OpenID Connect tokens issued by GitHub Actions workflows. It fetches the JWKS from GitHub’s OIDC provider (https://token.actions.githubusercontent.com/.well-known/jwks) and performs full JWT verification including signature validation, expiration checks, and claim assertions.\nThe skill validates critical claims including sub (subject) patterns matching repository and environment constraints, aud (audience) restrictions for your cloud provider, and custom claims like job_workflow_ref for reusable workflow verification. It supports configuring claim policies that enforce organizational rules such as requiring specific repository owners, branch protections, or environment approvals.\nFor cloud provider integration, the skill can test token acceptance against AWS STS AssumeRoleWithWebIdentity, GCP Workload Identity Federation, and Azure federated credentials endpoints without performing actual role assumption. It generates trust policy templates for each provider based on your repository structure.\nAdditional features include token lifetime analysis, issuer certificate chain validation, and detection of overly permissive trust policies. Outputs include detailed validation reports, recommended trust policy configurations, and integration test scripts for CI/CD pipelines."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/github-actions-oidc-token-verifier/"
framework:
  - "Claude Code"
---

# GitHub Actions OIDC Token Verifier

The GitHub Actions OIDC Token Verifier skill provides comprehensive validation of OpenID Connect tokens issued by GitHub Actions workflows. It fetches the JWKS from GitHub’s OIDC provider (https://token.actions.githubusercontent.com/.well-known/jwks) and performs full JWT verification including signature validation, expiration checks, and claim assertions.
The skill validates critical claims including sub (subject) patterns matching repository and environment constraints, aud (audience) restrictions for your cloud provider, and custom claims like job_workflow_ref for reusable workflow verification. It supports configuring claim policies that enforce organizational rules such as requiring specific repository owners, branch protections, or environment approvals.
For cloud provider integration, the skill can test token acceptance against AWS STS AssumeRoleWithWebIdentity, GCP Workload Identity Federation, and Azure federated credentials endpoints without performing actual role assumption. It generates trust policy templates for each provider based on your repository structure.
Additional features include token lifetime analysis, issuer certificate chain validation, and detection of overly permissive trust policies. Outputs include detailed validation reports, recommended trust policy configurations, and integration test scripts for CI/CD pipelines.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/github-actions-oidc-token-verifier
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/github-actions-oidc-token-verifier` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-oidc-token-verifier/)
