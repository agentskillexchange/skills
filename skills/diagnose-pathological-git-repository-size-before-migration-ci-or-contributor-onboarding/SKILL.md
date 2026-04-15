---
title: "Diagnose pathological Git repository size before migration, CI, or contributor onboarding"
description: "Uses git-sizer to identify the specific size and history characteristics that make a repository painful to clone, fetch, repack, or work in. Use it when an agent needs evidence about large blobs, oversized trees, too many refs, or other Git pathologies before proposing cleanup."
verification: listed
source: "https://agentskillexchange.com/skills/diagnose-pathological-git-repository-size-before-migration-ci-or-contributor-onboarding/"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Multi-Framework"
---

# Diagnose pathological Git repository size before migration, CI, or contributor onboarding

Uses git-sizer to identify the specific size and history characteristics that make a repository painful to clone, fetch, repack, or work in. Use it when an agent needs evidence about large blobs, oversized trees, too many refs, or other Git pathologies before proposing cleanup.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diagnose-pathological-git-repository-size-before-migration-ci-or-contributor-onboarding/)
