---
title: WooCommerce REST Inventory Sync
description: WooCommerce REST Inventory Sync connects to the WooCommerce REST API
  v3 to maintain accurate stock levels across storefronts, marketplace integrations,
  and warehouse systems. It monitors product inventory through the /wc/v3/products
  endpoint and processes batch updates via /wc/v3/products/batch for efficient bulk
  synchronization. The skill hooks into woocommerce_product_set_stock and woocommerce_variation_set_stock
  actions to detect real-time inventory changes, then propagates updates to connected
  channels. It uses WP-CLI commands like wp wc product update for administrative corrections
  and generates low-stock reports by querying products with _stock below configurable
  thresholds. For multi-warehouse setups, it tracks stock per location using custom
  meta fields and reconciles totals against the WooCommerce product _stock value.
  Rate limiting respects the WooCommerce API headers, and webhook-based sync via woocommerce_webhook_delivery
  ensures near-instant propagation to external systems like Shopify or Amazon SP-API
  connectors.
verification: security_reviewed
source: https://github.com/woocommerce/woocommerce
category:
- WordPress &amp; CMS
framework:
- OpenClaw
tool_ecosystem:
  github_repo: woocommerce/woocommerce
  github_stars: 10233
---

# WooCommerce REST Inventory Sync

WooCommerce REST Inventory Sync connects to the WooCommerce REST API v3 to maintain accurate stock levels across storefronts, marketplace integrations, and warehouse systems. It monitors product inventory through the /wc/v3/products endpoint and processes batch updates via /wc/v3/products/batch for efficient bulk synchronization. The skill hooks into woocommerce_product_set_stock and woocommerce_variation_set_stock actions to detect real-time inventory changes, then propagates updates to connected channels. It uses WP-CLI commands like wp wc product update for administrative corrections and generates low-stock reports by querying products with _stock below configurable thresholds. For multi-warehouse setups, it tracks stock per location using custom meta fields and reconciles totals against the WooCommerce product _stock value. Rate limiting respects the WooCommerce API headers, and webhook-based sync via woocommerce_webhook_delivery ensures near-instant propagation to external systems like Shopify or Amazon SP-API connectors.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/woocommerce-rest-inventory-sync/)
