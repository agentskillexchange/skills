---
name: "WooCommerce Order Sync Agent"
description: "Synchronizes WooCommerce orders with external ERPs using the WooCommerce REST API v3 and wp_schedule_event. Handles order status webhooks, inventory adjustments via wc_update_product_stock, and generates reconciliation reports."
category: "WordPress &amp; CMS"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/woocommerce-order-sync-agent/"
---
# WooCommerce Order Sync Agent

Synchronizes WooCommerce orders with external ERPs using the WooCommerce REST API v3 and wp_schedule_event. Handles order status webhooks, inventory adjustments via wc_update_product_stock, and generates reconciliation reports.

## Overview

This skill provides end-to-end order synchronization between WooCommerce and external ERP systems like SAP Business One, NetSuite, or Odoo. It leverages the WooCommerce REST API v3 endpoints for orders, products, and customers, using OAuth 1.0a authentication. The agent registers custom webhooks via wc_webhook_process_delivery for real-time order status changes (pending, processing, completed, refunded). Inventory levels are kept in sync using wc_update_product_stock() with configurable thresholds. The skill includes retry logic with exponential backoff for failed API calls, batch processing for bulk order exports using WP-CLI wc commands, and structured logging via WC_Logger. It also generates daily reconciliation reports comparing local order counts against ERP totals, flagging discrepancies for manual review. Supports multi-currency setups through WooCommerce Currency Switcher hooks.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill woocommerce-order-sync-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill woocommerce-order-sync-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill woocommerce-order-sync-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill woocommerce-order-sync-agent -a codex
```

### OpenClaw

```bash
clawhub install woocommerce-order-sync-agent
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/woocommerce-order-sync-agent/)
