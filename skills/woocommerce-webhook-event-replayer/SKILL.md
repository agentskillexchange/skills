---
name: "WooCommerce Webhook Event Replayer"
description: "Captures, stores, and replays WooCommerce webhook deliveries for debugging and integration testing. Intercepts order.created, product.updated, and subscription.renewed events using the WC REST API and provides a local replay server for downstream consumers."
category: "WordPress & CMS"
framework: "ChatGPT Agents"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/woocommerce-webhook-event-replayer/"
---

# WooCommerce Webhook Event Replayer

Captures, stores, and replays WooCommerce webhook deliveries for debugging and integration testing. Intercepts order.created, product.updated, and subscription.renewed events using the WC REST API and provides a local replay server for downstream consumers.

## Overview

Overview

The WooCommerce Webhook Event Replayer skill enables agents to capture, inspect, and replay WooCommerce webhook payloads for integration testing and debugging. When a WooCommerce store fires events like `order.created`, `order.updated`, `product.updated`, or `subscription.renewed`, the payloads are sent to configured endpoints — but debugging failures requires re-triggering real transactions. This skill eliminates that by recording every delivery and allowing instant replay against any target URL.

How It Works

The agent registers a lightweight webhook receiver endpoint using `register_rest_route()` under the `ase-replay/v1` namespace. Incoming webhook payloads are validated against the `X-WC-Webhook-Signature` HMAC-SHA256 header using the webhook secret, then stored as JSON files in `wp-content/webhook-logs/` organized by topic and timestamp. Each stored event includes the full HTTP headers, request body, delivery ID, and the webhook resource URL.

Replay and Integration

To replay an event, the agent reads the stored payload and sends it via `wp_remote_post()` to the target URL with the original headers intact, including the signature header recalculated with the target’s secret. The skill also provides a WP-CLI command `wp wc-replay list` to browse stored events and `wp wc-replay fire <id> --target=<url>` to trigger replays. Supports filtering by date range, topic, and HTTP status code of the original delivery. Integrates with WooCommerce REST API v3 for webhook management and uses WordPress Transients for delivery status caching. All replay operations are logged to the WordPress debug log when `WP_DEBUG_LOG` is enabled.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill woocommerce-webhook-event-replayer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill woocommerce-webhook-event-replayer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill woocommerce-webhook-event-replayer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill woocommerce-webhook-event-replayer -a codex
```

### OpenClaw

```bash
clawhub install woocommerce-webhook-event-replayer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/woocommerce-webhook-event-replayer/
