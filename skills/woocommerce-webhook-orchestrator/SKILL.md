---
title: WooCommerce Webhook Orchestrator
description: The WooCommerce Webhook Orchestrator provides full lifecycle management
  for WooCommerce webhooks through the wc/v3/webhooks REST API. It creates, monitors,
  and rotates webhooks using the WC_Webhook class with support for all standard topics
  including order.created, product.updated, and customer.deleted events. The agent
  validates incoming webhook payloads using HMAC-SHA256 signature verification via
  the X-WC-Webhook-Signature header and the webhook secret. It implements intelligent
  retry logic with exponential backoff for failed deliveries, tracking delivery status
  through the WC_Webhook_Data_Store. The orchestrator supports webhook payload transformation
  using woocommerce_webhook_payload filters, allowing custom data enrichment before
  delivery. It manages webhook health through automated ping tests and failure rate
  monitoring, automatically disabling and re-enabling webhooks that exceed error thresholds.
  Includes support for WooCommerce Subscriptions renewal events and custom webhook
  topics via woocommerce_webhook_topic_hooks filter.
verification: security_reviewed
source: https://agentskillexchange.com/skills/woocommerce-webhook-orchestrator/
category:
- WordPress &amp; CMS
framework:
- Cursor
---

# WooCommerce Webhook Orchestrator

The WooCommerce Webhook Orchestrator provides full lifecycle management for WooCommerce webhooks through the wc/v3/webhooks REST API. It creates, monitors, and rotates webhooks using the WC_Webhook class with support for all standard topics including order.created, product.updated, and customer.deleted events. The agent validates incoming webhook payloads using HMAC-SHA256 signature verification via the X-WC-Webhook-Signature header and the webhook secret. It implements intelligent retry logic with exponential backoff for failed deliveries, tracking delivery status through the WC_Webhook_Data_Store. The orchestrator supports webhook payload transformation using woocommerce_webhook_payload filters, allowing custom data enrichment before delivery. It manages webhook health through automated ping tests and failure rate monitoring, automatically disabling and re-enabling webhooks that exceed error thresholds. Includes support for WooCommerce Subscriptions renewal events and custom webhook topics via woocommerce_webhook_topic_hooks filter.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/woocommerce-webhook-orchestrator/)
