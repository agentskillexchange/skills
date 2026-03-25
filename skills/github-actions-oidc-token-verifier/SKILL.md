---
name: "GitHub Actions OIDC Token Verifier"
description: "Verifies GitHub Actions OIDC tokens against the GitHub OIDC provider JWKS endpoint. Validates subject claims, audience restrictions, and repository ownership for secure cloud deployments."
category: "CI/CD Integrations"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/github-actions-oidc-token-verifier/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "aws"  # from ase_tool_match
  github_stars: 3594  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 9204385  # from ase_npm_downloads
  github_repo: "aws/aws-sdk-js-v3"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# GitHub Actions OIDC Token Verifier

Verifies GitHub Actions OIDC tokens against the GitHub OIDC provider JWKS endpoint. Validates subject claims, audience restrictions, and repository ownership for secure cloud deployments.

## Overview

The GitHub Actions OIDC Token Verifier skill provides comprehensive validation of OpenID Connect tokens issued by GitHub Actions workflows. It fetches the JWKS from GitHub’s OIDC provider (https://token.actions.githubusercontent.com/.well-known/jwks) and performs full JWT verification including signature validation, expiration checks, and claim assertions.

The skill validates critical claims including sub (subject) patterns matching repository and environment constraints, aud (audience) restrictions for your cloud provider, and custom claims like job_workflow_ref for reusable workflow verification. It supports configuring claim policies that enforce organizational rules such as requiring specific repository owners, branch protections, or environment approvals.

For cloud provider integration, the skill can test token acceptance against AWS STS AssumeRoleWithWebIdentity, GCP Workload Identity Federation, and Azure federated credentials endpoints without performing actual role assumption. It generates trust policy templates for each provider based on your repository structure.

Additional features include token lifetime analysis, issuer certificate chain validation, and detection of overly permissive trust policies. Outputs include detailed validation reports, recommended trust policy configurations, and integration test scripts for CI/CD pipelines.

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

## Source

- Marketplace: https://agentskillexchange.com/skills/github-actions-oidc-token-verifier/
