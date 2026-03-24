---
name: "WP Multisite Network Sync Agent"
description: "Synchronizes content, users, and plugin configurations across WordPress Multisite networks using the WP_Site_Query API and switch_to_blog(). Automates bulk site provisioning via wp_insert_site() with REST endpoint monitoring."
category: "WordPress & CMS"
framework: "OpenClaw"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/wp-multisite-network-sync-agent/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "wordpress"  # from ase_tool_match
  github_stars: 20973  # from ase_github_stars (integer, not string)
  github_repo: "WordPress/WordPress"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# WP Multisite Network Sync Agent

Synchronizes content, users, and plugin configurations across WordPress Multisite networks using the WP_Site_Query API and switch_to_blog(). Automates bulk site provisioning via wp_insert_site() with REST endpoint monitoring.

## Overview

The WP Multisite Network Sync Agent provides comprehensive automation for managing large WordPress Multisite installations. It leverages the WP_Site_Query class to enumerate all network sites and uses switch_to_blog() for cross-site content operations. The agent monitors REST API endpoints across all subsites using wp_remote_get() with parallel requests, detecting configuration drift and plugin version mismatches. It automates new site provisioning through wp_insert_site() with custom blog templates, applying predefined theme settings and plugin activations via activate_plugin(). The synchronization engine handles user role mapping across sites using add_user_to_blog() and supports scheduled sync operations through WP-Cron with wp_schedule_event(). Database operations use $wpdb->get_blog_prefix() for safe cross-site queries. Includes rollback capabilities using WordPress transients for state tracking and WP_Filesystem for safe file operations during theme and plugin sync.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill wp-multisite-network-sync-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill wp-multisite-network-sync-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill wp-multisite-network-sync-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill wp-multisite-network-sync-agent -a codex
```

### OpenClaw

```bash
clawhub install wp-multisite-network-sync-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/wp-multisite-network-sync-agent/
