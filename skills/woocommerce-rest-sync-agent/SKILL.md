---
title: "WooCommerce REST Sync Agent"
description: "WooCommerce REST Sync Agent manages bidirectional product synchronization between WooCommerce stores or between WooCommerce and external inventory systems. It communicates via the official WC REST API v3, authenticating with OAuth 1.0a consumer key/secret pairs.\nThe agent uses the /wc/v3/products/batch endpoint to process up to 100 products per request, handling create, update, and delete operations atomically. It tracks sync state using product meta fields and SKU matching, resolving conflicts with configurable last-write-wins or source-priority strategies.\nSupports complex product types including variable products with attributes and variations via /wc/v3/products/{id}/variations, grouped products, and external/affiliate products. Handles product images by URL with wp_handle_sideload(), categories via /wc/v3/products/categories, and tags. Implements exponential backoff on 429 rate-limit responses and maintains a local SQLite journal for crash recovery."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/woocommerce-rest-sync-agent/"
framework:
  - "Codex"
---

# WooCommerce REST Sync Agent

WooCommerce REST Sync Agent manages bidirectional product synchronization between WooCommerce stores or between WooCommerce and external inventory systems. It communicates via the official WC REST API v3, authenticating with OAuth 1.0a consumer key/secret pairs.
The agent uses the /wc/v3/products/batch endpoint to process up to 100 products per request, handling create, update, and delete operations atomically. It tracks sync state using product meta fields and SKU matching, resolving conflicts with configurable last-write-wins or source-priority strategies.
Supports complex product types including variable products with attributes and variations via /wc/v3/products/{id}/variations, grouped products, and external/affiliate products. Handles product images by URL with wp_handle_sideload(), categories via /wc/v3/products/categories, and tags. Implements exponential backoff on 429 rate-limit responses and maintains a local SQLite journal for crash recovery.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/woocommerce-rest-sync-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/woocommerce-rest-sync-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/woocommerce-rest-sync-agent/)
