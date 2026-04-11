---
title: "Rewrite Git history to purge secrets, binaries, or accidental paths before sharing a repo"
description: "Use git-filter-repo when an agent needs to surgically rewrite repository history after a leaked secret, a huge binary commit, or a bad subtree split. The agent analyzes the problem, builds the rewrite command, and leaves a clean follow-up checklist for force-push, clone reset, and downstream cleanup."
slug: rewrite-git-history-to-purge-secrets-binaries-or-accidental-paths-before-sharing-a-repo
verification: listed
source: "https://github.com/newren/git-filter-repo"
category:
- "Runbooks & Diagnostics"
framework:
- "Multi-Framework"
tool_ecosystem:
  github_repo: newren/git-filter-repo
  github_stars: 12122
---
# Rewrite Git history to purge secrets, binaries, or accidental paths before sharing a repo

Use git-filter-repo when an agent needs to surgically rewrite repository history after a leaked secret, a huge binary commit, or a bad subtree split. The agent analyzes the problem, builds the rewrite command, and leaves a clean follow-up checklist for force-push, clone reset, and downstream cleanup.

## Installation

You can install this skill in any of these ways:

1. Browse and install from Agent Skill Exchange.
2. Clone or download this repository and copy the skill folder into your local skills directory.
3. Add it as a git submodule in your skills workspace.
4. Install it with your preferred agent skill or package manager if your setup supports that.
5. Copy the `SKILL.md` into an existing skill folder and adapt any referenced assets as needed.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rewrite-git-history-to-purge-secrets-binaries-or-accidental-paths-before-sharing-a-repo/)
