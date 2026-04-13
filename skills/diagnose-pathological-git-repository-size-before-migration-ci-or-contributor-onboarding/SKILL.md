---
title: "Diagnose pathological Git repository size before migration, CI, or contributor onboarding"
slug: "diagnose-pathological-git-repository-size-before-migration-ci-or-contributor-onboarding"
description: "Uses git-sizer to identify the specific size and history characteristics that make a repository painful to clone, fetch, repack, or work in. Use it when an agent needs evidence about large blobs, oversized trees, too many refs, or other Git pathologies before proposing cleanup."
verification: "security_reviewed"
source: "https://github.com/github/git-sizer"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "github/git-sizer"
  github_stars: 4013
---

# Diagnose pathological Git repository size before migration, CI, or contributor onboarding

Uses git-sizer to identify the specific size and history characteristics that make a repository painful to clone, fetch, repack, or work in. Use it when an agent needs evidence about large blobs, oversized trees, too many refs, or other Git pathologies before proposing cleanup.

## Installation

Choose the install method that fits your setup:

1. Install from Agent Skill Exchange
2. Install with OpenClaw skill tools
3. Clone or copy the upstream project files
4. Add the skill to your local skills directory manually
5. Use the upstream package or repo install flow directly

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diagnose-pathological-git-repository-size-before-migration-ci-or-contributor-onboarding/)
