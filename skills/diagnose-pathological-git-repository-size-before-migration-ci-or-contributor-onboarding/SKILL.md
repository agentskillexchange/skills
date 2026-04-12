---
title: "Diagnose pathological Git repository size before migration, CI, or contributor onboarding"
description: "Uses git-sizer to identify the specific size and history characteristics that make a repository painful to clone, fetch, repack, or work in. Use it when an agent needs evidence about large blobs, oversized trees, too many refs, or other Git pathologies before proposing cleanup."
verification: security_reviewed
source: "https://github.com/github/git-sizer"
---

# Diagnose pathological Git repository size before migration, CI, or contributor onboarding

Uses git-sizer to identify the specific size and history characteristics that make a repository painful to clone, fetch, repack, or work in. Use it when an agent needs evidence about large blobs, oversized trees, too many refs, or other Git pathologies before proposing cleanup.

## Installation

Choose the path that fits your setup:

1. Clone this repository and use the skill locally.
2. Copy the skill folder into your local skills directory.
3. Add the skill as a Git submodule in your skills workspace.
4. Vendor the files into an internal skill catalog for your team.
5. Reference the upstream source and recreate the skill in your own agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diagnose-pathological-git-repository-size-before-migration-ci-or-contributor-onboarding/)
