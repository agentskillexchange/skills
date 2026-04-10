---
title: "Git Secret Scanner with Gitleaks"
description: "Scans Git repositories for leaked secrets using Gitleaks, TruffleHog, and custom regex patterns. Detects API keys, AWS credentials, private keys, and database connection strings across commit history."
slug: "git-secret-scanner-gitleaks"
category:
  - "Security &amp; Verification"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/git-secret-scanner-gitleaks/"
---

# Git Secret Scanner with Gitleaks

Scans Git repositories for leaked secrets using Gitleaks, TruffleHog, and custom regex patterns. Detects API keys, AWS credentials, private keys, and database connection strings across commit history.

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
clawhub install git-secret-scanner-gitleaks
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill performs thorough secret detection across Git repository history using multiple scanning engines. It runs Gitleaks with both default and custom rule configurations to scan all commits, branches, and tags for exposed credentials. TruffleHog provides entropy-based detection for high-randomness strings that may be secrets without matching known patterns. The skill scans for AWS access keys and secret keys, Google Cloud service account JSON files, GitHub personal access tokens, Stripe API keys, database connection strings with embedded passwords, and SSH private keys. It analyzes .gitignore and .gitleaksignore configurations for gaps, checks pre-commit hook configurations for secret prevention, and validates that detected secrets are actually live by testing them against their respective APIs (with read-only operations). Reports include commit SHA, author, file path, and line number for each finding, with severity classification and remediation instructions including git filter-branch or BFG Repo-Cleaner commands for history rewriting.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/git-secret-scanner-gitleaks/)
