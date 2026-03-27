---
name: "WP-CLI Bulk Content Migrator"
description: "Automates large-scale WordPress content migrations using WP-CLI wp post create and wp term set commands. Handles custom post types, ACF field mapping, and taxonomy reassignment with rollback support."
category: "WordPress & CMS"
framework: "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/wp-cli-bulk-content-migrator/"
tool_ecosystem:
  tool: wordpress
  github_stars: 20976
  github_repo: WordPress/WordPress
  maintained: true
---

# WP-CLI Bulk Content Migrator

Automates large-scale WordPress content migrations using WP-CLI wp post create and wp term set commands. Handles custom post types, ACF field mapping, and taxonomy reassignment with rollback support.

## Overview

This skill automates complex WordPress content migrations using WP-CLI commands for reliable server-side execution. It handles bulk post creation via wp post create with support for custom post types, post meta, and featured images. Taxonomy assignment uses wp term set for categories, tags, and custom taxonomies.

Advanced Custom Fields (ACF) data is mapped using wp post meta update with proper field key references, supporting repeater fields, flexible content layouts, and relationship fields. The skill handles media library imports via wp media import with automatic attachment to posts and alt text assignment.

A transaction-like rollback system tracks all created/modified content IDs, allowing complete reversal if migration validation fails. Progress tracking provides real-time counts and ETA for large migrations (10k+ posts). The skill also handles URL rewriting in content bodies using wp search-replace for domain changes.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill wp-cli-bulk-content-migrator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill wp-cli-bulk-content-migrator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill wp-cli-bulk-content-migrator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill wp-cli-bulk-content-migrator -a codex
```

### OpenClaw

```bash
clawhub install wp-cli-bulk-content-migrator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/wp-cli-bulk-content-migrator/
