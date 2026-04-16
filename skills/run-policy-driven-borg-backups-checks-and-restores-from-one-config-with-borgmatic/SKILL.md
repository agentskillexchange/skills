---
title: "Run policy-driven Borg backups, checks, and restores from one config with borgmatic"
description: "Use borgmatic to drive Borg backup, prune, check, and restore routines from a single declarative config so an agent can supervise backup runbooks instead of stitching raw commands by hand."
verification: "listed"
source: "https://github.com/borgmatic-collective/borgmatic"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "borgmatic-collective/borgmatic"
  github_stars: 2200
---

# Run policy-driven Borg backups, checks, and restores from one config with borgmatic

Use borgmatic when an agent needs to execute a repeatable backup runbook around Borg, including create, prune, consistency checks, hooks, and restore-oriented validation from one configuration. Invoke this instead of using Borg directly when the real task is policy-driven backup orchestration and health checking, not manual archive commands one by one. The scope boundary is clear and skill-shaped: borgmatic is a declarative backup and restore operations layer for Borg workflows, not just a generic backup product card or a broad infrastructure platform listing.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-policy-driven-borg-backups-checks-and-restores-from-one-config-with-borgmatic/)
