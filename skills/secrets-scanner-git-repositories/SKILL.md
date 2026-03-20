---
name: Secrets Scanner for Git Repositories
description: Wraps Gitleaks and TruffleHog in a unified scan pipeline targeting both commit history and working tree. Deduplicates findings across tools, enriches each result with committer identity and timestamp, and suppresses known false positives via allowlist. Outputs SARIF-compatible JSON for GitHub Advanced Security.
category: Security &amp; Verification
framework: Any Agent
verification: listed
rating: 4.5
reviews: 44
source: https://agentskillexchange.com/skill/secrets-scanner-git-repositories/
---

# Secrets Scanner for Git Repositories

Wraps Gitleaks and TruffleHog in a unified scan pipeline targeting both commit history and working tree. Deduplicates findings across tools, enriches each result with committer identity and timestamp, and suppresses known false positives via allowlist. Outputs SARIF-compatible JSON for GitHub Advanced Security.

## Overview

Wraps Gitleaks and TruffleHog in a unified scan pipeline targeting both commit history and working tree. Deduplicates findings across tools, enriches each result with committer identity and timestamp, and suppresses known false positives via allowlist. Outputs SARIF-compatible JSON for GitHub Advanced Security.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill secrets-scanner-git-repositories
```

### OpenClaw

```bash
clawhub install secrets-scanner-git-repositories
```

### Claude Code

```bash
claude mcp add secrets-scanner-git-repositories
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/secrets-scanner-git-repositories/) for detailed installation instructions.

## Verification

- **Status**: listed
- **Category**: Security &amp; Verification
- **Framework**: Any Agent
- **Rating**: 4.5/5 (44 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/secrets-scanner-git-repositories/)
