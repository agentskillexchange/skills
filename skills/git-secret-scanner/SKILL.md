---
title: Git Secret Scanner
description: The Git Secret Scanner skill identifies leaked credentials, API keys,
  tokens, and other secrets across Git repository history using multi-layered detection
  approaches. It combines pattern-based scanning inspired by Gitleaks rule definitions
  with entropy analysis to catch both known secret formats and high-entropy strings
  that may represent credentials. The skill scans the complete Git history using git
  log –all -p –diff-filter=A to examine every added line across all branches and historical
  commits, including deleted branches accessible via reflog. It matches content against
  a comprehensive rule set covering AWS access keys (AKIA pattern), GitHub personal
  access tokens (ghp_/gho_/ghs_ prefixes), Slack webhooks, Stripe API keys, Google
  Cloud service account JSON, JWT tokens, and database connection strings. Capabilities
  include integration with the GitHub Secret Scanning API via /repos/{owner}/{repo}/secret-scanning/alerts
  for repositories with GitHub Advanced Security, pre-commit hook generation using
  the pre-commit framework to prevent future secret commits, .gitignore and .gitleaks.toml
  allowlist configuration for false positive management, and git filter-branch command
  generation for history rewriting to remove exposed secrets. The skill generates
  severity-ranked reports with credential rotation checklists, links to provider-specific
  key rotation documentation, and estimated blast radius analysis based on the secret
  type and exposure duration.
verification: security_reviewed
source: https://agentskillexchange.com/skills/git-secret-scanner/
category:
- Security &amp; Verification
framework:
- Claude Agents
---

# Git Secret Scanner

The Git Secret Scanner skill identifies leaked credentials, API keys, tokens, and other secrets across Git repository history using multi-layered detection approaches. It combines pattern-based scanning inspired by Gitleaks rule definitions with entropy analysis to catch both known secret formats and high-entropy strings that may represent credentials. The skill scans the complete Git history using git log –all -p –diff-filter=A to examine every added line across all branches and historical commits, including deleted branches accessible via reflog. It matches content against a comprehensive rule set covering AWS access keys (AKIA pattern), GitHub personal access tokens (ghp_/gho_/ghs_ prefixes), Slack webhooks, Stripe API keys, Google Cloud service account JSON, JWT tokens, and database connection strings. Capabilities include integration with the GitHub Secret Scanning API via /repos/{owner}/{repo}/secret-scanning/alerts for repositories with GitHub Advanced Security, pre-commit hook generation using the pre-commit framework to prevent future secret commits, .gitignore and .gitleaks.toml allowlist configuration for false positive management, and git filter-branch command generation for history rewriting to remove exposed secrets. The skill generates severity-ranked reports with credential rotation checklists, links to provider-specific key rotation documentation, and estimated blast radius analysis based on the secret type and exposure duration.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/git-secret-scanner/)
