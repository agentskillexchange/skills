---
name: "Diagnose pathological Git repository size before migration, CI, or contributor onboarding"
slug: "diagnose-pathological-git-repository-size-before-migration-ci-or-contributor-onboarding"
description: "Uses git-sizer to identify the specific size and history characteristics that make a repository painful to clone, fetch, repack, or work in. Use it when an agent needs evidence about large blobs, oversized trees, too many refs, or other Git pathologies before proposing cleanup."
github_stars: 4014
verification: "security_reviewed"
source: "https://github.com/github/git-sizer"
author: "GitHub"
publisher_type: "Company"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "github/git-sizer"
  github_stars: 4014
---

# Diagnose pathological Git repository size before migration, CI, or contributor onboarding

Uses git-sizer to identify the specific size and history characteristics that make a repository painful to clone, fetch, repack, or work in. Use it when an agent needs evidence about large blobs, oversized trees, too many refs, or other Git pathologies before proposing cleanup.

## Prerequisites

Git 2.6 or newer and a full non-shallow clone of the repository being analyzed

## Installation

Basic usage or getting-started notes:
- git-sizer computes various size metrics for a local Git repository, flagging those that might cause you problems or inconvenience. For example:
- Consider using ["git notes"](https://git-scm.com/docs/git-notes) rather than tags to attach auxiliary information to commits (for example, CI build results).
- Does the repository include too many objects? The more objects, the longer it takes for Git to traverse the repository's history, for example when garbage-collecting. Suggestions:

- Source: https://github.com/github/git-sizer
- Extracted from upstream docs: https://raw.githubusercontent.com/github/git-sizer/HEAD/README.md

## Documentation

- https://github.com/github/git-sizer

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diagnose-pathological-git-repository-size-before-migration-ci-or-contributor-onboarding/)
