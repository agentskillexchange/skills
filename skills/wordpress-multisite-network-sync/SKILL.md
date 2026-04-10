---
name: WordPress Multisite Network Sync
description: Synchronizes plugin settings and theme mods across a WordPress Multisite
  network using the Network Admin REST endpoints and wp_get_sites() iteration. Propagates
  sitewide options, user role caps, and widget configurations from a primary site
  to subsites.
verification: security_reviewed
source: https://agentskillexchange.com/skills/wordpress-multisite-network-sync/
category:
- WordPress &amp; CMS
framework:
- Codex
---
# WordPress Multisite Network Sync

Synchronizes plugin settings and theme mods across a WordPress Multisite network using the Network Admin REST endpoints and wp_get_sites() iteration. Propagates sitewide options, user role caps, and widget configurations from a primary site to subsites.
This skill automates the tedious task of keeping multisite subsites in sync with a primary configuration. It iterates over all active subsites, compares settings for target plugins, and applies updates via switch_to_blog()/update_option() through WP-CLI or direct REST. Supports allowlist/denylist for which options to propagate and dry-run mode for preview. Generates a diff report before applying changes.
Ideal for agency workflows managing 10+ subsites with shared plugin configurations, theme settings, or user role structures. Not for syncing post content between sites — use the WP Replicator pattern for content. Requires Super Admin credentials and WP Multisite configured with subdirectory or subdomain mode.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wordpress-multisite-network-sync/)
