---
title: "Audit GitHub Actions workflows for insecure permissions and unpinned actions"
description: "This ASE skill uses zizmor to audit GitHub Actions workflows and composite actions for security mistakes before they ship. An agent can scan local repos or remote GitHub repositories, flag risky permission scopes and unsafe workflow patterns, and return plain output, GitHub-native findings, or SARIF for follow-up automation."
verification: "security_reviewed"
source: "https://github.com/zizmorcore/zizmor"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "zizmorcore/zizmor"
  github_stars: 4145
---

# Audit GitHub Actions workflows for insecure permissions and unpinned actions

This ASE skill uses zizmor to audit GitHub Actions workflows and composite actions for security mistakes before they ship. An agent can scan local repos or remote GitHub repositories, flag risky permission scopes and unsafe workflow patterns, and return plain output, GitHub-native findings, or SARIF for follow-up automation.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/audit-github-actions-workflows-for-insecure-permissions-and-unpinned-actions/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/audit-github-actions-workflows-for-insecure-permissions-and-unpinned-actions
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/audit-github-actions-workflows-for-insecure-permissions-and-unpinned-actions`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-github-actions-workflows-for-insecure-permissions-and-unpinned-actions/)
