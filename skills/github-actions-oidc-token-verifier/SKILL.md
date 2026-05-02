---
title: "GitHub Actions OIDC Token Verifier"
description: "Verifies GitHub Actions OIDC tokens against the GitHub OIDC provider JWKS endpoint. Validates subject claims, audience restrictions, and repository ownership for secure cloud deployments."
verification: "security_reviewed"
source: "https://docs.github.com/en/actions"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
---

# GitHub Actions OIDC Token Verifier

The GitHub Actions OIDC Token Verifier skill provides comprehensive validation of OpenID Connect tokens issued by GitHub Actions workflows. It fetches the JWKS from GitHub’s OIDC provider (https://token.actions.githubusercontent.com/.well-known/jwks) and performs full JWT verification including signature validation, expiration checks, and claim assertions.

The skill validates critical claims including sub (subject) patterns matching repository and environment constraints, aud (audience) restrictions for your cloud provider, and custom claims like job_workflow_ref for reusable workflow verification. It supports configuring claim policies that enforce organizational rules such as requiring specific repository owners, branch protections, or environment approvals.

For cloud provider integration, the skill can test token acceptance against AWS STS AssumeRoleWithWebIdentity, GCP Workload Identity Federation, and Azure federated credentials endpoints without performing actual role assumption. It generates trust policy templates for each provider based on your repository structure.

Additional features include token lifetime analysis, issuer certificate chain validation, and detection of overly permissive trust policies. Outputs include detailed validation reports, recommended trust policy configurations, and integration test scripts for CI/CD pipelines.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/github-actions-oidc-token-verifier/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/github-actions-oidc-token-verifier
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/github-actions-oidc-token-verifier`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-oidc-token-verifier/)
