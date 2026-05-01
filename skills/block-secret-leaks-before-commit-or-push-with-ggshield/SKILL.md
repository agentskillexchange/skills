---
title: "Block secret leaks before commit or push with ggshield"
description: "Scan staged changes, commits, or repositories for secrets before they leave the workstation or CI job, instead of relying on a later platform-side catch."
verification: "listed"
source: "https://github.com/GitGuardian/ggshield"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "GitGuardian/ggshield"
  github_stars: 1940
---

# Block secret leaks before commit or push with ggshield

Use ggshield when an agent needs a pre-commit, pre-push, or CI guardrail that checks code changes for leaked credentials before they are shared. The agent can scan staged diffs, recent commits, or whole repositories and return concrete secret findings early enough to stop the handoff. The scope boundary is specific: this skill is about running GitGuardian’s local scanning workflow at the change boundary, not about publishing a generic secret-management or SaaS product card.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/block-secret-leaks-before-commit-or-push-with-ggshield/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/block-secret-leaks-before-commit-or-push-with-ggshield
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/block-secret-leaks-before-commit-or-push-with-ggshield`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/block-secret-leaks-before-commit-or-push-with-ggshield/)
