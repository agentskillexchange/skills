---
title: "WooCommerce Order Sync Agent"
description: "Synchronizes WooCommerce orders with external ERPs using the WooCommerce REST API v3 and wp_schedule_event. Handles order status webhooks, inventory adjustments via wc_update_product_stock, and generates reconciliation reports."
slug: "woocommerce-order-sync-agent"
category:
  - "WordPress &amp; CMS"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/woocommerce-order-sync-agent/"
---

# WooCommerce Order Sync Agent

Synchronizes WooCommerce orders with external ERPs using the WooCommerce REST API v3 and wp_schedule_event. Handles order status webhooks, inventory adjustments via wc_update_product_stock, and generates reconciliation reports.

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
clawhub install woocommerce-order-sync-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill provides end-to-end order synchronization between WooCommerce and external ERP systems like SAP Business One, NetSuite, or Odoo. It leverages the WooCommerce REST API v3 endpoints for orders, products, and customers, using OAuth 1.0a authentication. The agent registers custom webhooks via wc_webhook_process_delivery for real-time order status changes (pending, processing, completed, refunded). Inventory levels are kept in sync using wc_update_product_stock() with configurable thresholds. The skill includes retry logic with exponential backoff for failed API calls, batch processing for bulk order exports using WP-CLI wc commands, and structured logging via WC_Logger. It also generates daily reconciliation reports comparing local order counts against ERP totals, flagging discrepancies for manual review. Supports multi-currency setups through WooCommerce Currency Switcher hooks.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/woocommerce-order-sync-agent/)
