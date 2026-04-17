---
name: Audit GitHub Actions workflows for insecure permissions and unpinned actions
description: This ASE skill uses zizmor to audit GitHub Actions workflows and composite
  actions for security mistakes before they ship. An agent can scan local repos or
  remote GitHub repositories, flag risky permission scopes and unsafe workflow patterns,
  and return plain output, GitHub-native findings, or SARIF for follow-up automation.
category: Security & Verification
framework: Multi-Framework
verification: security_reviewed
source: https://github.com/zizmorcore/zizmor
tool_ecosystem:
  github_repo: zizmorcore/zizmor
  github_stars: 4145
  tool: zizmor
---
# Audit GitHub Actions workflows for insecure permissions and unpinned actions
This ASE skill uses zizmor to audit GitHub Actions workflows and composite actions for security mistakes before they ship. An agent can scan local repos or remote GitHub repositories, flag risky permission scopes and unsafe workflow patterns, and return plain output, GitHub-native findings, or SARIF for follow-up automation.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/audit-github-actions-workflows-for-insecure-permissions-and-unpinned-actions
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/audit-github-actions-workflows-for-insecure-permissions-and-unpinned-actions` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-github-actions-workflows-for-insecure-permissions-and-unpinned-actions/)
