---
title: "WP-CLI Bulk Content Migrator"
description: "Automates large-scale WordPress content migrations using WP-CLI wp post create and wp term set commands. Handles custom post types, ACF field mapping, and taxonomy reassignment with rollback support."
verification: "security_reviewed"
source: "https://github.com/wp-cli/wp-cli"
category:
  - "WordPress & CMS"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "wp-cli/wp-cli"
  github_stars: 5061
---

# WP-CLI Bulk Content Migrator

This skill automates complex WordPress content migrations using WP-CLI commands for reliable server-side execution. It handles bulk post creation via wp post create with support for custom post types, post meta, and featured images. Taxonomy assignment uses wp term set for categories, tags, and custom taxonomies. Advanced Custom Fields (ACF) data is mapped using wp post meta update with proper field key references, supporting repeater fields, flexible content layouts, and relationship fields. The skill handles media library imports via wp media import with automatic attachment to posts and alt text assignment. A transaction-like rollback system tracks all created/modified content IDs, allowing complete reversal if migration validation fails. Progress tracking provides real-time counts and ETA for large migrations (10k+ posts). The skill also handles URL rewriting in content bodies using wp search-replace for domain changes.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/wp-cli-bulk-content-migrator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/wp-cli-bulk-content-migrator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/wp-cli-bulk-content-migrator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-cli-bulk-content-migrator/)
