---
name: "WooCommerce Webhook Delivery Inspector"
description: "Inspects WooCommerce webhook reliability through the `WC_Webhook` model, Action Scheduler queues, and REST endpoints such as `/wp-json/wc/v3/webhooks`. Great for tracing failed deliveries, replay patterns, and event coverage across order, product, and customer workflows."
category: "WordPress & CMS"
framework: "ChatGPT Agents"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/woocommerce-webhook-delivery-inspector/"
---

# WooCommerce Webhook Delivery Inspector

Inspects WooCommerce webhook reliability through the `WC_Webhook` model, Action Scheduler queues, and REST endpoints such as `/wp-json/wc/v3/webhooks`. Great for tracing failed deliveries, replay patterns, and event coverage across order, product, and customer workflows.

## Overview

WooCommerce Webhook Delivery Inspector is meant for stores and integrations teams that need a dependable way to understand why webhook events are firing, failing, or arriving out of sequence. The skill uses real WooCommerce interfaces such as the `WC_Webhook` class, Action Scheduler job data, and REST resources like `/wp-json/wc/v3/webhooks` to inspect endpoint configuration, topic coverage, delivery history, and retry behavior. That makes it useful when downstream systems miss order updates or inventory changes appear to be delayed.

The skill can separate transport failures from application logic problems by checking webhook status, secret usage, response codes, and the queued jobs that actually dispatch deliveries. It also helps teams review whether they are listening to the correct topics for orders, products, coupons, and customers, rather than assuming the remote service is at fault. In environments with ERP or warehouse syncs, that distinction matters a lot.

Use this skill to audit WooCommerce event flows, debug broken integrations, and tighten webhook observability before delivery issues turn into fulfillment or reporting gaps.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill woocommerce-webhook-delivery-inspector
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill woocommerce-webhook-delivery-inspector -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill woocommerce-webhook-delivery-inspector -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill woocommerce-webhook-delivery-inspector -a codex
```

### OpenClaw

```bash
clawhub install woocommerce-webhook-delivery-inspector
```

## Source

- Marketplace: https://agentskillexchange.com/skills/woocommerce-webhook-delivery-inspector/
