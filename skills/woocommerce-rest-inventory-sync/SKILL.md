---
title: "WooCommerce REST Inventory Sync"
description: "WooCommerce REST Inventory Sync connects to the WooCommerce REST API v3 to maintain accurate stock levels across storefronts, marketplace integrations, and warehouse systems. It monitors product inventory through the /wc/v3/products endpoint and processes batch updates via /wc/v3/products/batch for efficient bulk synchronization.\nThe skill hooks into woocommerce_product_set_stock and woocommerce_variation_set_stock actions to detect real-time inventory changes, then propagates updates to connected channels. It uses WP-CLI commands like wp wc product update for administrative corrections and generates low-stock reports by querying products with _stock below configurable thresholds.\nFor multi-warehouse setups, it tracks stock per location using custom meta fields and reconciles totals against the WooCommerce product _stock value. Rate limiting respects the WooCommerce API headers, and webhook-based sync via woocommerce_webhook_delivery ensures near-instant propagation to external systems like Shopify or Amazon SP-API connectors."
verification: security_reviewed
source: "https://github.com/woocommerce/woocommerce"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "woocommerce/woocommerce"
  github_stars: 10243
---

# WooCommerce REST Inventory Sync

WooCommerce REST Inventory Sync connects to the WooCommerce REST API v3 to maintain accurate stock levels across storefronts, marketplace integrations, and warehouse systems. It monitors product inventory through the /wc/v3/products endpoint and processes batch updates via /wc/v3/products/batch for efficient bulk synchronization.
The skill hooks into woocommerce_product_set_stock and woocommerce_variation_set_stock actions to detect real-time inventory changes, then propagates updates to connected channels. It uses WP-CLI commands like wp wc product update for administrative corrections and generates low-stock reports by querying products with _stock below configurable thresholds.
For multi-warehouse setups, it tracks stock per location using custom meta fields and reconciles totals against the WooCommerce product _stock value. Rate limiting respects the WooCommerce API headers, and webhook-based sync via woocommerce_webhook_delivery ensures near-instant propagation to external systems like Shopify or Amazon SP-API connectors.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/woocommerce-rest-inventory-sync
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/woocommerce-rest-inventory-sync` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/woocommerce-rest-inventory-sync/)
