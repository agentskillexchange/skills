---
title: "WooCommerce Webhook Delivery Inspector"
description: "Inspects WooCommerce webhook reliability through the `WC_Webhook` model, Action Scheduler queues, and REST endpoints such as `/wp-json/wc/v3/webhooks`. Great for tracing failed deliveries, replay patterns, and event coverage across order, product, and customer workflows."
verification: security_reviewed
source: "https://github.com/woocommerce/woocommerce"
category:
  - "WordPress &amp; CMS"
tool_ecosystem:
  github_repo: "woocommerce/woocommerce"
  github_stars: 10231
---

# WooCommerce Webhook Delivery Inspector

Inspects WooCommerce webhook reliability through the `WC_Webhook` model, Action Scheduler queues, and REST endpoints such as `/wp-json/wc/v3/webhooks`. Great for tracing failed deliveries, replay patterns, and event coverage across order, product, and customer workflows.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/woocommerce-webhook-delivery-inspector/)
