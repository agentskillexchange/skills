---
title: WP-CLI Bulk Content Migrator
description: This skill automates complex WordPress content migrations using WP-CLI
  commands for reliable server-side execution. It handles bulk post creation via wp
  post create with support for custom post types, post meta, and featured images.
  Taxonomy assignment uses wp term set for categories, tags, and custom taxonomies.
  Advanced Custom Fields (ACF) data is mapped using wp post meta update with proper
  field key references, supporting repeater fields, flexible content layouts, and
  relationship fields. The skill handles media library imports via wp media import
  with automatic attachment to posts and alt text assignment. A transaction-like rollback
  system tracks all created/modified content IDs, allowing complete reversal if migration
  validation fails. Progress tracking provides real-time counts and ETA for large
  migrations (10k+ posts). The skill also handles URL rewriting in content bodies
  using wp search-replace for domain changes.
verification: security_reviewed
source: https://agentskillexchange.com/skills/wp-cli-bulk-content-migrator/
category:
- WordPress &amp; CMS
framework:
- OpenClaw
---

# WP-CLI Bulk Content Migrator

This skill automates complex WordPress content migrations using WP-CLI commands for reliable server-side execution. It handles bulk post creation via wp post create with support for custom post types, post meta, and featured images. Taxonomy assignment uses wp term set for categories, tags, and custom taxonomies. Advanced Custom Fields (ACF) data is mapped using wp post meta update with proper field key references, supporting repeater fields, flexible content layouts, and relationship fields. The skill handles media library imports via wp media import with automatic attachment to posts and alt text assignment. A transaction-like rollback system tracks all created/modified content IDs, allowing complete reversal if migration validation fails. Progress tracking provides real-time counts and ETA for large migrations (10k+ posts). The skill also handles URL rewriting in content bodies using wp search-replace for domain changes.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-cli-bulk-content-migrator/)
