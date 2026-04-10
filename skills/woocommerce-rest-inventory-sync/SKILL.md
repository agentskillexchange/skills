---
title: "WooCommerce REST Inventory Sync"
description: "Synchronizes WooCommerce product inventory across multiple channels using the WooCommerce REST API v3 and wp_update_post hooks. Handles stock level reconciliation, low-stock alerts via WP-CLI, and batch product updates through the /wc/v3/products/batch endpoint."
slug: "woocommerce-rest-inventory-sync"
category:
  - "WordPress &amp; CMS"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://github.com/woocommerce/woocommerce"
tool_ecosystem:
  github_repo: "woocommerce/woocommerce"
  github_stars: 10243
listed: true
---

# WooCommerce REST Inventory Sync

Synchronizes WooCommerce product inventory across multiple channels using the WooCommerce REST API v3 and wp_update_post hooks. Handles stock level reconciliation, low-stock alerts via WP-CLI, and batch product updates through the /wc/v3/products/batch endpoint.

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
clawhub install woocommerce-rest-inventory-sync
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

WooCommerce REST Inventory Sync connects to the WooCommerce REST API v3 to maintain accurate stock levels across storefronts, marketplace integrations, and warehouse systems. It monitors product inventory through the /wc/v3/products endpoint and processes batch updates via /wc/v3/products/batch for efficient bulk synchronization.
The skill hooks into woocommerce_product_set_stock and woocommerce_variation_set_stock actions to detect real-time inventory changes, then propagates updates to connected channels. It uses WP-CLI commands like wp wc product update for administrative corrections and generates low-stock reports by querying products with _stock below configurable thresholds.
For multi-warehouse setups, it tracks stock per location using custom meta fields and reconciles totals against the WooCommerce product _stock value. Rate limiting respects the WooCommerce API headers, and webhook-based sync via woocommerce_webhook_delivery ensures near-instant propagation to external systems like Shopify or Amazon SP-API connectors.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/woocommerce-rest-inventory-sync/)
