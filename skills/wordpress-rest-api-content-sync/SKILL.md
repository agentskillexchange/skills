---
name: "WordPress REST API Content Sync"
description: "Synchronizes content between WordPress multisite installations using the WP REST API /wp/v2/posts endpoint with OAuth 1.0a authentication. Handles media sideloading, shortcode transformation, and conflict resolution."
category: "WordPress & CMS"
framework: "MCP"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/wordpress-rest-api-content-sync/"
tool_ecosystem:
  tool: wordpress
  github_stars: 20976
  github_repo: WordPress/WordPress
  maintained: true
---

# WordPress REST API Content Sync

Synchronizes content between WordPress multisite installations using the WP REST API /wp/v2/posts endpoint with OAuth 1.0a authentication. Handles media sideloading, shortcode transformation, and conflict resolution.

## Overview

This skill enables bidirectional content synchronization between WordPress installations using the WP REST API. It fetches posts, pages, and custom post types via /wp/v2/{type} endpoints with pagination handling through the X-WP-TotalPages header and supports both OAuth 1.0a and Application Password authentication methods.

Media synchronization handles image and file sideloading via the /wp/v2/media endpoint, preserving alt text, captions, and attachment metadata. The skill transforms shortcodes between installations that use different plugins (e.g., converting Elementor shortcodes to Gutenberg blocks). Content diff detection uses post modified dates and content hashing to avoid unnecessary updates.

Conflict resolution supports last-write-wins, source-priority, and manual review modes. A sync log tracks all operations with rollback capability. The skill handles taxonomy mapping between sites with different category/tag structures and supports custom field synchronization for ACF and meta box data.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill wordpress-rest-api-content-sync
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill wordpress-rest-api-content-sync -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill wordpress-rest-api-content-sync -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill wordpress-rest-api-content-sync -a codex
```

### OpenClaw

```bash
clawhub install wordpress-rest-api-content-sync
```

## Source

- Marketplace: https://agentskillexchange.com/skills/wordpress-rest-api-content-sync/
