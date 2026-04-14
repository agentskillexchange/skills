---
title: "WordPress Multisite Network Sync"
description: "Synchronizes plugin settings and theme mods across a WordPress Multisite network using the Network Admin REST endpoints and wp_get_sites() iteration. Propagates sitewide options, user role caps, and widget configurations from a primary site to subsites."
verification: security_reviewed
source: "https://github.com/WordPress/WordPress"
category:
  - "WordPress &amp; CMS"
framework:
  - "Codex"
---

# WordPress Multisite Network Sync

Synchronizes plugin settings and theme mods across a WordPress Multisite network using the Network Admin REST endpoints and wp_get_sites() iteration. Propagates sitewide options, user role caps, and widget configurations from a primary site to subsites.

This skill automates the tedious task of keeping multisite subsites in sync with a primary configuration. It iterates over all active subsites, compares settings for target plugins, and applies updates via switch_to_blog()/update_option() through WP-CLI or direct REST. Supports allowlist/denylist for which options to propagate and dry-run mode for preview. Generates a diff report before applying changes.

Ideal for agency workflows managing 10+ subsites with shared plugin configurations, theme settings, or user role structures. Not for syncing post content between sites — use the WP Replicator pattern for content. Requires Super Admin credentials and WP Multisite configured with subdirectory or subdomain mode.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wordpress-multisite-network-sync/)
