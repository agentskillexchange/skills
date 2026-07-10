---
title: "Git Secret Scanner with Gitleaks"
description: "Scans Git repositories for leaked secrets using Gitleaks, TruffleHog, and custom regex patterns. Detects API keys, AWS credentials, private keys, and database connection strings across commit history."
verification: "security_reviewed"
source: "https://github.com/gitleaks/gitleaks"
author: "Gitleaks"
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

## Prerequisites

Git

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
brew install gitleaks
```

## Documentation

- https://github.com/gitleaks/gitleaks#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/git-secret-scanner-gitleaks/)
