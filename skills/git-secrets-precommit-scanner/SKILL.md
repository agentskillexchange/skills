---
title: "Git Secrets Pre-Commit Scanner"
description: "Scans git diffs for exposed secrets using truffleHog entropy detection and custom regex patterns. Integrates with pre-commit hooks and GitHub push protection API for real-time blocking."
slug: "git-secrets-precommit-scanner"
category:
  - "Security &amp; Verification"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/git-secrets-precommit-scanner/"
listed: true
---

# Git Secrets Pre-Commit Scanner

Scans git diffs for exposed secrets using truffleHog entropy detection and custom regex patterns. Integrates with pre-commit hooks and GitHub push protection API for real-time blocking.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install git-secrets-precommit-scanner
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Git Secrets Pre-Commit Scanner prevents credential leaks by analyzing git diffs before commits are finalized. It combines truffleHog high-entropy string detection with configurable regex patterns for API keys, tokens, passwords, and private key formats across 40+ service providers including AWS, GCP, Stripe, and GitHub. The agent installs as a pre-commit hook using the pre-commit framework, scanning staged changes in real-time with sub-second performance. It supports allowlisting known safe patterns via .gitallowed files, scanning entire repository history for retroactive detection, and generating remediation scripts that rotate compromised credentials. Integration with GitHub push protection API enables server-side blocking as a secondary defense layer. The scanner handles binary file detection, large file skipping, and produces structured JSON output for security dashboard ingestion.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/git-secrets-precommit-scanner/)
