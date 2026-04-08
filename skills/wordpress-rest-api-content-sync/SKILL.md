---
title: WordPress REST API Content Sync
description: This skill enables bidirectional content synchronization between WordPress
  installations using the WP REST API. It fetches posts, pages, and custom post types
  via /wp/v2/{type} endpoints with pagination handling through the X-WP-TotalPages
  header and supports both OAuth 1.0a and Application Password authentication methods.
  Media synchronization handles image and file sideloading via the /wp/v2/media endpoint,
  preserving alt text, captions, and attachment metadata. The skill transforms shortcodes
  between installations that use different plugins (e.g., converting Elementor shortcodes
  to Gutenberg blocks). Content diff detection uses post modified dates and content
  hashing to avoid unnecessary updates. Conflict resolution supports last-write-wins,
  source-priority, and manual review modes. A sync log tracks all operations with
  rollback capability. The skill handles taxonomy mapping between sites with different
  category/tag structures and supports custom field synchronization for ACF and meta
  box data.
verification: security_reviewed
source: https://agentskillexchange.com/skills/wordpress-rest-api-content-sync/
category:
- WordPress &amp; CMS
framework:
- MCP
---

# WordPress REST API Content Sync

This skill enables bidirectional content synchronization between WordPress installations using the WP REST API. It fetches posts, pages, and custom post types via /wp/v2/{type} endpoints with pagination handling through the X-WP-TotalPages header and supports both OAuth 1.0a and Application Password authentication methods. Media synchronization handles image and file sideloading via the /wp/v2/media endpoint, preserving alt text, captions, and attachment metadata. The skill transforms shortcodes between installations that use different plugins (e.g., converting Elementor shortcodes to Gutenberg blocks). Content diff detection uses post modified dates and content hashing to avoid unnecessary updates. Conflict resolution supports last-write-wins, source-priority, and manual review modes. A sync log tracks all operations with rollback capability. The skill handles taxonomy mapping between sites with different category/tag structures and supports custom field synchronization for ACF and meta box data.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wordpress-rest-api-content-sync/)
