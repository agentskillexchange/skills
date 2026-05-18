---
name: "Run policy-driven Borg backups, checks, and restores from one config with borgmatic"
slug: "run-policy-driven-borg-backups-checks-and-restores-from-one-config-with-borgmatic"
description: "Use borgmatic to drive Borg backup, prune, check, and restore routines from a single declarative config so an agent can supervise backup runbooks instead of stitching raw commands by hand."
github_stars: 2200
verification: "security_reviewed"
source: "https://github.com/borgmatic-collective/borgmatic"
author: "Borgmatic Collective"
publisher_type: "open_source_project"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "borgmatic-collective/borgmatic"
  github_stars: 2200
---

# Run policy-driven Borg backups, checks, and restores from one config with borgmatic

Use borgmatic to drive Borg backup, prune, check, and restore routines from a single declarative config so an agent can supervise backup runbooks instead of stitching raw commands by hand.

## Prerequisites

borgmatic, Borg Backup

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install borgmatic from the supported package or Python distribution path in the borgmatic docs, then configure `borgmatic.yaml` and run borgmatic create, check, prune, or restore workflows from that config.
```

## Documentation

- https://torsion.org/borgmatic/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-policy-driven-borg-backups-checks-and-restores-from-one-config-with-borgmatic/)
