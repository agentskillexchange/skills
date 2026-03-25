---
name: "WooCommerce REST Order Manager"
description: "Queries and updates WooCommerce orders via the WooCommerce REST API v3 (/wp-json/wc/v3/orders), filters by status, date range, and customer, and bulk-updates fulfillment status. Generates order export CSVs with custom field mapping for 3PL handoff."
category: "WordPress & CMS"
framework: "Claude Code"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/woocommerce-rest-order-manager/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "stripe"  # from ase_tool_match
  github_stars: 4377  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 8442269  # from ase_npm_downloads
  github_repo: "stripe/stripe-node"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
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
