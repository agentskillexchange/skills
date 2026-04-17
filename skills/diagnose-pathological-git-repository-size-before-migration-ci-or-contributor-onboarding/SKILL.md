---
title: "Diagnose pathological Git repository size before migration, CI, or contributor onboarding"
description: "This skill uses git-sizer to inspect a local repository and explain why it has become slow, fragile, or expensive to operate. The tool computes size-related metrics across objects, trees, refs, blobs, path lengths, and history structure, then flags the areas most likely to create operational pain. For an agent, that turns an unfocused complaint like “this repo is miserable to clone” into a concrete diagnostic workflow with measurable findings.\nInvoke this before migrating a repository to a new host, before enabling heavier CI on a monorepo, before asking external contributors to clone it, or before deciding whether Git LFS, history rewriting, or repo splitting is justified. An agent can run the tool on a full non-shallow clone, interpret the flagged sections, and translate them into next actions such as pruning stale refs, moving large binary assets to Git LFS, rewriting history to remove oversized blobs, or sharding giant directories. It is especially useful when the team needs to know which class of Git problem they actually have instead of applying random cleanup folklore.\nThe scope boundary is clear. This is not a Git hosting platform, not a backup tool, and not a general repository maintenance suite. It does one narrow job well: diagnose repository size pathologies so later remediation work is targeted. Integration points include migration runbooks, repository health checks, Git LFS adoption decisions, git-filter-repo cleanup work, and CI guardrails that fail when repositories cross size thresholds that hurt developer experience."
verification: security_reviewed
source: "https://github.com/github/git-sizer"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "github/git-sizer"
  github_stars: 4014
---

# Diagnose pathological Git repository size before migration, CI, or contributor onboarding

This skill uses git-sizer to inspect a local repository and explain why it has become slow, fragile, or expensive to operate. The tool computes size-related metrics across objects, trees, refs, blobs, path lengths, and history structure, then flags the areas most likely to create operational pain. For an agent, that turns an unfocused complaint like “this repo is miserable to clone” into a concrete diagnostic workflow with measurable findings.
Invoke this before migrating a repository to a new host, before enabling heavier CI on a monorepo, before asking external contributors to clone it, or before deciding whether Git LFS, history rewriting, or repo splitting is justified. An agent can run the tool on a full non-shallow clone, interpret the flagged sections, and translate them into next actions such as pruning stale refs, moving large binary assets to Git LFS, rewriting history to remove oversized blobs, or sharding giant directories. It is especially useful when the team needs to know which class of Git problem they actually have instead of applying random cleanup folklore.
The scope boundary is clear. This is not a Git hosting platform, not a backup tool, and not a general repository maintenance suite. It does one narrow job well: diagnose repository size pathologies so later remediation work is targeted. Integration points include migration runbooks, repository health checks, Git LFS adoption decisions, git-filter-repo cleanup work, and CI guardrails that fail when repositories cross size thresholds that hurt developer experience.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/diagnose-pathological-git-repository-size-before-migration-ci-or-contributor-onboarding
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/diagnose-pathological-git-repository-size-before-migration-ci-or-contributor-onboarding` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diagnose-pathological-git-repository-size-before-migration-ci-or-contributor-onboarding/)
