---
title: Git Secrets Pre-Commit Scanner
description: The Git Secrets Pre-Commit Scanner prevents credential leaks by analyzing
  git diffs before commits are finalized. It combines truffleHog high-entropy string
  detection with configurable regex patterns for API keys, tokens, passwords, and
  private key formats across 40+ service providers including AWS, GCP, Stripe, and
  GitHub. The agent installs as a pre-commit hook using the pre-commit framework,
  scanning staged changes in real-time with sub-second performance. It supports allowlisting
  known safe patterns via .gitallowed files, scanning entire repository history for
  retroactive detection, and generating remediation scripts that rotate compromised
  credentials. Integration with GitHub push protection API enables server-side blocking
  as a secondary defense layer. The scanner handles binary file detection, large file
  skipping, and produces structured JSON output for security dashboard ingestion.
verification: security_reviewed
source: https://agentskillexchange.com/skills/git-secrets-precommit-scanner/
category:
- Security &amp; Verification
framework:
- OpenClaw
---

# Git Secrets Pre-Commit Scanner

The Git Secrets Pre-Commit Scanner prevents credential leaks by analyzing git diffs before commits are finalized. It combines truffleHog high-entropy string detection with configurable regex patterns for API keys, tokens, passwords, and private key formats across 40+ service providers including AWS, GCP, Stripe, and GitHub. The agent installs as a pre-commit hook using the pre-commit framework, scanning staged changes in real-time with sub-second performance. It supports allowlisting known safe patterns via .gitallowed files, scanning entire repository history for retroactive detection, and generating remediation scripts that rotate compromised credentials. Integration with GitHub push protection API enables server-side blocking as a secondary defense layer. The scanner handles binary file detection, large file skipping, and produces structured JSON output for security dashboard ingestion.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/git-secrets-precommit-scanner/)
