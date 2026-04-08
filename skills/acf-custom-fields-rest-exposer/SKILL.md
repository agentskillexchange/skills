---
title: ACF Custom Fields REST Exposer
description: This skill automates the exposure of ACF (Advanced Custom Fields) data
  through WordPress REST API endpoints. It uses register_rest_field() to attach ACF
  values to post type responses, with custom get_callback functions that handle complex
  field types. Repeater fields are serialized as nested arrays with proper subfield
  mapping using get_field() and have_rows() iterators. Flexible content layouts are
  exposed with their layout names and subfield data intact. Gallery fields return
  structured arrays with image IDs, URLs, alt text, and srcset data via wp_get_attachment_image_srcset().
  The agent configures field group visibility through acf_add_local_field_group()
  with proper location rules. Relationship and post object fields resolve to full
  post objects rather than raw IDs. Group fields are nested properly with their subfield
  hierarchy. The skill includes schema validation for each field type, caching with
  wp_cache_set() for expensive field lookups, and permission callbacks to restrict
  sensitive fields. Supports ACF blocks integration through acf_register_block_type().
verification: security_reviewed
source: https://agentskillexchange.com/skills/acf-custom-fields-rest-exposer/
category:
- WordPress &amp; CMS
framework:
- Cursor
---

# ACF Custom Fields REST Exposer

This skill automates the exposure of ACF (Advanced Custom Fields) data through WordPress REST API endpoints. It uses register_rest_field() to attach ACF values to post type responses, with custom get_callback functions that handle complex field types. Repeater fields are serialized as nested arrays with proper subfield mapping using get_field() and have_rows() iterators. Flexible content layouts are exposed with their layout names and subfield data intact. Gallery fields return structured arrays with image IDs, URLs, alt text, and srcset data via wp_get_attachment_image_srcset(). The agent configures field group visibility through acf_add_local_field_group() with proper location rules. Relationship and post object fields resolve to full post objects rather than raw IDs. Group fields are nested properly with their subfield hierarchy. The skill includes schema validation for each field type, caching with wp_cache_set() for expensive field lookups, and permission callbacks to restrict sensitive fields. Supports ACF blocks integration through acf_register_block_type().

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/acf-custom-fields-rest-exposer/)
