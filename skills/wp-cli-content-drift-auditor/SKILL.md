---
title: "WP-CLI Content Drift Auditor"
description: "Audits WordPress content drift by comparing live posts, revisions, and key options using WP-CLI commands like `wp post list`, `wp post meta get`, and `wp option get`. Useful for catching accidental edits, stale templates, and mismatches between REST output and database state before they turn into site-wide regressions."
verification: security_reviewed
source: "https://github.com/wp-cli/wp-cli"
tool_ecosystem:
  github_repo: "wp-cli/wp-cli"
  github_stars: 5048
---

# WP-CLI Content Drift Auditor

Audits WordPress content drift by comparing live posts, revisions, and key options using WP-CLI commands like `wp post list`, `wp post meta get`, and `wp option get`. Useful for catching accidental edits, stale templates, and mismatches between REST output and database state before they turn into site-wide regressions.

## Installation

Choose the path that fits your setup:

1. Clone this repository and use the skill locally.
2. Copy the skill folder into your local skills directory.
3. Add the skill as a Git submodule in your skills workspace.
4. Vendor the files into an internal skill catalog for your team.
5. Reference the upstream source and recreate the skill in your own agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-cli-content-drift-auditor/)
