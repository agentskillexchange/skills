---
title: "Rewrite Git history to purge secrets, binaries, or accidental paths before sharing a repo"
description: "This skill uses git-filter-repo from newren/git-filter-repo to perform controlled repository history rewrites. It is the right tool when an agent needs to remove secrets from old commits, strip large files, extract a subdirectory into its own module, rename tags during a split, or otherwise repair history before a repository is shared more widely. The upstream project positions it as the modern replacement for git filter-branch , with much better performance and far fewer ways to make a mess of the rewrite. A user should invoke this skill when the task is a bounded repository surgery problem, not ordinary day-to-day Git use. If a secret landed in history, if a binary bloated the repo for months, or if a team wants to publish only one part of a monorepo, the agent needs a repeatable cleanup playbook. That is where this becomes a skill rather than a product listing. The agent inspects the damage, chooses flags such as --path , --invert-paths , --replace-text , --to-subdirectory-filter , or --analyze , runs the rewrite in a safe clone, and then documents the risky human follow-up, especially force-push coordination and fresh clones for collaborators. The scope boundary is narrow and important. This is not a generic Git client, not a backup system, and not a repository browser. It is for history rewriting with explicit cleanup intent. Upstream documentation also spells out the prerequisites, including git &gt;= 2.36.0 and python3 &gt;= 3.6 , plus the simple installation path of putting the git-filter-repo script on $PATH . That makes it a strong fit for security remediation, repo extraction, and pre-publication cleanup workflows."
source: "https://github.com/newren/git-filter-repo"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "newren/git-filter-repo"
  github_stars: 12127
---

# Rewrite Git history to purge secrets, binaries, or accidental paths before sharing a repo

This skill uses git-filter-repo from newren/git-filter-repo to perform controlled repository history rewrites. It is the right tool when an agent needs to remove secrets from old commits, strip large files, extract a subdirectory into its own module, rename tags during a split, or otherwise repair history before a repository is shared more widely. The upstream project positions it as the modern replacement for git filter-branch , with much better performance and far fewer ways to make a mess of the rewrite. A user should invoke this skill when the task is a bounded repository surgery problem, not ordinary day-to-day Git use. If a secret landed in history, if a binary bloated the repo for months, or if a team wants to publish only one part of a monorepo, the agent needs a repeatable cleanup playbook. That is where this becomes a skill rather than a product listing. The agent inspects the damage, chooses flags such as --path , --invert-paths , --replace-text , --to-subdirectory-filter , or --analyze , runs the rewrite in a safe clone, and then documents the risky human follow-up, especially force-push coordination and fresh clones for collaborators. The scope boundary is narrow and important. This is not a generic Git client, not a backup system, and not a repository browser. It is for history rewriting with explicit cleanup intent. Upstream documentation also spells out the prerequisites, including git &gt;= 2.36.0 and python3 &gt;= 3.6 , plus the simple installation path of putting the git-filter-repo script on $PATH . That makes it a strong fit for security remediation, repo extraction, and pre-publication cleanup workflows.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rewrite-git-history-to-purge-secrets-binaries-or-accidental-paths-before-sharing-a-repo/)
