---
title: "WP-CLI Site Migration Automator"
description: "Automates full WordPress site migrations using WP-CLI search-replace, wp db export, and rsync. Handles serialized data, multisite network moves, and DNS preflight checks via dig and curl health probes."
slug: "wp-cli-site-migration-automator"
category:
  - "WordPress &amp; CMS"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/wp-cli-site-migration-automator/"
---

# WP-CLI Site Migration Automator

Automates full WordPress site migrations using WP-CLI search-replace, wp db export, and rsync. Handles serialized data, multisite network moves, and DNS preflight checks via dig and curl health probes.

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
clawhub install wp-cli-site-migration-automator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill orchestrates complete WordPress site migrations between hosts with zero downtime. It begins with wp db export to create a timestamped SQL dump, then uses rsync with –checksum for efficient file transfer of wp-content directories. The core of the migration uses wp search-replace with –precise and –all-tables flags to handle serialized PHP data in options, postmeta, and widget configurations. For multisite networks, it manages domain mapping via wp site list and wp search-replace –url targeting individual subsites. DNS preflight checks use dig to verify A/AAAA records and curl health probes to confirm the new server responds correctly before cutover. The agent manages wp-config.php updates for database credentials, table prefixes, and environment-specific constants like WP_HOME and WP_SITEURL. Post-migration validation includes wp core verify-checksums, wp plugin list –status=active comparison, and wp cron event list verification. Includes rollback procedures with automated backup restoration.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-cli-site-migration-automator/)
