---
name: "rewrite-git-history-to-purge-secrets-binaries-or-accidental-paths-before-sharing-a-repo"
title: "Rewrite Git history to purge secrets, binaries, or accidental paths before sharing a repo"
description: "Use git-filter-repo when an agent needs to surgically rewrite repository history after a leaked secret, a huge binary commit, or a bad subtree split. The agent analyzes the problem, builds the rewrite command, and leaves a clean follow-up checklist for force-push, clone reset, and downstream cleanup."
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/newren/git-filter-repo"
tool_ecosystem:
  github_repo: "newren/git-filter-repo"
  github_stars: 12123
---

# Rewrite Git history to purge secrets, binaries, or accidental paths before sharing a repo

Use git-filter-repo when an agent needs to surgically rewrite repository history after a leaked secret, a huge binary commit, or a bad subtree split. The agent analyzes the problem, builds the rewrite command, and leaves a clean follow-up checklist for force-push, clone reset, and downstream cleanup.

## Installation

You can install this skill using any of these methods:

1. OpenClaw skill installer
2. ClawHub CLI
3. Git clone into your skills directory
4. Download and extract the skill folder manually
5. Copy the skill folder from a local checkout

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rewrite-git-history-to-purge-secrets-binaries-or-accidental-paths-before-sharing-a-repo/)
