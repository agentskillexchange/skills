---
name: "WooCommerce Webhook Delivery Inspector"
description: "Inspects WooCommerce webhook reliability through the `WC_Webhook` model, Action Scheduler queues, and REST endpoints such as `/wp-json/wc/v3/webhooks`. Great for tracing failed deliveries, replay patterns, and event coverage across order, product, and customer workflows."
verification: security_reviewed
source: "https://github.com/woocommerce/woocommerce"
category:
  - "WordPress &amp; CMS"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "woocommerce/woocommerce"
  github_stars: 10231
---

# WooCommerce Webhook Delivery Inspector

WooCommerce Webhook Delivery Inspector is meant for stores and integrations teams that need a dependable way to understand why webhook events are firing, failing, or arriving out of sequence. The skill uses real WooCommerce interfaces such as the WC_Webhook class, Action Scheduler job data, and REST resources like /wp-json/wc/v3/webhooks to inspect endpoint configuration, topic coverage, delivery history, and retry behavior. That makes it useful when downstream systems miss order updates or inventory changes appear to be delayed.
The skill can separate transport failures from application logic problems by checking webhook status, secret usage, response codes, and the queued jobs that actually dispatch deliveries. It also helps teams review whether they are listening to the correct topics for orders, products, coupons, and customers, rather than assuming the remote service is at fault. In environments with ERP or warehouse syncs, that distinction matters a lot.
Use this skill to audit WooCommerce event flows, debug broken integrations, and tighten webhook observability before delivery issues turn into fulfillment or reporting gaps.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/woocommerce-webhook-delivery-inspector/)
