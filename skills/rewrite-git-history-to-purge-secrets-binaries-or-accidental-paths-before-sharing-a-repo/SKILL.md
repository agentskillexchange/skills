---
title: "Rewrite Git history to purge secrets, binaries, or accidental paths before sharing a repo"
description: "Use git-filter-repo when an agent needs to surgically rewrite repository history after a leaked secret, a huge binary commit, or a bad subtree split. The agent analyzes the problem, builds the rewrite command, and leaves a clean follow-up checklist for force-push, clone reset, and downstream cleanup."
verification: "listed"
source: "https://github.com/newren/git-filter-repo"
categories:
  - "Runbooks &amp; Diagnostics"
frameworks:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "newren/git-filter-repo"
  github_stars: 12122
---

# Rewrite Git history to purge secrets, binaries, or accidental paths before sharing a repo

Use git-filter-repo when an agent needs to surgically rewrite repository history after a leaked secret, a huge binary commit, or a bad subtree split. The agent analyzes the problem, builds the rewrite command, and leaves a clean follow-up checklist for force-push, clone reset, and downstream cleanup.

## Installation

You can install this skill using one of these methods:

1. Install from Agent Skill Exchange in OpenClaw
2. Install from ClawHub
3. Copy the skill folder into your local skills directory
4. Add it as a git submodule or synced folder in your workspace
5. Use your team or org skill distribution workflow

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rewrite-git-history-to-purge-secrets-binaries-or-accidental-paths-before-sharing-a-repo/)
