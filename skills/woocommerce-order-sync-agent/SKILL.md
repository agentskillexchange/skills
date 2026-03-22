---
name: "WooCommerce Order Sync Agent"
description: "Synchronizes WooCommerce orders with external ERPs using the WooCommerce REST API v3 and wp_schedule_event. Handles order status webhooks, inventory adjustments via wc_update_product_stock, and generates reconciliation reports."
category: "WordPress & CMS"
framework: "OpenClaw"
verification: "community"
rating: "0"
reviews: "0"
creator: "Community"
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skill/woocommerce-order-sync-agent/"
---

# WooCommerce Order Sync Agent

Synchronizes WooCommerce orders with external ERPs using the WooCommerce REST API v3 and wp_schedule_event. Handles order status webhooks, inventory adjustments via wc_update_product_stock, and generates reconciliation reports.

## Installation

Install this skill in your agent framework of choice:

### npx (Any Agent)
```bash
npx agentskills install woocommerce-order-sync-agent
```

### Claude Code
```bash
claude mcp add skill-woocommerce-order-sync-agent -- npx agentskills run woocommerce-order-sync-agent
```

### Cursor
Add to your `.cursor/mcp.json`:
```json
{
  "mcpServers": {
    "skill-woocommerce-order-sync-agent": {
      "command": "npx",
      "args": ["agentskills", "run", "woocommerce-order-sync-agent"]
    }
  }
}
```

### OpenClaw
```bash
clawhub install woocommerce-order-sync-agent
```

### Codex
```bash
codex install woocommerce-order-sync-agent
```

## Details

| | |
|---|---|
| **Category** | WordPress & CMS |
| **Framework** | OpenClaw |
| **Verification** | community |
| **Rating** | 0 ⭐ (0 reviews) |

## Creator

**Community**


## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/woocommerce-order-sync-agent/)
- [Browse All Skills](https://agentskillexchange.com/)
