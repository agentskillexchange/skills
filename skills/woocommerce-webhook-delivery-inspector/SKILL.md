---
title: "WooCommerce Webhook Delivery Inspector"
description: "Inspects WooCommerce webhook reliability through the `WC_Webhook` model, Action Scheduler queues, and REST endpoints such as `/wp-json/wc/v3/webhooks`. Great for tracing failed deliveries, replay patterns, and event coverage across order, product, and customer workflows."
slug: "woocommerce-webhook-delivery-inspector"
category:
  - "WordPress &amp; CMS"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://github.com/woocommerce/woocommerce"
tool_ecosystem:
  github_repo: "woocommerce/woocommerce"
  github_stars: 10231
---

# WooCommerce Webhook Delivery Inspector

Inspects WooCommerce webhook reliability through the `WC_Webhook` model, Action Scheduler queues, and REST endpoints such as `/wp-json/wc/v3/webhooks`. Great for tracing failed deliveries, replay patterns, and event coverage across order, product, and customer workflows.

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
clawhub install woocommerce-webhook-delivery-inspector
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

WooCommerce Webhook Delivery Inspector is meant for stores and integrations teams that need a dependable way to understand why webhook events are firing, failing, or arriving out of sequence. The skill uses real WooCommerce interfaces such as the WC_Webhook class, Action Scheduler job data, and REST resources like /wp-json/wc/v3/webhooks to inspect endpoint configuration, topic coverage, delivery history, and retry behavior. That makes it useful when downstream systems miss order updates or inventory changes appear to be delayed.
The skill can separate transport failures from application logic problems by checking webhook status, secret usage, response codes, and the queued jobs that actually dispatch deliveries. It also helps teams review whether they are listening to the correct topics for orders, products, coupons, and customers, rather than assuming the remote service is at fault. In environments with ERP or warehouse syncs, that distinction matters a lot.
Use this skill to audit WooCommerce event flows, debug broken integrations, and tighten webhook observability before delivery issues turn into fulfillment or reporting gaps.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/woocommerce-webhook-delivery-inspector/)
