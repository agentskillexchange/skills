---
title: "Gate pull requests with targeted diff-aware AI security review using Claude Code Security Review"
description: "Run a Claude Code powered security review pass on trusted pull requests so suspicious auth, secret, injection, and unsafe logic changes surface before merge."
verification: "security_reviewed"
source: "https://github.com/anthropics/claude-code-security-review"
category:
  - "Security & Verification"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "anthropics/claude-code-security-review"
  github_stars: 4304
---

# Gate pull requests with targeted diff-aware AI security review using Claude Code Security Review

This skill is for repositories that want a dedicated security-focused AI review pass inside GitHub Actions. It covers the workflow of triggering on trusted pull requests, scanning only the changed code, tuning false-positive filtering, and posting findings back to the pull request for human review. Invoke this instead of using Claude Code manually when you need a repeatable, CI-native security checkpoint rather than an informal one-off review. It fits best when maintainers want security findings attached to the PR discussion and governed by normal merge policy. The scope boundary is tight: this is not a general Claude Code listing and not a generic SAST product card. It is specifically the GitHub Action workflow for AI-assisted security review of pull request diffs.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/gate-pull-requests-with-targeted-diff-aware-ai-security-review-using-claude-code-security-review/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/gate-pull-requests-with-targeted-diff-aware-ai-security-review-using-claude-code-security-review
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/gate-pull-requests-with-targeted-diff-aware-ai-security-review-using-claude-code-security-review`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gate-pull-requests-with-targeted-diff-aware-ai-security-review-using-claude-code-security-review/)
