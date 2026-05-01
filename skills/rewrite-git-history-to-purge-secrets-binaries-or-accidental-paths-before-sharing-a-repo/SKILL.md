---
title: "Rewrite Git history to purge secrets, binaries, or accidental paths before sharing a repo"
description: "Use git-filter-repo when an agent needs to surgically rewrite repository history after a leaked secret, a huge binary commit, or a bad subtree split. The agent analyzes the problem, builds the rewrite command, and leaves a clean follow-up checklist for force-push, clone reset, and downstream cleanup."
verification: "security_reviewed"
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

This skill uses git-filter-repo from newren/git-filter-repo to perform controlled repository history rewrites. It is the right tool when an agent needs to remove secrets from old commits, strip large files, extract a subdirectory into its own module, rename tags during a split, or otherwise repair history before a repository is shared more widely. The upstream project positions it as the modern replacement for git filter-branch, with much better performance and far fewer ways to make a mess of the rewrite.

A user should invoke this skill when the task is a bounded repository surgery problem, not ordinary day-to-day Git use. If a secret landed in history, if a binary bloated the repo for months, or if a team wants to publish only one part of a monorepo, the agent needs a repeatable cleanup playbook. That is where this becomes a skill rather than a product listing. The agent inspects the damage, chooses flags such as --path, --invert-paths, --replace-text, --to-subdirectory-filter, or --analyze, runs the rewrite in a safe clone, and then documents the risky human follow-up, especially force-push coordination and fresh clones for collaborators.

The scope boundary is narrow and important. This is not a generic Git client, not a backup system, and not a repository browser. It is for history rewriting with explicit cleanup intent. Upstream documentation also spells out the prerequisites, including git >= 2.36.0 and python3 >= 3.6, plus the simple installation path of putting the git-filter-repo script on $PATH. That makes it a strong fit for security remediation, repo extraction, and pre-publication cleanup workflows.

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
