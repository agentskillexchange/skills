---
title: "WP-CLI Site Migration Automator"
description: "This skill orchestrates complete WordPress site migrations between hosts with zero downtime. It begins with wp db export to create a timestamped SQL dump, then uses rsync with &#8211;checksum for efficient file transfer of wp-content directories. The core of the migration uses wp search-replace with &#8211;precise and &#8211;all-tables flags to handle serialized PHP data in options, postmeta, and widget configurations. For multisite networks, it manages domain mapping via wp site list and wp search-replace &#8211;url targeting individual subsites. DNS preflight checks use dig to verify A/AAAA records and curl health probes to confirm the new server responds correctly before cutover. The agent manages wp-config.php updates for database credentials, table prefixes, and environment-specific constants like WP_HOME and WP_SITEURL. Post-migration validation includes wp core verify-checksums, wp plugin list &#8211;status=active comparison, and wp cron event list verification. Includes rollback procedures with automated backup restoration."
source: "https://agentskillexchange.com/skills/wp-cli-site-migration-automator/"
verification: "security_reviewed"
category:
  - "WordPress &amp; CMS"
framework:
  - "Codex"
---

# WP-CLI Site Migration Automator

This skill orchestrates complete WordPress site migrations between hosts with zero downtime. It begins with wp db export to create a timestamped SQL dump, then uses rsync with &#8211;checksum for efficient file transfer of wp-content directories. The core of the migration uses wp search-replace with &#8211;precise and &#8211;all-tables flags to handle serialized PHP data in options, postmeta, and widget configurations. For multisite networks, it manages domain mapping via wp site list and wp search-replace &#8211;url targeting individual subsites. DNS preflight checks use dig to verify A/AAAA records and curl health probes to confirm the new server responds correctly before cutover. The agent manages wp-config.php updates for database credentials, table prefixes, and environment-specific constants like WP_HOME and WP_SITEURL. Post-migration validation includes wp core verify-checksums, wp plugin list &#8211;status=active comparison, and wp cron event list verification. Includes rollback procedures with automated backup restoration.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-cli-site-migration-automator/)
