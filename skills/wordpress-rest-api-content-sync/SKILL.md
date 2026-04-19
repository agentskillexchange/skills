---
title: "WordPress REST API Content Sync"
description: "This skill enables bidirectional content synchronization between WordPress installations using the WP REST API. It fetches posts, pages, and custom post types via /wp/v2/{type} endpoints with pagination handling through the X-WP-TotalPages header and supports both OAuth 1.0a and Application Password authentication methods. Media synchronization handles image and file sideloading via the /wp/v2/media endpoint, preserving alt text, captions, and attachment metadata. The skill transforms shortcodes between installations that use different plugins (e.g., converting Elementor shortcodes to Gutenberg blocks). Content diff detection uses post modified dates and content hashing to avoid unnecessary updates. Conflict resolution supports last-write-wins, source-priority, and manual review modes. A sync log tracks all operations with rollback capability. The skill handles taxonomy mapping between sites with different category/tag structures and supports custom field synchronization for ACF and meta box data."
source: "https://github.com/WordPress/WordPress"
verification: "security_reviewed"
category:
  - "WordPress &amp; CMS"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "wordpress/wordpress"
  github_stars: 21027
---

# WordPress REST API Content Sync

This skill enables bidirectional content synchronization between WordPress installations using the WP REST API. It fetches posts, pages, and custom post types via /wp/v2/{type} endpoints with pagination handling through the X-WP-TotalPages header and supports both OAuth 1.0a and Application Password authentication methods. Media synchronization handles image and file sideloading via the /wp/v2/media endpoint, preserving alt text, captions, and attachment metadata. The skill transforms shortcodes between installations that use different plugins (e.g., converting Elementor shortcodes to Gutenberg blocks). Content diff detection uses post modified dates and content hashing to avoid unnecessary updates. Conflict resolution supports last-write-wins, source-priority, and manual review modes. A sync log tracks all operations with rollback capability. The skill handles taxonomy mapping between sites with different category/tag structures and supports custom field synchronization for ACF and meta box data.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wordpress-rest-api-content-sync/)
