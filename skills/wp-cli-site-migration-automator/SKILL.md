---
name: "WP-CLI Site Migration Automator"
description: "Automates full WordPress site migrations using WP-CLI search-replace, wp db export, and rsync. Handles serialized data, multisite network moves, and DNS preflight checks via dig and curl health probes."
category: "WordPress & CMS"
framework: "Codex"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/wp-cli-site-migration-automator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "wordpress"  # from ase_tool_match
  github_stars: 20976  # from ase_github_stars (integer, not string)
  github_repo: "WordPress/WordPress"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# WP-CLI Site Migration Automator

Automates full WordPress site migrations using WP-CLI search-replace, wp db export, and rsync. Handles serialized data, multisite network moves, and DNS preflight checks via dig and curl health probes.

## Overview

This skill orchestrates complete WordPress site migrations between hosts with zero downtime. It begins with wp db export to create a timestamped SQL dump, then uses rsync with –checksum for efficient file transfer of wp-content directories. The core of the migration uses wp search-replace with –precise and –all-tables flags to handle serialized PHP data in options, postmeta, and widget configurations. For multisite networks, it manages domain mapping via wp site list and wp search-replace –url targeting individual subsites. DNS preflight checks use dig to verify A/AAAA records and curl health probes to confirm the new server responds correctly before cutover. The agent manages wp-config.php updates for database credentials, table prefixes, and environment-specific constants like WP_HOME and WP_SITEURL. Post-migration validation includes wp core verify-checksums, wp plugin list –status=active comparison, and wp cron event list verification. Includes rollback procedures with automated backup restoration.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill wp-cli-site-migration-automator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill wp-cli-site-migration-automator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill wp-cli-site-migration-automator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill wp-cli-site-migration-automator -a codex
```

### OpenClaw

```bash
clawhub install wp-cli-site-migration-automator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/wp-cli-site-migration-automator/
