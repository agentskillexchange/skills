---
title: WP-CLI Site Migration Automator
description: This skill orchestrates complete WordPress site migrations between hosts
  with zero downtime. It begins with wp db export to create a timestamped SQL dump,
  then uses rsync with –checksum for efficient file transfer of wp-content directories.
  The core of the migration uses wp search-replace with –precise and –all-tables flags
  to handle serialized PHP data in options, postmeta, and widget configurations. For
  multisite networks, it manages domain mapping via wp site list and wp search-replace
  –url targeting individual subsites. DNS preflight checks use dig to verify A/AAAA
  records and curl health probes to confirm the new server responds correctly before
  cutover. The agent manages wp-config.php updates for database credentials, table
  prefixes, and environment-specific constants like WP_HOME and WP_SITEURL. Post-migration
  validation includes wp core verify-checksums, wp plugin list –status=active comparison,
  and wp cron event list verification. Includes rollback procedures with automated
  backup restoration.
verification: security_reviewed
source: https://agentskillexchange.com/skills/wp-cli-site-migration-automator/
category:
- WordPress &amp; CMS
framework:
- Codex
---

# WP-CLI Site Migration Automator

This skill orchestrates complete WordPress site migrations between hosts with zero downtime. It begins with wp db export to create a timestamped SQL dump, then uses rsync with –checksum for efficient file transfer of wp-content directories. The core of the migration uses wp search-replace with –precise and –all-tables flags to handle serialized PHP data in options, postmeta, and widget configurations. For multisite networks, it manages domain mapping via wp site list and wp search-replace –url targeting individual subsites. DNS preflight checks use dig to verify A/AAAA records and curl health probes to confirm the new server responds correctly before cutover. The agent manages wp-config.php updates for database credentials, table prefixes, and environment-specific constants like WP_HOME and WP_SITEURL. Post-migration validation includes wp core verify-checksums, wp plugin list –status=active comparison, and wp cron event list verification. Includes rollback procedures with automated backup restoration.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-cli-site-migration-automator/)
