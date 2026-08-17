---
name: "Zinc Universal Checkout"
slug: "zinc-universal-checkout"
description: "Discover, buy, track, and return products across Amazon, Walmart, Target, Best Buy, eBay, and 50+ US retailers via the Zinc API (zinc.com). Use when the user wants to search for or buy a product, check out, check order status or tracking, cancel an order, or return an item."
verification: "listed"
source: "https://github.com/zincio/skills/tree/master/skills/universal-checkout"
category: "Developer Tools"
framework: "Claude Code"
---

# Zinc Universal Checkout

Zinc Universal Checkout is an Agent Skill that teaches compatible agents how to use the Zinc API (`https://api.zinc.com`) for the full US shopping lifecycle: discover products, place orders, track shipments, cancel queued orders, and open returns. One integration covers Amazon, Walmart, Target, Best Buy, eBay, Home Depot, Lowe's, Wayfair, and 50+ other US retailers. The live retailer catalog is `GET https://api.zinc.com/retailers` (free, no auth). Product discovery uses `GET /search` (or metered `POST /agent/search` on the payment rail) and returns directly orderable product URLs. Orders go to `POST /orders` or `POST /agent/orders`; tracking, cancel, and returns use `GET /orders/{id}`, `POST /orders/{id}/cancel`, and `POST /returns`.

## Authentication

Pick one method:

- **API key:** set `ZINC_API_KEY` from [app.zinc.com](https://app.zinc.com) and send `Authorization: Bearer $ZINC_API_KEY` to `/orders` and related endpoints. This is the standard flow for a funded Zinc account.
- **MPP (Machine Payments Protocol):** no Zinc account required. Pay per request via Stripe Link (cards/wallets), Tempo stablecoins (`TEMPO_PRIVATE_KEY`), or x402 (USDC on Base). Agent endpoints live under `/agent/*`. Data calls such as search are typically $0.01 each; `GET /retailers` is free. Try the flow without code at [agent.zinc.com](https://agent.zinc.com).

Amounts are in US cents (`5000` = $50.00). Required order fields include a product URL, a US shipping address, and `max_price`.

## Safety

Always confirm with the user before placing an order or opening a return — both spend real money. Search, order listing, and tracking reads are safe. `max_price` is the **total** ceiling in cents, including item price, tax, and shipping/handling, not the item subtotal. A value that omits shipping trips `max_price_exceeded`. On the MPP rail, Zinc authorizes `max_price + $1` (the API fee) on the payment method.

## Upstream install and per-retailer skills

The canonical catalog is [zincio/skills](https://github.com/zincio/skills). For general shopping across retailers, install the upstream skill:

```bash
npm exec --package=skills@1.5.7 -- skills add zincio/skills --skill universal-checkout
```

Per-retailer skills also exist (`amazon-checkout`, `walmart-checkout`, `target-checkout`, `bestbuy-checkout`, `ebay-checkout`, and others). Use those only when the agent should buy from a single store. Do not stack several near-identical retailer skills — overlapping descriptions make triggering ambiguous. Prefer `universal-checkout` when buying across stores.

## Support

- Email: [support@zinc.com](mailto:support@zinc.com)
- Docs: [https://www.zinc.com/docs/v2/agent-skills/overview](https://www.zinc.com/docs/v2/agent-skills/overview)

## Installation

No source-backed install or usage instructions could be extracted automatically. Review the upstream project before running this skill in a sensitive workflow.

- Source: https://github.com/zincio/skills/tree/master/skills/universal-checkout

