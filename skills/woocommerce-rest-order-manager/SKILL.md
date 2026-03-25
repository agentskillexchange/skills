---
name: "WooCommerce REST Order Manager"
description: "Queries and updates WooCommerce orders via the WooCommerce REST API v3 (/wp-json/wc/v3/orders), filters by status, date range, and customer, and bulk-updates fulfillment status. Generates order export CSVs with custom field mapping for 3PL handoff."
category: "WordPress & CMS"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/woocommerce-rest-order-manager/"
tool_ecosystem:
  tool: "stripe"
  github_stars: 4377
  npm_weekly_downloads: 8442269
  github_repo: "stripe/stripe-node"
  license: "MIT"
  maintained: true
---

# WooCommerce REST Order Manager

Queries and updates WooCommerce orders via the WooCommerce REST API v3 (/wp-json/wc/v3/orders), filters by status, date range, and customer, and bulk-updates fulfillment status. Generates order export CSVs with custom field mapping for 3PL handoff.

## Overview

Queries and updates WooCommerce orders via the WooCommerce REST API v3 (/wp-json/wc/v3/orders), filters by status, date range, and customer, and bulk-updates fulfillment status. Generates order export CSVs with custom field mapping for 3PL handoff.

This skill handles order management operations against live WooCommerce stores. It can list pending orders by date range, update order status (processing, completed, refunded), add order notes, and export order data with line items, shipping details, and custom meta fields to CSV. Uses consumer key and secret authentication via Basic Auth headers.

Ideal for fulfillment teams, store operators, and 3PL integrations that need programmatic order access without building a full custom plugin. Not for payment processing or refund initiation — those require Stripe or gateway-specific SDKs. Requires WooCommerce 7.0+ and REST API enabled in WooCommerce settings.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill woocommerce-rest-order-manager
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill woocommerce-rest-order-manager -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill woocommerce-rest-order-manager -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill woocommerce-rest-order-manager -a codex
```

### OpenClaw

```bash
clawhub install woocommerce-rest-order-manager
```

## Source

- Marketplace: https://agentskillexchange.com/skills/woocommerce-rest-order-manager/
