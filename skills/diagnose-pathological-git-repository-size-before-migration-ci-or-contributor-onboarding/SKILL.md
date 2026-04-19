---
title: "Diagnose pathological Git repository size before migration, CI, or contributor onboarding"
description: "This skill uses git-sizer to inspect a local repository and explain why it has become slow, fragile, or expensive to operate. The tool computes size-related metrics across objects, trees, refs, blobs, path lengths, and history structure, then flags the areas most likely to create operational pain. For an agent, that turns an unfocused complaint like “this repo is miserable to clone” into a concrete diagnostic workflow with measurable findings. Invoke this before migrating a repository to a new host, before enabling heavier CI on a monorepo, before asking external contributors to clone it, or before deciding whether Git LFS, history rewriting, or repo splitting is justified. An agent can run the tool on a full non-shallow clone, interpret the flagged sections, and translate them into next actions such as pruning stale refs, moving large binary assets to Git LFS, rewriting history to remove oversized blobs, or sharding giant directories. It is especially useful when the team needs to know which class of Git problem they actually have instead of applying random cleanup folklore. The scope boundary is clear. This is not a Git hosting platform, not a backup tool, and not a general repository maintenance suite. It does one narrow job well: diagnose repository size pathologies so later remediation work is targeted. Integration points include migration runbooks, repository health checks, Git LFS adoption decisions, git-filter-repo cleanup work, and CI guardrails that fail when repositories cross size thresholds that hurt developer experience."
source: "https://github.com/github/git-sizer"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "github/git-sizer"
  github_stars: 4014
---

# Diagnose pathological Git repository size before migration, CI, or contributor onboarding

This skill uses git-sizer to inspect a local repository and explain why it has become slow, fragile, or expensive to operate. The tool computes size-related metrics across objects, trees, refs, blobs, path lengths, and history structure, then flags the areas most likely to create operational pain. For an agent, that turns an unfocused complaint like “this repo is miserable to clone” into a concrete diagnostic workflow with measurable findings. Invoke this before migrating a repository to a new host, before enabling heavier CI on a monorepo, before asking external contributors to clone it, or before deciding whether Git LFS, history rewriting, or repo splitting is justified. An agent can run the tool on a full non-shallow clone, interpret the flagged sections, and translate them into next actions such as pruning stale refs, moving large binary assets to Git LFS, rewriting history to remove oversized blobs, or sharding giant directories. It is especially useful when the team needs to know which class of Git problem they actually have instead of applying random cleanup folklore. The scope boundary is clear. This is not a Git hosting platform, not a backup tool, and not a general repository maintenance suite. It does one narrow job well: diagnose repository size pathologies so later remediation work is targeted. Integration points include migration runbooks, repository health checks, Git LFS adoption decisions, git-filter-repo cleanup work, and CI guardrails that fail when repositories cross size thresholds that hurt developer experience.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diagnose-pathological-git-repository-size-before-migration-ci-or-contributor-onboarding/)
