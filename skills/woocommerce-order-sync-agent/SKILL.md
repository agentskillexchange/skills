---
name: "WooCommerce Order Sync Agent"
description: "Synchronizes WooCommerce orders with external ERPs using the WooCommerce REST API v3 and wp_schedule_event. Handles order status webhooks, inventory adjustments via wc_update_product_stock, and generates reconciliation reports."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/woocommerce-order-sync-agent/"
category:
  - "WordPress &amp; CMS"
framework:
  - "OpenClaw"
---

# WooCommerce Order Sync Agent

This skill provides end-to-end order synchronization between WooCommerce and external ERP systems like SAP Business One, NetSuite, or Odoo. It leverages the WooCommerce REST API v3 endpoints for orders, products, and customers, using OAuth 1.0a authentication. The agent registers custom webhooks via wc_webhook_process_delivery for real-time order status changes (pending, processing, completed, refunded). Inventory levels are kept in sync using wc_update_product_stock() with configurable thresholds. The skill includes retry logic with exponential backoff for failed API calls, batch processing for bulk order exports using WP-CLI wc commands, and structured logging via WC_Logger. It also generates daily reconciliation reports comparing local order counts against ERP totals, flagging discrepancies for manual review. Supports multi-currency setups through WooCommerce Currency Switcher hooks.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/woocommerce-order-sync-agent/)
