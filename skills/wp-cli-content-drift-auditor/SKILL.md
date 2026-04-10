---
title: "WP-CLI Content Drift Auditor"
description: "Audits WordPress content drift by comparing live posts, revisions, and key options using WP-CLI commands like `wp post list`, `wp post meta get`, and `wp option get`. Useful for catching accidental edits, stale templates, and mismatches between REST output and database state before they turn into site-wide regressions."
slug: "wp-cli-content-drift-auditor"
category:
  - "WordPress &amp; CMS"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://github.com/wp-cli/wp-cli"
tool_ecosystem:
  github_repo: "wp-cli/wp-cli"
  github_stars: 5048
---

# WP-CLI Content Drift Auditor

Audits WordPress content drift by comparing live posts, revisions, and key options using WP-CLI commands like `wp post list`, `wp post meta get`, and `wp option get`. Useful for catching accidental edits, stale templates, and mismatches between REST output and database state before they turn into site-wide regressions.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install wp-cli-content-drift-auditor
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

WP-CLI Content Drift Auditor is a practical skill for teams that need to detect silent content changes across a WordPress site without building a full custom dashboard. It leans on WP-CLI primitives such as wp post list, wp post get, wp post meta get, wp option get, and wp db query to compare the current state of posts, pages, custom post types, and key site settings. That makes it useful when a page looks different in production, the excerpt no longer matches the hero copy, or a block template was adjusted by hand and no one recorded it.
The skill also helps reconcile differences between rendered content and what clients see from /wp-json/wp/v2. It can sample post dates, slugs, statuses, excerpts, and modified timestamps, then highlight suspicious drift such as unexpectedly changed metadata, duplicate slugs, or updates that bypassed a normal release process. In editorial environments, that is often faster than digging through wp-admin screens one by one.
Use this skill for incident triage, release validation, and ongoing integrity checks on content-heavy WordPress installs where small CMS edits can have outsized downstream effects.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-cli-content-drift-auditor/)
