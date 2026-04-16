---
title: "Git Secret Scanner with Gitleaks"
description: "Scans Git repositories for leaked secrets using Gitleaks, TruffleHog, and custom regex patterns. Detects API keys, AWS credentials, private keys, and database connection strings across commit history."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/git-secret-scanner-gitleaks/"
category:
  - "Security &amp; Verification"
framework:
  - "Claude Code"
---

# Git Secret Scanner with Gitleaks

This skill performs thorough secret detection across Git repository history using multiple scanning engines. It runs Gitleaks with both default and custom rule configurations to scan all commits, branches, and tags for exposed credentials. TruffleHog provides entropy-based detection for high-randomness strings that may be secrets without matching known patterns. The skill scans for AWS access keys and secret keys, Google Cloud service account JSON files, GitHub personal access tokens, Stripe API keys, database connection strings with embedded passwords, and SSH private keys. It analyzes .gitignore and .gitleaksignore configurations for gaps, checks pre-commit hook configurations for secret prevention, and validates that detected secrets are actually live by testing them against their respective APIs (with read-only operations). Reports include commit SHA, author, file path, and line number for each finding, with severity classification and remediation instructions including git filter-branch or BFG Repo-Cleaner commands for history rewriting.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/git-secret-scanner-gitleaks/)
