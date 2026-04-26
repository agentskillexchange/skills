---
title: "Gitleaks Git Repository Secret Scanner"
description: "Gitleaks is an open-source SAST tool for detecting hardcoded secrets like passwords, API keys, and tokens in Git repositories, files, and directories. With 24,000+ GitHub stars and 20 million Docker downloads, it is the most widely adopted open-source secret scanner."
verification: "security_reviewed"
source: "https://github.com/gitleaks/gitleaks"
category:
  - "Security & Verification"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "gitleaks/gitleaks"
  github_stars: 25731
---

# Gitleaks Git Repository Secret Scanner

Gitleaks is a static analysis security testing (SAST) tool purpose-built for finding secrets in source code, available at github.com/gitleaks/gitleaks with over 24,000 GitHub stars, 20 million Docker downloads, and 14 million GitHub downloads. It scans Git repositories, arbitrary files, directories, and stdin for hardcoded credentials including API keys, passwords, private keys, and authentication tokens.

The detection engine uses a regex-based approach with entropy analysis to minimize false positives. Gitleaks ships with a comprehensive set of built-in rules covering hundreds of secret patterns from major providers including AWS, GCP, Azure, GitHub, Slack, Stripe, Twilio, SendGrid, and many others. Each finding includes the secret value, the rule that matched, the entropy score, the file path and line number, the commit hash and author, and a unique fingerprint for deduplication across scans.

Gitleaks operates in two primary modes. The git command scans the full Git history of a repository, catching secrets that were committed and later removed but still exist in the commit log. The dir command scans the current filesystem state, useful for pre-commit checks or scanning non-Git directories. Both modes support JSON, CSV, JUnit, and SARIF output formats for integration with CI dashboards and security platforms.

Integration paths include a first-party GitHub Action (gitleaks-action) that runs on pull requests and pushes, pre-commit hooks via the pre-commit framework for catching secrets before they enter the repository, and direct CLI usage in any CI/CD pipeline. Installation is available through Homebrew, Docker (both DockerHub and GitHub Container Registry), and Go install.

For agent skills focused on security scanning, code review, or CI/CD pipeline hardening, Gitleaks provides the secret detection layer. An agent can run Gitleaks against a repository before a merge, parse the structured output to identify which secrets were exposed, and suggest remediation steps like rotating the compromised credential and adding the pattern to a baseline file. Its SARIF output integrates with GitHub Advanced Security for dashboard visibility.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/gitleaks-git-secret-scanner/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/gitleaks-git-secret-scanner
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/gitleaks-git-secret-scanner`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gitleaks-git-secret-scanner/)
