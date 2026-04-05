---
name: "GitHub Actions OIDC Token Verifier"
description: "Verifies GitHub Actions OIDC tokens against the GitHub OIDC provider JWKS endpoint. Validates subject claims, audience restrictions, and repository ownership for secure cloud deployments."
category: "CI/CD Integrations"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/github-actions-oidc-token-verifier/"
---
# GitHub Actions OIDC Token Verifier

Verifies GitHub Actions OIDC tokens against the GitHub OIDC provider JWKS endpoint. Validates subject claims, audience restrictions, and repository ownership for secure cloud deployments.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill github-actions-oidc-token-verifier
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill github-actions-oidc-token-verifier -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill github-actions-oidc-token-verifier -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill github-actions-oidc-token-verifier -a codex
```

### OpenClaw

```bash
clawhub install github-actions-oidc-token-verifier
```

## Details

The GitHub Actions OIDC Token Verifier skill provides comprehensive validation of OpenID Connect tokens issued by GitHub Actions workflows. It fetches the JWKS from GitHub’s OIDC provider (https://token.actions.githubusercontent.com/.well-known/jwks) and performs full JWT verification including signature validation, expiration checks, and claim assertions.

The skill validates critical claims including sub (subject) patterns matching repository and environment constraints, aud (audience) restrictions for your cloud provider, and custom claims like job_workflow_ref for reusable workflow verification. It supports configuring claim policies that enforce organizational rules such as requiring specific repository owners, branch protections, or environment approvals.

For cloud provider integration, the skill can test token acceptance against AWS STS AssumeRoleWithWebIdentity, GCP Workload Identity Federation, and Azure federated credentials endpoints without performing actual role assumption. It generates trust policy templates for each provider based on your repository structure.

Additional features include token lifetime analysis, issuer certificate chain validation, and detection of overly permissive trust policies. Outputs include detailed validation reports, recommended trust policy configurations, and integration test scripts for CI/CD pipelines.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-oidc-token-verifier/)
