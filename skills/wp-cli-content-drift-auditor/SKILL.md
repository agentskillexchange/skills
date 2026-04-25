---
title: "WP-CLI Content Drift Auditor"
description: "Audits WordPress content drift by comparing live posts, revisions, and key options using WP-CLI commands like `wp post list`, `wp post meta get`, and `wp option get`. Useful for catching accidental edits, stale templates, and mismatches between REST output and database state before they turn into site-wide regressions."
verification: "security_reviewed"
source: "https://github.com/wp-cli/wp-cli"
category:
  - "WordPress & CMS"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "wp-cli/wp-cli"
  github_stars: 5048
---

# WP-CLI Content Drift Auditor

WP-CLI Content Drift Auditor is a practical skill for teams that need to detect silent content changes across a WordPress site without building a full custom dashboard. It leans on WP-CLI primitives such as wp post list, wp post get, wp post meta get, wp option get, and wp db query to compare the current state of posts, pages, custom post types, and key site settings. That makes it useful when a page looks different in production, the excerpt no longer matches the hero copy, or a block template was adjusted by hand and no one recorded it. The skill also helps reconcile differences between rendered content and what clients see from /wp-json/wp/v2. It can sample post dates, slugs, statuses, excerpts, and modified timestamps, then highlight suspicious drift such as unexpectedly changed metadata, duplicate slugs, or updates that bypassed a normal release process. In editorial environments, that is often faster than digging through wp-admin screens one by one. Use this skill for incident triage, release validation, and ongoing integrity checks on content-heavy WordPress installs where small CMS edits can have outsized downstream effects.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/wp-cli-content-drift-auditor/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/wp-cli-content-drift-auditor
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/wp-cli-content-drift-auditor`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-cli-content-drift-auditor/)
