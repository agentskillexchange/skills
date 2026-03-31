---
name: "WordPress Multisite Network Sync"
description: "Synchronizes plugin settings and theme mods across a WordPress Multisite network using the Network Admin REST endpoints and wp_get_sites() iteration. Propagates sitewide options, user role caps, and widget configurations from a primary site to subsites."
category: "WordPress &amp; CMS"
framework: "Codex"
verification: security_reviewed
source: "https://github.com/wordpress/wordpress"
tool_ecosystem:
  tool: wordpress
  github_repo: wordpress/wordpress
  github_stars: 20985
  maintained: true
---
# WordPress Multisite Network Sync

Synchronizes plugin settings and theme mods across a WordPress Multisite network using the Network Admin REST endpoints and wp_get_sites() iteration. Propagates sitewide options, user role caps, and widget configurations from a primary site to subsites.

## Overview

Synchronizes plugin settings and theme mods across a WordPress Multisite network using the Network Admin REST endpoints and wp_get_sites() iteration. Propagates sitewide options, user role caps, and widget configurations from a primary site to subsites.

This skill automates the tedious task of keeping multisite subsites in sync with a primary configuration. It iterates over all active subsites, compares settings for target plugins, and applies updates via switch_to_blog()/update_option() through WP-CLI or direct REST. Supports allowlist/denylist for which options to propagate and dry-run mode for preview. Generates a diff report before applying changes.

Ideal for agency workflows managing 10+ subsites with shared plugin configurations, theme settings, or user role structures. Not for syncing post content between sites — use the WP Replicator pattern for content. Requires Super Admin credentials and WP Multisite configured with subdirectory or subdomain mode.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill wordpress-multisite-network-sync
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill wordpress-multisite-network-sync -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill wordpress-multisite-network-sync -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill wordpress-multisite-network-sync -a codex
```

### OpenClaw

```bash
clawhub install wordpress-multisite-network-sync
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wordpress-multisite-network-sync/)
