---
title: "Diagnose pathological Git repository size before migration, CI, or contributor onboarding"
description: "Uses git-sizer to identify the specific size and history characteristics that make a repository painful to clone, fetch, repack, or work in. Use it when an agent needs evidence about large blobs, oversized trees, too many refs, or other Git pathologies before proposing cleanup."
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diagnose-pathological-git-repository-size-before-migration-ci-or-contributor-onboarding/)
