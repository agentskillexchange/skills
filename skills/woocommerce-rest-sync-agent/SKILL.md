---
title: "WooCommerce REST Sync Agent"
description: "WooCommerce REST Sync Agent manages bidirectional product synchronization between WooCommerce stores or between WooCommerce and external inventory systems. It communicates via the official WC REST API v3, authenticating with OAuth 1.0a consumer key/secret pairs. The agent uses the /wc/v3/products/batch endpoint to process up to 100 products per request, handling create, update, and delete operations atomically. It tracks sync state using product meta fields and SKU matching, resolving conflicts with configurable last-write-wins or source-priority strategies. Supports complex product types including variable products with attributes and variations via /wc/v3/products/{id}/variations , grouped products, and external/affiliate products. Handles product images by URL with wp_handle_sideload() , categories via /wc/v3/products/categories , and tags. Implements exponential backoff on 429 rate-limit responses and maintains a local SQLite journal for crash recovery."
source: "https://agentskillexchange.com/skills/woocommerce-rest-sync-agent/"
verification: "security_reviewed"
category:
  - "WordPress &amp; CMS"
framework:
  - "Codex"
---

# WooCommerce REST Sync Agent

WooCommerce REST Sync Agent manages bidirectional product synchronization between WooCommerce stores or between WooCommerce and external inventory systems. It communicates via the official WC REST API v3, authenticating with OAuth 1.0a consumer key/secret pairs. The agent uses the /wc/v3/products/batch endpoint to process up to 100 products per request, handling create, update, and delete operations atomically. It tracks sync state using product meta fields and SKU matching, resolving conflicts with configurable last-write-wins or source-priority strategies. Supports complex product types including variable products with attributes and variations via /wc/v3/products/{id}/variations , grouped products, and external/affiliate products. Handles product images by URL with wp_handle_sideload() , categories via /wc/v3/products/categories , and tags. Implements exponential backoff on 429 rate-limit responses and maintains a local SQLite journal for crash recovery.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/woocommerce-rest-sync-agent/)
