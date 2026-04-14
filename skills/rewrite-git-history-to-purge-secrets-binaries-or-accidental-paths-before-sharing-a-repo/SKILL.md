---
title: "Rewrite Git history to purge secrets, binaries, or accidental paths before sharing a repo"
slug: "rewrite-git-history-to-purge-secrets-binaries-or-accidental-paths-before-sharing-a-repo"
verification: security_reviewed
source: "https://github.com/newren/git-filter-repo"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "newren/git-filter-repo"
  github_stars: 12127
---
# Rewrite Git history to purge secrets, binaries, or accidental paths before sharing a repo

Use git-filter-repo when an agent needs to surgically rewrite repository history after a leaked secret, a huge binary commit, or a bad subtree split. The agent analyzes the problem, builds the rewrite command, and leaves a clean follow-up checklist for force-push, clone reset, and downstream cleanup.

## Installation

Choose the method that fits your setup:

1. Install from Agent Skill Exchange
2. Clone or download the upstream project
3. Install with the upstream package manager
4. Add the skill to your local skills directory
5. Follow the upstream documentation for environment-specific setup

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rewrite-git-history-to-purge-secrets-binaries-or-accidental-paths-before-sharing-a-repo/)
