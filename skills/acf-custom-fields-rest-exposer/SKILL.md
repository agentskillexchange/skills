---
name: "ACF Custom Fields REST Exposer"
description: "Exposes Advanced Custom Fields data through the WordPress REST API using register_rest_field and acf_format_value. Handles repeater fields, flexible content layouts, and gallery fields with proper serialization."
category: "WordPress & CMS"
framework: "Cursor"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/acf-custom-fields-rest-exposer/"
tool_ecosystem:
  tool: "wordpress"
  github_stars: 20976
  github_repo: "WordPress/WordPress"
  maintained: true
---

# ACF Custom Fields REST Exposer

Exposes Advanced Custom Fields data through the WordPress REST API using register_rest_field and acf_format_value. Handles repeater fields, flexible content layouts, and gallery fields with proper serialization.

## Overview

This skill automates the exposure of ACF (Advanced Custom Fields) data through WordPress REST API endpoints. It uses register_rest_field() to attach ACF values to post type responses, with custom get_callback functions that handle complex field types. Repeater fields are serialized as nested arrays with proper subfield mapping using get_field() and have_rows() iterators. Flexible content layouts are exposed with their layout names and subfield data intact. Gallery fields return structured arrays with image IDs, URLs, alt text, and srcset data via wp_get_attachment_image_srcset(). The agent configures field group visibility through acf_add_local_field_group() with proper location rules. Relationship and post object fields resolve to full post objects rather than raw IDs. Group fields are nested properly with their subfield hierarchy. The skill includes schema validation for each field type, caching with wp_cache_set() for expensive field lookups, and permission callbacks to restrict sensitive fields. Supports ACF blocks integration through acf_register_block_type().

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill acf-custom-fields-rest-exposer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill acf-custom-fields-rest-exposer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill acf-custom-fields-rest-exposer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill acf-custom-fields-rest-exposer -a codex
```

### OpenClaw

```bash
clawhub install acf-custom-fields-rest-exposer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/acf-custom-fields-rest-exposer/
