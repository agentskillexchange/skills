---
name: "Git Secret Scanner with Gitleaks"
description: "Scans Git repositories for leaked secrets using Gitleaks, TruffleHog, and custom regex patterns. Detects API keys, AWS credentials, private keys, and database connection strings across commit history."
category: "Security & Verification"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/git-secret-scanner-gitleaks/"
tool_ecosystem:
  tool: stripe
  github_stars: 4377
  npm_weekly_downloads: 8442269
  github_repo: stripe/stripe-node
  license: MIT
  maintained: true
---
# Git Secret Scanner with Gitleaks

Scans Git repositories for leaked secrets using Gitleaks, TruffleHog, and custom regex patterns. Detects API keys, AWS credentials, private keys, and database connection strings across commit history.

## Overview

This skill performs thorough secret detection across Git repository history using multiple scanning engines. It runs Gitleaks with both default and custom rule configurations to scan all commits, branches, and tags for exposed credentials. TruffleHog provides entropy-based detection for high-randomness strings that may be secrets without matching known patterns. The skill scans for AWS access keys and secret keys, Google Cloud service account JSON files, GitHub personal access tokens, Stripe API keys, database connection strings with embedded passwords, and SSH private keys. It analyzes .gitignore and .gitleaksignore configurations for gaps, checks pre-commit hook configurations for secret prevention, and validates that detected secrets are actually live by testing them against their respective APIs (with read-only operations). Reports include commit SHA, author, file path, and line number for each finding, with severity classification and remediation instructions including git filter-branch or BFG Repo-Cleaner commands for history rewriting.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill git-secret-scanner-gitleaks
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill git-secret-scanner-gitleaks -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill git-secret-scanner-gitleaks -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill git-secret-scanner-gitleaks -a codex
```

### OpenClaw

```bash
clawhub install git-secret-scanner-gitleaks
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/git-secret-scanner-gitleaks/)
