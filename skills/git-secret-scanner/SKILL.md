---
title: "Git Secret Scanner"
description: "The Git Secret Scanner skill identifies leaked credentials, API keys, tokens, and other secrets across Git repository history using multi-layered detection approaches. It combines pattern-based scanning inspired by Gitleaks rule definitions with entropy analysis to catch both known secret formats and high-entropy strings that may represent credentials.\nThe skill scans the complete Git history using git log –all -p –diff-filter=A to examine every added line across all branches and historical commits, including deleted branches accessible via reflog. It matches content against a comprehensive rule set covering AWS access keys (AKIA pattern), GitHub personal access tokens (ghp_/gho_/ghs_ prefixes), Slack webhooks, Stripe API keys, Google Cloud service account JSON, JWT tokens, and database connection strings.\nCapabilities include integration with the GitHub Secret Scanning API via /repos/{owner}/{repo}/secret-scanning/alerts for repositories with GitHub Advanced Security, pre-commit hook generation using the pre-commit framework to prevent future secret commits, .gitignore and .gitleaks.toml allowlist configuration for false positive management, and git filter-branch command generation for history rewriting to remove exposed secrets. The skill generates severity-ranked reports with credential rotation checklists, links to provider-specific key rotation documentation, and estimated blast radius analysis based on the secret type and exposure duration."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/git-secret-scanner/"
framework:
  - "Claude Agents"
---

# Git Secret Scanner

The Git Secret Scanner skill identifies leaked credentials, API keys, tokens, and other secrets across Git repository history using multi-layered detection approaches. It combines pattern-based scanning inspired by Gitleaks rule definitions with entropy analysis to catch both known secret formats and high-entropy strings that may represent credentials.
The skill scans the complete Git history using git log –all -p –diff-filter=A to examine every added line across all branches and historical commits, including deleted branches accessible via reflog. It matches content against a comprehensive rule set covering AWS access keys (AKIA pattern), GitHub personal access tokens (ghp_/gho_/ghs_ prefixes), Slack webhooks, Stripe API keys, Google Cloud service account JSON, JWT tokens, and database connection strings.
Capabilities include integration with the GitHub Secret Scanning API via /repos/{owner}/{repo}/secret-scanning/alerts for repositories with GitHub Advanced Security, pre-commit hook generation using the pre-commit framework to prevent future secret commits, .gitignore and .gitleaks.toml allowlist configuration for false positive management, and git filter-branch command generation for history rewriting to remove exposed secrets. The skill generates severity-ranked reports with credential rotation checklists, links to provider-specific key rotation documentation, and estimated blast radius analysis based on the secret type and exposure duration.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/git-secret-scanner
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/git-secret-scanner` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/git-secret-scanner/)
