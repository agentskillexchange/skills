---
title: "WooCommerce REST Order Manager"
description: "Queries and updates WooCommerce orders via the WooCommerce REST API v3 (/wp-json/wc/v3/orders), filters by status, date range, and customer, and bulk-updates fulfillment status. Generates order export CSVs with custom field mapping for 3PL handoff."
slug: "woocommerce-rest-order-manager"
category:
  - "WordPress &amp; CMS"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/woocommerce-rest-order-manager/"
---

# WooCommerce REST Order Manager

Queries and updates WooCommerce orders via the WooCommerce REST API v3 (/wp-json/wc/v3/orders), filters by status, date range, and customer, and bulk-updates fulfillment status. Generates order export CSVs with custom field mapping for 3PL handoff.

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
clawhub install woocommerce-rest-order-manager
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill handles order management operations against live WooCommerce stores. It can list pending orders by date range, update order status (processing, completed, refunded), add order notes, and export order data with line items, shipping details, and custom meta fields to CSV. Uses consumer key and secret authentication via Basic Auth headers.
Ideal for fulfillment teams, store operators, and 3PL integrations that need programmatic order access without building a full custom plugin. Not for payment processing or refund initiation — those require Stripe or gateway-specific SDKs. Requires WooCommerce 7.0+ and REST API enabled in WooCommerce settings.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/woocommerce-rest-order-manager/)
