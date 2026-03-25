---
name: "Stripe MCP Server"
description: "Use this skill when you need to query Stripe customers, charges, subscriptions, invoices, or payment intents from your AI agent. It enables agents to look up payment data, issue refunds, create payment links, and investigate failed charges without accessing the Stripe dashboard."
category: "Integrations & Connectors"
framework: "MCP-compatible"
verification: listed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/stripe-mcp-server/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "stripe"  # from ase_tool_match
  github_stars: 4377  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 8442269  # from ase_npm_downloads
  github_repo: "stripe/stripe-node"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Stripe MCP Server

Use this skill when you need to query Stripe customers, charges, subscriptions, invoices, or payment intents from your AI agent. It enables agents to look up payment data, issue refunds, create payment links, and investigate failed charges without accessing the Stripe dashboard.

## Overview

Use this skill when you need to query Stripe customers, charges, subscriptions, invoices, or payment intents from your AI agent. It enables agents to look up payment data, issue refunds, create payment links, and investigate failed charges without accessing the Stripe dashboard.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill stripe-mcp-server
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill stripe-mcp-server -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill stripe-mcp-server -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill stripe-mcp-server -a codex
```

### OpenClaw

```bash
clawhub install stripe-mcp-server
```

## Source

- Marketplace: https://agentskillexchange.com/skills/stripe-mcp-server/
