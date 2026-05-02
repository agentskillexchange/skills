---
title: "WooCommerce Order Sync Agent"
description: "Synchronizes WooCommerce orders with external ERPs using the WooCommerce REST API v3 and wp_schedule_event. Handles order status webhooks, inventory adjustments via wc_update_product_stock, and generates reconciliation reports."
verification: "security_reviewed"
source: "https://github.com/woocommerce/woocommerce"
category:
  - "WordPress & CMS"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "woocommerce/woocommerce"
  github_stars: 10271
---

# WooCommerce Order Sync Agent

This skill provides end-to-end order synchronization between WooCommerce and external ERP systems like SAP Business One, NetSuite, or Odoo. It leverages the WooCommerce REST API v3 endpoints for orders, products, and customers, using OAuth 1.0a authentication. The agent registers custom webhooks via wc_webhook_process_delivery for real-time order status changes (pending, processing, completed, refunded). Inventory levels are kept in sync using wc_update_product_stock() with configurable thresholds. The skill includes retry logic with exponential backoff for failed API calls, batch processing for bulk order exports using WP-CLI wc commands, and structured logging via WC_Logger. It also generates daily reconciliation reports comparing local order counts against ERP totals, flagging discrepancies for manual review. Supports multi-currency setups through WooCommerce Currency Switcher hooks.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/woocommerce-order-sync-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/woocommerce-order-sync-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/woocommerce-order-sync-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/woocommerce-order-sync-agent/)
