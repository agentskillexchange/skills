---
title: "Connect accounting agents to Xero through MCP"
description: "Use Xero MCP Server to give approved MCP clients controlled access to Xero accounting data, reports, invoices, contacts, and related business records."
verification: "security_reviewed"
source: "https://github.com/XeroAPI/xero-mcp-server"
author: "XeroAPI"
publisher_type: "vendor_open_source"
category:
  - "Integrations & Connectors"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "XeroAPI/xero-mcp-server"
  github_stars: 294
  npm_package: "@xeroapi/xero-mcp-server"
  npm_weekly_downloads: 7989
---

# Connect accounting agents to Xero through MCP

Use Xero MCP Server to give approved MCP clients controlled access to Xero accounting data, reports, invoices, contacts, and related business records.

## Prerequisites

Node.js 18+, npm or pnpm, Xero developer account, Xero client credentials or bearer token, MCP-compatible client

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Add the server to an MCP client using npx -y @xeroapi/xero-mcp-server@latest, then set XERO_CLIENT_ID and XERO_CLIENT_SECRET with required scopes or provide XERO_CLIENT_BEARER_TOKEN for bearer-token mode.
```

## Documentation

- https://github.com/XeroAPI/xero-mcp-server

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/connect-accounting-agents-to-xero-through-mcp/)
