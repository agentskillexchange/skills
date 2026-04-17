---
title: "WordPress REST API Content Sync"
description: "This skill enables bidirectional content synchronization between WordPress installations using the WP REST API. It fetches posts, pages, and custom post types via /wp/v2/{type} endpoints with pagination handling through the X-WP-TotalPages header and supports both OAuth 1.0a and Application Password authentication methods.\nMedia synchronization handles image and file sideloading via the /wp/v2/media endpoint, preserving alt text, captions, and attachment metadata. The skill transforms shortcodes between installations that use different plugins (e.g., converting Elementor shortcodes to Gutenberg blocks). Content diff detection uses post modified dates and content hashing to avoid unnecessary updates.\nConflict resolution supports last-write-wins, source-priority, and manual review modes. A sync log tracks all operations with rollback capability. The skill handles taxonomy mapping between sites with different category/tag structures and supports custom field synchronization for ACF and meta box data."
verification: security_reviewed
source: "https://github.com/WordPress/WordPress"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "wordpress/wordpress"
  github_stars: 21027
---

# WordPress REST API Content Sync

This skill enables bidirectional content synchronization between WordPress installations using the WP REST API. It fetches posts, pages, and custom post types via /wp/v2/{type} endpoints with pagination handling through the X-WP-TotalPages header and supports both OAuth 1.0a and Application Password authentication methods.
Media synchronization handles image and file sideloading via the /wp/v2/media endpoint, preserving alt text, captions, and attachment metadata. The skill transforms shortcodes between installations that use different plugins (e.g., converting Elementor shortcodes to Gutenberg blocks). Content diff detection uses post modified dates and content hashing to avoid unnecessary updates.
Conflict resolution supports last-write-wins, source-priority, and manual review modes. A sync log tracks all operations with rollback capability. The skill handles taxonomy mapping between sites with different category/tag structures and supports custom field synchronization for ACF and meta box data.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/wordpress-rest-api-content-sync
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/wordpress-rest-api-content-sync` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wordpress-rest-api-content-sync/)
