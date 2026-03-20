---
name: Secrets Scanner for Git Repositories
description: Wraps Gitleaks and TruffleHog in a unified scan pipeline targeting both commit history and working tree. Deduplicates findings, enriches results with committer identity and timestamps, and suppresses known false positives via allowlist. Outputs SARIF JSON for GitHub Advanced Security.
category: Security &amp; Verification
framework: Any Agent
verification: security_reviewed
rating: 4.4
reviews: 59
source: https://agentskillexchange.com/skill/secrets-scanner-git-repositories-2/
---

# Secrets Scanner for Git Repositories

Wraps Gitleaks and TruffleHog in a unified scan pipeline targeting both commit history and working tree. Deduplicates findings, enriches results with committer identity and timestamps, and suppresses known false positives via allowlist. Outputs SARIF JSON for GitHub Advanced Security.

## Overview

Wraps Gitleaks and TruffleHog in a unified scan pipeline targeting both commit history and working tree. Deduplicates findings, enriches results with committer identity and timestamps, and suppresses known false positives via allowlist. Outputs SARIF JSON for GitHub Advanced Security.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill secrets-scanner-git-repositories-2
```

### OpenClaw

```bash
clawhub install secrets-scanner-git-repositories-2
```

### Claude Code

```bash
claude mcp add secrets-scanner-git-repositories-2
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/secrets-scanner-git-repositories-2/) for detailed installation instructions.

## Verification

- **Status**: security_reviewed
- **Category**: Security &amp; Verification
- **Framework**: Any Agent
- **Rating**: 4.4/5 (59 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/secrets-scanner-git-repositories-2/)
