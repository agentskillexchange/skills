---
title: "WP-CLI Content Drift Auditor"
slug: "wp-cli-content-drift-auditor"
verification: "security_reviewed"
description: "Audits WordPress content drift by comparing live posts, revisions, and key options using WP-CLI commands like `wp post list`, `wp post meta get`, and `wp option get`. Useful for catching accidental edits, stale templates, and mismatches between REST output and database state before they turn into site-wide regressions."
category:
  - "WordPress &amp; CMS"
framework:
  - "OpenClaw"
source: "https://github.com/wp-cli/wp-cli"
tool_ecosystem:
  github_repo: "wp-cli/wp-cli"
  github_stars: 5048
---

# WP-CLI Content Drift Auditor

Audits WordPress content drift by comparing live posts, revisions, and key options using WP-CLI commands like `wp post list`, `wp post meta get`, and `wp option get`. Useful for catching accidental edits, stale templates, and mismatches between REST output and database state before they turn into site-wide regressions.

## Installation

Choose the setup path that fits your environment:

1. Clone or download this skill into your local skills workspace.
2. Install it with ClawHub if it is available there.
3. Copy the folder into your OpenClaw or AgentSkills directory manually.
4. Add it as a git submodule if you manage skills as pinned dependencies.
5. Vendor it directly into a project repo when you need a fixed internal copy.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-cli-content-drift-auditor/)
