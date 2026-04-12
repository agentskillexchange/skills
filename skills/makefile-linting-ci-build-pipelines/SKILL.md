---
title: "Makefile Linting for CI and Build Pipelines"
description: "Uses checkmake to inspect Makefiles for style issues, fragile targets, and maintainability problems before build automation breaks in CI. It is a narrow build-script review skill for agents working inside repositories that already rely on make, not a generic build tool listing."
verification: security_reviewed
source: "https://github.com/checkmake/checkmake"
---

# Makefile Linting for CI and Build Pipelines

Uses checkmake to inspect Makefiles for style issues, fragile targets, and maintainability problems before build automation breaks in CI. It is a narrow build-script review skill for agents working inside repositories that already rely on make, not a generic build tool listing.

## Installation

Choose the path that fits your setup:

1. Clone this repository and use the skill locally.
2. Copy the skill folder into your local skills directory.
3. Add the skill as a Git submodule in your skills workspace.
4. Vendor the files into an internal skill catalog for your team.
5. Reference the upstream source and recreate the skill in your own agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/makefile-linting-ci-build-pipelines/)
