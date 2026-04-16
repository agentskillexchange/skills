---
title: "WooCommerce REST Order Manager"
description: "Queries and updates WooCommerce orders via the WooCommerce REST API v3 (/wp-json/wc/v3/orders), filters by status, date range, and customer, and bulk-updates fulfillment status. Generates order export CSVs with custom field mapping for 3PL handoff."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/woocommerce-rest-order-manager/"
category:
  - "WordPress & CMS"
framework:
  - "Claude Code"
---

# WooCommerce REST Order Manager

Queries and updates WooCommerce orders via the WooCommerce REST API v3 (/wp-json/wc/v3/orders), filters by status, date range, and customer, and bulk-updates fulfillment status. Generates order export CSVs with custom field mapping for 3PL handoff.


This skill handles order management operations against live WooCommerce stores. It can list pending orders by date range, update order status (processing, completed, refunded), add order notes, and export order data with line items, shipping details, and custom meta fields to CSV. Uses consumer key and secret authentication via Basic Auth headers.


Ideal for fulfillment teams, store operators, and 3PL integrations that need programmatic order access without building a full custom plugin. Not for payment processing or refund initiation — those require Stripe or gateway-specific SDKs. Requires WooCommerce 7.0+ and REST API enabled in WooCommerce settings.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/woocommerce-rest-order-manager/)
