---
title: "WordPress Multisite Network Sync"
description: "Synchronizes plugin settings and theme mods across a WordPress Multisite network using the Network Admin REST endpoints and wp_get_sites() iteration. Propagates sitewide options, user role caps, and widget configurations from a primary site to subsites."
verification: security_reviewed
source: "https://github.com/WordPress/WordPress"
category:
  - "WordPress & CMS"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "wordpress/wordpress"
  github_stars: 21027
---

# WordPress Multisite Network Sync

Synchronizes plugin settings and theme mods across a WordPress Multisite network using the Network Admin REST endpoints and wp_get_sites() iteration. Propagates sitewide options, user role caps, and widget configurations from a primary site to subsites.

This skill automates the tedious task of keeping multisite subsites in sync with a primary configuration. It iterates over all active subsites, compares settings for target plugins, and applies updates via switch_to_blog()/update_option() through WP-CLI or direct REST. Supports allowlist/denylist for which options to propagate and dry-run mode for preview. Generates a diff report before applying changes.

Ideal for agency workflows managing 10+ subsites with shared plugin configurations, theme settings, or user role structures. Not for syncing post content between sites — use the WP Replicator pattern for content. Requires Super Admin credentials and WP Multisite configured with subdirectory or subdomain mode.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/wordpress-multisite-network-sync
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/wordpress-multisite-network-sync` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wordpress-multisite-network-sync/)
