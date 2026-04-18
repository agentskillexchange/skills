---
title: "WooCommerce Webhook Orchestrator"
description: "Manages WooCommerce webhook lifecycles using the wc/v3/webhooks REST API and WC_Webhook class. Handles order, product, and customer event routing with payload signature verification via X-WC-Webhook-Signature."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/woocommerce-webhook-orchestrator/"
category:
  - "WordPress & CMS"
framework:
  - "Cursor"
---

# WooCommerce Webhook Orchestrator

The WooCommerce Webhook Orchestrator provides full lifecycle management for WooCommerce webhooks through the wc/v3/webhooks REST API. It creates, monitors, and rotates webhooks using the WC_Webhook class with support for all standard topics including order.created, product.updated, and customer.deleted events. The agent validates incoming webhook payloads using HMAC-SHA256 signature verification via the X-WC-Webhook-Signature header and the webhook secret. It implements intelligent retry logic with exponential backoff for failed deliveries, tracking delivery status through the WC_Webhook_Data_Store. The orchestrator supports webhook payload transformation using woocommerce_webhook_payload filters, allowing custom data enrichment before delivery. It manages webhook health through automated ping tests and failure rate monitoring, automatically disabling and re-enabling webhooks that exceed error thresholds. Includes support for WooCommerce Subscriptions renewal events and custom webhook topics via woocommerce_webhook_topic_hooks filter.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/woocommerce-webhook-orchestrator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/woocommerce-webhook-orchestrator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/woocommerce-webhook-orchestrator/)
