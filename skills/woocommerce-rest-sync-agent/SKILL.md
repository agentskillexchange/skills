---
title: WooCommerce REST Sync Agent
description: WooCommerce REST Sync Agent manages bidirectional product synchronization
  between WooCommerce stores or between WooCommerce and external inventory systems.
  It communicates via the official WC REST API v3, authenticating with OAuth 1.0a
  consumer key/secret pairs. The agent uses the /wc/v3/products/batch endpoint to
  process up to 100 products per request, handling create, update, and delete operations
  atomically. It tracks sync state using product meta fields and SKU matching, resolving
  conflicts with configurable last-write-wins or source-priority strategies. Supports
  complex product types including variable products with attributes and variations
  via /wc/v3/products/{id}/variations , grouped products, and external/affiliate products.
  Handles product images by URL with wp_handle_sideload() , categories via /wc/v3/products/categories
  , and tags. Implements exponential backoff on 429 rate-limit responses and maintains
  a local SQLite journal for crash recovery.
verification: security_reviewed
source: https://agentskillexchange.com/skills/woocommerce-rest-sync-agent/
category:
- WordPress &amp; CMS
framework:
- Codex
---

# WooCommerce REST Sync Agent

WooCommerce REST Sync Agent manages bidirectional product synchronization between WooCommerce stores or between WooCommerce and external inventory systems. It communicates via the official WC REST API v3, authenticating with OAuth 1.0a consumer key/secret pairs. The agent uses the /wc/v3/products/batch endpoint to process up to 100 products per request, handling create, update, and delete operations atomically. It tracks sync state using product meta fields and SKU matching, resolving conflicts with configurable last-write-wins or source-priority strategies. Supports complex product types including variable products with attributes and variations via /wc/v3/products/{id}/variations , grouped products, and external/affiliate products. Handles product images by URL with wp_handle_sideload() , categories via /wc/v3/products/categories , and tags. Implements exponential backoff on 429 rate-limit responses and maintains a local SQLite journal for crash recovery.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/woocommerce-rest-sync-agent/)
