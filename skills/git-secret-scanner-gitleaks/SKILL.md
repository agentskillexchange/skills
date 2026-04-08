---
title: Git Secret Scanner with Gitleaks
description: This skill performs thorough secret detection across Git repository history
  using multiple scanning engines. It runs Gitleaks with both default and custom rule
  configurations to scan all commits, branches, and tags for exposed credentials.
  TruffleHog provides entropy-based detection for high-randomness strings that may
  be secrets without matching known patterns. The skill scans for AWS access keys
  and secret keys, Google Cloud service account JSON files, GitHub personal access
  tokens, Stripe API keys, database connection strings with embedded passwords, and
  SSH private keys. It analyzes .gitignore and .gitleaksignore configurations for
  gaps, checks pre-commit hook configurations for secret prevention, and validates
  that detected secrets are actually live by testing them against their respective
  APIs (with read-only operations). Reports include commit SHA, author, file path,
  and line number for each finding, with severity classification and remediation instructions
  including git filter-branch or BFG Repo-Cleaner commands for history rewriting.
verification: security_reviewed
source: https://agentskillexchange.com/skills/git-secret-scanner-gitleaks/
category:
- Security &amp; Verification
framework:
- Claude Code
---

# Git Secret Scanner with Gitleaks

This skill performs thorough secret detection across Git repository history using multiple scanning engines. It runs Gitleaks with both default and custom rule configurations to scan all commits, branches, and tags for exposed credentials. TruffleHog provides entropy-based detection for high-randomness strings that may be secrets without matching known patterns. The skill scans for AWS access keys and secret keys, Google Cloud service account JSON files, GitHub personal access tokens, Stripe API keys, database connection strings with embedded passwords, and SSH private keys. It analyzes .gitignore and .gitleaksignore configurations for gaps, checks pre-commit hook configurations for secret prevention, and validates that detected secrets are actually live by testing them against their respective APIs (with read-only operations). Reports include commit SHA, author, file path, and line number for each finding, with severity classification and remediation instructions including git filter-branch or BFG Repo-Cleaner commands for history rewriting.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/git-secret-scanner-gitleaks/)
