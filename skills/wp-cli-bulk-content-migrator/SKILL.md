---
title: "WP-CLI Bulk Content Migrator"
description: "Automates large-scale WordPress content migrations using WP-CLI wp post create and wp term set commands. Handles custom post types, ACF field mapping, and taxonomy reassignment with rollback support."
slug: "wp-cli-bulk-content-migrator"
category:
  - "WordPress &amp; CMS"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/wp-cli-bulk-content-migrator/"
---

# WP-CLI Bulk Content Migrator

Automates large-scale WordPress content migrations using WP-CLI wp post create and wp term set commands. Handles custom post types, ACF field mapping, and taxonomy reassignment with rollback support.

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
clawhub install wp-cli-bulk-content-migrator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill automates complex WordPress content migrations using WP-CLI commands for reliable server-side execution. It handles bulk post creation via wp post create with support for custom post types, post meta, and featured images. Taxonomy assignment uses wp term set for categories, tags, and custom taxonomies.
Advanced Custom Fields (ACF) data is mapped using wp post meta update with proper field key references, supporting repeater fields, flexible content layouts, and relationship fields. The skill handles media library imports via wp media import with automatic attachment to posts and alt text assignment.
A transaction-like rollback system tracks all created/modified content IDs, allowing complete reversal if migration validation fails. Progress tracking provides real-time counts and ETA for large migrations (10k+ posts). The skill also handles URL rewriting in content bodies using wp search-replace for domain changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-cli-bulk-content-migrator/)
