---
name: "WooCommerce REST Inventory Sync"
description: "Synchronizes WooCommerce product inventory across multiple channels using the WooCommerce REST API v3 and wp_update_post hooks. Handles stock level reconciliation, low-stock alerts via WP-CLI, and batch product updates through the /wc/v3/products/batch endpoint."
category: "WordPress & CMS"
framework: "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/woocommerce-rest-inventory-sync/"
---

# WooCommerce REST Inventory Sync

Synchronizes WooCommerce product inventory across multiple channels using the WooCommerce REST API v3 and wp_update_post hooks. Handles stock level reconciliation, low-stock alerts via WP-CLI, and batch product updates through the /wc/v3/products/batch endpoint.

## Overview

WooCommerce REST Inventory Sync connects to the WooCommerce REST API v3 to maintain accurate stock levels across storefronts, marketplace integrations, and warehouse systems. It monitors product inventory through the /wc/v3/products endpoint and processes batch updates via /wc/v3/products/batch for efficient bulk synchronization.

The skill hooks into woocommerce_product_set_stock and woocommerce_variation_set_stock actions to detect real-time inventory changes, then propagates updates to connected channels. It uses WP-CLI commands like wp wc product update for administrative corrections and generates low-stock reports by querying products with _stock below configurable thresholds.

For multi-warehouse setups, it tracks stock per location using custom meta fields and reconciles totals against the WooCommerce product _stock value. Rate limiting respects the WooCommerce API headers, and webhook-based sync via woocommerce_webhook_delivery ensures near-instant propagation to external systems like Shopify or Amazon SP-API connectors.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill woocommerce-rest-inventory-sync
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill woocommerce-rest-inventory-sync -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill woocommerce-rest-inventory-sync -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill woocommerce-rest-inventory-sync -a codex
```

### OpenClaw

```bash
clawhub install woocommerce-rest-inventory-sync
```

## Source

- Marketplace: https://agentskillexchange.com/skills/woocommerce-rest-inventory-sync/
