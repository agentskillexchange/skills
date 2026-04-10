---
title: "WordPress REST API Content Sync"
description: "Synchronizes content between WordPress multisite installations using the WP REST API /wp/v2/posts endpoint with OAuth 1.0a authentication. Handles media sideloading, shortcode transformation, and conflict resolution."
slug: "wordpress-rest-api-content-sync"
category:
  - "WordPress &amp; CMS"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/wordpress-rest-api-content-sync/"
---

# WordPress REST API Content Sync

Synchronizes content between WordPress multisite installations using the WP REST API /wp/v2/posts endpoint with OAuth 1.0a authentication. Handles media sideloading, shortcode transformation, and conflict resolution.

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
clawhub install wordpress-rest-api-content-sync
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill enables bidirectional content synchronization between WordPress installations using the WP REST API. It fetches posts, pages, and custom post types via /wp/v2/{type} endpoints with pagination handling through the X-WP-TotalPages header and supports both OAuth 1.0a and Application Password authentication methods.
Media synchronization handles image and file sideloading via the /wp/v2/media endpoint, preserving alt text, captions, and attachment metadata. The skill transforms shortcodes between installations that use different plugins (e.g., converting Elementor shortcodes to Gutenberg blocks). Content diff detection uses post modified dates and content hashing to avoid unnecessary updates.
Conflict resolution supports last-write-wins, source-priority, and manual review modes. A sync log tracks all operations with rollback capability. The skill handles taxonomy mapping between sites with different category/tag structures and supports custom field synchronization for ACF and meta box data.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wordpress-rest-api-content-sync/)
