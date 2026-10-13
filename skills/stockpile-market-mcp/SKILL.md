---
name: "Stockpile Market MCP"
slug: "stockpile-market-mcp"
description: "Autonomous e-commerce storefront operations, marketplace catalog curation, collectible appraisals, and order fulfillment via Stockpile MCP."
category: "Integrations & Connectors"
framework: "Multi-Framework"
verification: listed
source: "https://github.com/casualbrooks/mcp-stockpile"
---

# Stockpile Market MCP

Autonomous e-commerce storefront operations, market catalog discovery, collectible item appraisals, inventory tracking, and order fulfillment via the [Stockpile Market](https://stockpile.market) Model Context Protocol (MCP) server.

Provides 23 tools for autonomous agents operating across Claude Code, Cursor, OpenClaw, Codex, and OpenAI ecosystems:
- **Catalog Discovery**: Search public marketplace listings, categories, and item provenance.
- **Storefront Management**: Create and configure custom merchant stores and policies.
- **Inventory Control**: List, modify, grade, and delist inventory with photographic evidence.
- **Appraisals**: Automated market valuations based on recent comp sales and condition grades.
- **Fulfillment**: Manage orders, verify buyer details, submit tracking carriers, and handle refunds.
- **Content Moderation**: Built-in compliance checks preventing listing of prohibited substances or illegal services.

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

Get your agent credentials at [https://stockpile.market/agent-hub](https://stockpile.market/agent-hub).
