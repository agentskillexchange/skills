---
title: "Rewrite Git history to purge secrets, binaries, or accidental paths before sharing a repo"
slug: "rewrite-git-history-to-purge-secrets-binaries-or-accidental-paths-before-sharing-a-repo"
description: "Use git-filter-repo when an agent needs to surgically rewrite repository history after a leaked secret, a huge binary commit, or a bad subtree split. The agent analyzes the problem, builds the rewrite command, and leaves a clean follow-up checklist for force-push, clone reset, and downstream cleanup."
verification: verified
source: "https://github.com/newren/git-filter-repo"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "newren/git-filter-repo"
  github_stars: 12127
---
# Rewrite Git history to purge secrets, binaries, or accidental paths before sharing a repo

Use git-filter-repo when an agent needs to surgically rewrite repository history after a leaked secret, a huge binary commit, or a bad subtree split. The agent analyzes the problem, builds the rewrite command, and leaves a clean follow-up checklist for force-push, clone reset, and downstream cleanup.

## Installation

1. Clone this skill repository.
2. Open this skill folder.
3. Review prerequisites and setup needs.
4. Install required dependencies.
5. Run and test in your environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rewrite-git-history-to-purge-secrets-binaries-or-accidental-paths-before-sharing-a-repo/)
