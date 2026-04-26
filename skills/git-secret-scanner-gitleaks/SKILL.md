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

Scans Git repositories for leaked secrets using Gitleaks, TruffleHog, and custom regex patterns. Detects API keys, AWS credentials, private keys, and database connection strings across commit history.

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
