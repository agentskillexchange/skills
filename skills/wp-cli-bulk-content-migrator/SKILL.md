---
title: "WP-CLI Bulk Content Migrator"
description: "Automates large-scale WordPress content migrations using WP-CLI wp post create and wp term set commands. Handles custom post types, ACF field mapping, and taxonomy reassignment with rollback support."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/wp-cli-bulk-content-migrator/"
category:
  - "WordPress &amp; CMS"
framework:
  - "OpenClaw"
---

# WP-CLI Bulk Content Migrator

This skill automates complex WordPress content migrations using WP-CLI commands for reliable server-side execution. It handles bulk post creation via wp post create with support for custom post types, post meta, and featured images. Taxonomy assignment uses wp term set for categories, tags, and custom taxonomies.

Advanced Custom Fields (ACF) data is mapped using wp post meta update with proper field key references, supporting repeater fields, flexible content layouts, and relationship fields. The skill handles media library imports via wp media import with automatic attachment to posts and alt text assignment.

A transaction-like rollback system tracks all created/modified content IDs, allowing complete reversal if migration validation fails. Progress tracking provides real-time counts and ETA for large migrations (10k+ posts). The skill also handles URL rewriting in content bodies using wp search-replace for domain changes.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-cli-bulk-content-migrator/)
