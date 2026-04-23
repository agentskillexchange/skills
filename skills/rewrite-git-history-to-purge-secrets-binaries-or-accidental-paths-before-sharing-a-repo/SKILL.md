---
title: "Rewrite Git history to purge secrets, binaries, or accidental paths before sharing a repo"
description: "Use git-filter-repo when an agent needs to surgically rewrite repository history after a leaked secret, a huge binary commit, or a bad subtree split. The agent analyzes the problem, builds the rewrite command, and leaves a clean follow-up checklist for force-push, clone reset, and downstream cleanup."
verification: security_reviewed
source: "https://github.com/newren/git-filter-repo"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "newren/git-filter-repo"
  github_stars: 12127
---

# Rewrite Git history to purge secrets, binaries, or accidental paths before sharing a repo

Use git-filter-repo when an agent needs to surgically rewrite repository history after a leaked secret, a huge binary commit, or a bad subtree split. The agent analyzes the problem, builds the rewrite command, and leaves a clean follow-up checklist for force-push, clone reset, and downstream cleanup.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/rewrite-git-history-to-purge-secrets-binaries-or-accidental-paths-before-sharing-a-repo/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/rewrite-git-history-to-purge-secrets-binaries-or-accidental-paths-before-sharing-a-repo
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/rewrite-git-history-to-purge-secrets-binaries-or-accidental-paths-before-sharing-a-repo`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rewrite-git-history-to-purge-secrets-binaries-or-accidental-paths-before-sharing-a-repo/)
