---
title: "Makefile Linting for CI and Build Pipelines"
description: "Uses checkmake to inspect Makefiles for style issues, fragile targets, and maintainability problems before build automation breaks in CI. It is a narrow build-script review skill for agents working inside repositories that already rely on make, not a generic build tool listing."
verification: "security_reviewed"
source: "https://github.com/checkmake/checkmake"
category: ["Code Quality &amp; Review"]
framework: ["Multi-Framework"]
---

# Makefile Linting for CI and Build Pipelines

Uses checkmake to inspect Makefiles for style issues, fragile targets, and maintainability problems before build automation breaks in CI. It is a narrow build-script review skill for agents working inside repositories that already rely on make, not a generic build tool listing.

## Installation

Choose the install path that fits your setup:

1. Install from the Agent Skill Exchange catalog if your agent client supports it.
2. Copy the skill folder into your local skills directory.
3. Add it as a git submodule in your shared agent-skills repo.
4. Vendor the files directly into a project-specific `.agents/skills/` or equivalent folder.
5. Keep a fork or mirror if you need local modifications or pinned revisions.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/makefile-linting-ci-build-pipelines/)
