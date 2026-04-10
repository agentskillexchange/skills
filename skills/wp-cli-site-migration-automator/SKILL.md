---
name: "WP-CLI Site Migration Automator"
description: "Automates full WordPress site migrations using WP-CLI search-replace, wp db export, and rsync. Handles serialized data, multisite network moves, and DNS preflight checks via dig and curl health probes."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/wp-cli-site-migration-automator/"
category:
  - "WordPress &amp; CMS"
framework:
  - "Codex"
---

# WP-CLI Site Migration Automator

This skill orchestrates complete WordPress site migrations between hosts with zero downtime. It begins with wp db export to create a timestamped SQL dump, then uses rsync with -checksum for efficient file transfer of wp-content directories. The core of the migration uses wp search-replace with -precise and -all-tables flags to handle serialized PHP data in options, postmeta, and widget configurations. For multisite networks, it manages domain mapping via wp site list and wp search-replace -url targeting individual subsites. DNS preflight checks use dig to verify A/AAAA records and curl health probes to confirm the new server responds correctly before cutover. The agent manages wp-config.php updates for database credentials, table prefixes, and environment-specific constants like WP_HOME and WP_SITEURL. Post-migration validation includes wp core verify-checksums, wp plugin list -status=active comparison, and wp cron event list verification. Includes rollback procedures with automated backup restoration.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-cli-site-migration-automator/)
