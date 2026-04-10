---
name: "WooCommerce REST Order Manager"
description: "Queries and updates WooCommerce orders via the WooCommerce REST API v3 (/wp-json/wc/v3/orders), filters by status, date range, and customer, and bulk-updates fulfillment status. Generates order export CSVs with custom field mapping for 3PL handoff."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/woocommerce-rest-order-manager/"
category:
  - "WordPress &amp; CMS"
framework:
  - "Claude Code"
---

# WooCommerce REST Order Manager

Queries and updates WooCommerce orders via the WooCommerce REST API v3 (/wp-json/wc/v3/orders), filters by status, date range, and customer, and bulk-updates fulfillment status. Generates order export CSVs with custom field mapping for 3PL handoff.
This skill handles order management operations against live WooCommerce stores. It can list pending orders by date range, update order status (processing, completed, refunded), add order notes, and export order data with line items, shipping details, and custom meta fields to CSV. Uses consumer key and secret authentication via Basic Auth headers.
Ideal for fulfillment teams, store operators, and 3PL integrations that need programmatic order access without building a full custom plugin. Not for payment processing or refund initiation — those require Stripe or gateway-specific SDKs. Requires WooCommerce 7.0+ and REST API enabled in WooCommerce settings.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/woocommerce-rest-order-manager/)
