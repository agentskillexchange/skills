---
title: "WooCommerce REST Sync Agent"
description: "Synchronizes WooCommerce product data bidirectionally using the WC REST API v3 and wc/v3/products endpoints. Handles batch create/update/delete with OAuth 1.0a authentication and rate-limit backoff."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/woocommerce-rest-sync-agent/"
category:
  - "WordPress &amp; CMS"
framework:
  - "Codex"
---

# WooCommerce REST Sync Agent

WooCommerce REST Sync Agent manages bidirectional product synchronization between WooCommerce stores or between WooCommerce and external inventory systems. It communicates via the official WC REST API v3, authenticating with OAuth 1.0a consumer key/secret pairs.

The agent uses the /wc/v3/products/batch endpoint to process up to 100 products per request, handling create, update, and delete operations atomically. It tracks sync state using product meta fields and SKU matching, resolving conflicts with configurable last-write-wins or source-priority strategies.

Supports complex product types including variable products with attributes and variations via /wc/v3/products/{id}/variations, grouped products, and external/affiliate products. Handles product images by URL with wp_handle_sideload(), categories via /wc/v3/products/categories, and tags. Implements exponential backoff on 429 rate-limit responses and maintains a local SQLite journal for crash recovery.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/woocommerce-rest-sync-agent/)
