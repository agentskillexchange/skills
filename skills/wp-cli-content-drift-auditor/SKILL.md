---
title: "WP-CLI Content Drift Auditor"
description: "WP-CLI Content Drift Auditor is a practical skill for teams that need to detect silent content changes across a WordPress site without building a full custom dashboard. It leans on WP-CLI primitives such as wp post list , wp post get , wp post meta get , wp option get , and wp db query to compare the current state of posts, pages, custom post types, and key site settings. That makes it useful when a page looks different in production, the excerpt no longer matches the hero copy, or a block template was adjusted by hand and no one recorded it. The skill also helps reconcile differences between rendered content and what clients see from /wp-json/wp/v2 . It can sample post dates, slugs, statuses, excerpts, and modified timestamps, then highlight suspicious drift such as unexpectedly changed metadata, duplicate slugs, or updates that bypassed a normal release process. In editorial environments, that is often faster than digging through wp-admin screens one by one. Use this skill for incident triage, release validation, and ongoing integrity checks on content-heavy WordPress installs where small CMS edits can have outsized downstream effects."
source: "https://github.com/wp-cli/wp-cli"
verification: "security_reviewed"
category:
  - "WordPress &amp; CMS"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "wp-cli/wp-cli"
  github_stars: 5048
---

# WP-CLI Content Drift Auditor

WP-CLI Content Drift Auditor is a practical skill for teams that need to detect silent content changes across a WordPress site without building a full custom dashboard. It leans on WP-CLI primitives such as wp post list , wp post get , wp post meta get , wp option get , and wp db query to compare the current state of posts, pages, custom post types, and key site settings. That makes it useful when a page looks different in production, the excerpt no longer matches the hero copy, or a block template was adjusted by hand and no one recorded it. The skill also helps reconcile differences between rendered content and what clients see from /wp-json/wp/v2 . It can sample post dates, slugs, statuses, excerpts, and modified timestamps, then highlight suspicious drift such as unexpectedly changed metadata, duplicate slugs, or updates that bypassed a normal release process. In editorial environments, that is often faster than digging through wp-admin screens one by one. Use this skill for incident triage, release validation, and ongoing integrity checks on content-heavy WordPress installs where small CMS edits can have outsized downstream effects.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-cli-content-drift-auditor/)
