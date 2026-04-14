---
title: "WooCommerce Webhook Orchestrator"
description: "Manages WooCommerce webhook lifecycles using the wc/v3/webhooks REST API and WC_Webhook class. Handles order, product, and customer event routing with payload signature verification via X-WC-Webhook-Signature."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/woocommerce-webhook-orchestrator/"
category:
  - "WordPress &amp; CMS"
framework:
  - "Cursor"
---

# WooCommerce Webhook Orchestrator

The WooCommerce Webhook Orchestrator provides full lifecycle management for WooCommerce webhooks through the wc/v3/webhooks REST API. It creates, monitors, and rotates webhooks using the WC_Webhook class with support for all standard topics including order.created, product.updated, and customer.deleted events. The agent validates incoming webhook payloads using HMAC-SHA256 signature verification via the X-WC-Webhook-Signature header and the webhook secret. It implements intelligent retry logic with exponential backoff for failed deliveries, tracking delivery status through the WC_Webhook_Data_Store. The orchestrator supports webhook payload transformation using woocommerce_webhook_payload filters, allowing custom data enrichment before delivery. It manages webhook health through automated ping tests and failure rate monitoring, automatically disabling and re-enabling webhooks that exceed error thresholds. Includes support for WooCommerce Subscriptions renewal events and custom webhook topics via woocommerce_webhook_topic_hooks filter.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/woocommerce-webhook-orchestrator/)
