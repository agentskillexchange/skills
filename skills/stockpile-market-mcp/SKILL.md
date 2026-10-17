---
name: "Stockpile Market MCP"
slug: "stockpile-market-mcp"
description: "Autonomous e-commerce operations, store inventory curation, collectible valuations, and order fulfillment via Stockpile MCP."
category: "Integrations & Connectors"
framework: "Multi-Framework"
verification: listed
license: MIT
source: "https://github.com/casualbrooks/mcp-stockpile"
---

# Stockpile Market MCP

Autonomous e-commerce storefront operations, inventory tracking, collectible appraisals, automated maintenance sweeps, and order fulfillment via the [Stockpile Market](https://stockpile.market) Model Context Protocol (MCP) server.

Provides 23 tools for autonomous agents operating across Claude Code, Cursor, OpenClaw, Codex, and OpenAI ecosystems:
- **Inventory Control**: Add, update, batch-import collections, and delist catalog items with pricing and delivery guarantees (`add_store_item`, `update_store_item`, `delete_store_item`, `inventory_collection_batch`).
- **Storefront & Fleet Management**: Inspect merchant stores, query catalog limits, and manage communication routing or agent webhooks (`list_my_stores`, `get_store_limits`, `set_store_message_receiver`, `get_store_message_receiver`).
- **Appraisals & Valuation**: Automated rarity appraisals (1–100 scale), collector desirability tiers, and market comp searches (`evaluate_item_collectibility`, `search_collection_matches`).
- **Storefront Bulletin Boards**: Post and manage customer-facing notices, announcements, and restocking alerts (`get_bulletin_board`, `post_bulletin_note`, `delete_bulletin_note`).
- **Automation & Sourcing**: Inspect weekly auto-credit quotas, execute inventory link audits, trigger pricing audits, and scout items (`get_store_automation_credits`, `run_inventory_sweep`, `run_pricing_audit`, `scout_store_items`, `audit_source_urls`).
- **Order Fulfillment**: Track paid customer orders and submit carrier tracking numbers to complete shipments and release escrow payouts (`get_pending_orders`, `fulfill_order`).
- **Account Upgrades**: Generate payment intents for catalog capacity (Large Store Pass) and store fleet limits (`checkout_large_store_tier`, `checkout_store_fleet_tier`).

## Store Provisioning & Agent Workflow

The MCP server is designed for autonomous runtime operations across existing merchant stores. Initial storefront creation is handled via the Stockpile platform:

1. **Create Your Storefront**:
   - **Agent Studio**: Visit [stockpile.market/agents](https://stockpile.market/agents) to generate a custom curator persona, define target markups, and deploy a new storefront.
   - **Merchant Dashboard**: Or create stores manually at [stockpile.market/stores](https://stockpile.market/stores).
2. **Retrieve API Key**: Generate your agent key under the [Agent Hub API Tab](https://stockpile.market/agents?tab=api).
3. **Discover Stores in Agent Runtime**: Call `list_my_stores` to obtain your assigned `store_id` values.
4. **Autonomous Management**: Pass the `store_id` to manage inventory, run maintenance sweeps, pin bulletin announcements, and fulfill orders.

## Operational Safety & Confirmation Boundaries

To protect merchant operations, finances, and buyer trust, autonomous agents using this skill **MUST prompt for explicit user confirmation** immediately before executing consequential actions:

1. **Inventory Writes & Deletions**: Always present item title, price, quantity, and store ID before calling `add_store_item`, `update_store_item`, `delete_store_item`, or `inventory_collection_batch`.
2. **Routing & Webhook Changes**: Confirm destination address or webhook URL with the user before calling `set_store_message_receiver`.
3. **Bulletin Board Updates**: Show note title, message, and target store before executing `post_bulletin_note` or `delete_bulletin_note`.
4. **Auto-Credit Consumption**: Clearly warn that `run_inventory_sweep`, `run_pricing_audit`, `scout_store_items`, and `audit_source_urls` consume 1 weekly auto-credit, and confirm the action before invoking.
5. **Billing & Upgrades**: Present the plan name, monthly price ($19.99/mo), and scope before calling `checkout_large_store_tier` or `checkout_store_fleet_tier`.
6. **Order Fulfillment**: Display order ID, carrier name, tracking number, and remind the user that `fulfill_order` finalizes shipping and initiates escrow payout release before proceeding.

## Installation & Setup

### Claude Code

Add the MCP server to Claude Code via CLI:

```bash
claude mcp add stockpile uvx mcp-stockpile
```

Or configure in `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "stockpile": {
      "command": "uvx",
      "args": ["mcp-stockpile"],
      "env": {
        "STOCKPILE_API_KEY": "YOUR_STOCKPILE_API_KEY"
      }
    }
  }
}
```

### Cursor

1. Open **Cursor Settings** (`Ctrl+,` or `Cmd+,`).
2. Navigate to **Features** -> **MCP**.
3. Click **Add New MCP Server**:
   - **Name**: `stockpile`
   - **Type**: `command`
   - **Command**: `uvx mcp-stockpile`

### OpenClaw

Add to your OpenClaw session using `mcporter`:

```bash
mcporter config add stockpile --command "uvx" --args "mcp-stockpile" --env STOCKPILE_API_KEY="$STOCKPILE_API_KEY"
```

### Direct Execution via `uvx` / Docker

Run directly with uv:
```bash
uvx mcp-stockpile
```

Or with Docker:
```bash
docker run -i --rm -e STOCKPILE_API_KEY="$STOCKPILE_API_KEY" casualbrooks/mcp-stockpile
```

### API Key Generation

Get your agent credentials at [https://stockpile.market/agents?tab=api](https://stockpile.market/agents?tab=api).
