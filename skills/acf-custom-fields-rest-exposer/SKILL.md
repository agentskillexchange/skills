---
title: "ACF Custom Fields REST Exposer"
description: "Exposes Advanced Custom Fields data through the WordPress REST API using register_rest_field and acf_format_value. Handles repeater fields, flexible content layouts, and gallery fields with proper serialization."
slug: "acf-custom-fields-rest-exposer"
category:
  - "WordPress &amp; CMS"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/acf-custom-fields-rest-exposer/"
listed: true
---

# ACF Custom Fields REST Exposer

Exposes Advanced Custom Fields data through the WordPress REST API using register_rest_field and acf_format_value. Handles repeater fields, flexible content layouts, and gallery fields with proper serialization.

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
clawhub install acf-custom-fields-rest-exposer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill automates the exposure of ACF (Advanced Custom Fields) data through WordPress REST API endpoints. It uses register_rest_field() to attach ACF values to post type responses, with custom get_callback functions that handle complex field types. Repeater fields are serialized as nested arrays with proper subfield mapping using get_field() and have_rows() iterators. Flexible content layouts are exposed with their layout names and subfield data intact. Gallery fields return structured arrays with image IDs, URLs, alt text, and srcset data via wp_get_attachment_image_srcset(). The agent configures field group visibility through acf_add_local_field_group() with proper location rules. Relationship and post object fields resolve to full post objects rather than raw IDs. Group fields are nested properly with their subfield hierarchy. The skill includes schema validation for each field type, caching with wp_cache_set() for expensive field lookups, and permission callbacks to restrict sensitive fields. Supports ACF blocks integration through acf_register_block_type().

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/acf-custom-fields-rest-exposer/)
