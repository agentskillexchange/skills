---
title: "Diagnose pathological Git repository size before migration, CI, or contributor onboarding"
slug: "diagnose-pathological-git-repository-size-before-migration-ci-or-contributor-onboarding"
verification: security_reviewed
source: "https://github.com/github/git-sizer"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "github/git-sizer"
  github_stars: 4014
---
# Diagnose pathological Git repository size before migration, CI, or contributor onboarding

Uses git-sizer to identify the specific size and history characteristics that make a repository painful to clone, fetch, repack, or work in. Use it when an agent needs evidence about large blobs, oversized trees, too many refs, or other Git pathologies before proposing cleanup.

## Installation

Choose the method that fits your setup:

1. Install from Agent Skill Exchange
2. Clone or download the upstream project
3. Install with the upstream package manager
4. Add the skill to your local skills directory
5. Follow the upstream documentation for environment-specific setup

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diagnose-pathological-git-repository-size-before-migration-ci-or-contributor-onboarding/)
