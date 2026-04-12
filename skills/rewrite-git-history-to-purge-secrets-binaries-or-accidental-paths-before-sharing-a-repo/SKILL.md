---
title: "Rewrite Git history to purge secrets, binaries, or accidental paths before sharing a repo"
slug: "rewrite-git-history-to-purge-secrets-binaries-or-accidental-paths-before-sharing-a-repo"
description: "Use git-filter-repo when an agent needs to surgically rewrite repository history after a leaked secret, a huge binary commit, or a bad subtree split. The agent analyzes the problem, builds the rewrite command, and leaves a clean follow-up checklist for force-push, clone reset, and downstream cleanup."
verification: security_reviewed
source: "https://github.com/newren/git-filter-repo"
category:
  - "Runbooks &amp; Diagnostics"
tool_ecosystem:
  github_repo: "https://github.com/newren/git-filter-repo"
  github_stars: 12123
---

# Rewrite Git history to purge secrets, binaries, or accidental paths before sharing a repo

Use git-filter-repo when an agent needs to surgically rewrite repository history after a leaked secret, a huge binary commit, or a bad subtree split. The agent analyzes the problem, builds the rewrite command, and leaves a clean follow-up checklist for force-push, clone reset, and downstream cleanup.

## Installation

Choose the setup path that fits your environment:

1. Install from the Agent Skill Exchange UI
2. Clone or download this skill into your skills directory
3. Install with your agent platform's skill manager, if supported
4. Vendor the skill into your workspace or repo
5. Copy the skill files manually for local customization

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rewrite-git-history-to-purge-secrets-binaries-or-accidental-paths-before-sharing-a-repo/)
