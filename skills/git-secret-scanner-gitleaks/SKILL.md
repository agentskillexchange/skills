---
title: "Git Secret Scanner with Gitleaks"
description: "Scans Git repositories for leaked secrets using Gitleaks, TruffleHog, and custom regex patterns. Detects API keys, AWS credentials, private keys, and database connection strings across commit history."
verification: "security_reviewed"
source: "https://github.com/gitleaks/gitleaks"
category:
  - "Security & Verification"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "gitleaks/gitleaks"
  github_stars: 26101
---

# Git Secret Scanner with Gitleaks

This skill performs thorough secret detection across Git repository history using multiple scanning engines. It runs Gitleaks with both default and custom rule configurations to scan all commits, branches, and tags for exposed credentials. TruffleHog provides entropy-based detection for high-randomness strings that may be secrets without matching known patterns. The skill scans for AWS access keys and secret keys, Google Cloud service account JSON files, GitHub personal access tokens, Stripe API keys, database connection strings with embedded passwords, and SSH private keys. It analyzes .gitignore and .gitleaksignore configurations for gaps, checks pre-commit hook configurations for secret prevention, and validates that detected secrets are actually live by testing them against their respective APIs (with read-only operations). Reports include commit SHA, author, file path, and line number for each finding, with severity classification and remediation instructions including git filter-branch or BFG Repo-Cleaner commands for history rewriting.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/git-secret-scanner-gitleaks/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/git-secret-scanner-gitleaks
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/git-secret-scanner-gitleaks`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/git-secret-scanner-gitleaks/)
