---
title: "Git Secrets Pre-Commit Scanner"
description: "The Git Secrets Pre-Commit Scanner prevents credential leaks by analyzing git diffs before commits are finalized. It combines truffleHog high-entropy string detection with configurable regex patterns for API keys, tokens, passwords, and private key formats across 40+ service providers including AWS, GCP, Stripe, and GitHub. The agent installs as a pre-commit hook using the pre-commit framework, scanning staged changes in real-time with sub-second performance. It supports allowlisting known safe patterns via .gitallowed files, scanning entire repository history for retroactive detection, and generating remediation scripts that rotate compromised credentials. Integration with GitHub push protection API enables server-side blocking as a secondary defense layer. The scanner handles binary file detection, large file skipping, and produces structured JSON output for security dashboard ingestion."
source: "https://agentskillexchange.com/skills/git-secrets-precommit-scanner/"
verification: "security_reviewed"
category:
  - "Security &amp; Verification"
framework:
  - "OpenClaw"
---

# Git Secrets Pre-Commit Scanner

The Git Secrets Pre-Commit Scanner prevents credential leaks by analyzing git diffs before commits are finalized. It combines truffleHog high-entropy string detection with configurable regex patterns for API keys, tokens, passwords, and private key formats across 40+ service providers including AWS, GCP, Stripe, and GitHub. The agent installs as a pre-commit hook using the pre-commit framework, scanning staged changes in real-time with sub-second performance. It supports allowlisting known safe patterns via .gitallowed files, scanning entire repository history for retroactive detection, and generating remediation scripts that rotate compromised credentials. Integration with GitHub push protection API enables server-side blocking as a secondary defense layer. The scanner handles binary file detection, large file skipping, and produces structured JSON output for security dashboard ingestion.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/git-secrets-precommit-scanner/)
