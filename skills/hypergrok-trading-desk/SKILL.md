---
name: "HyperGrok Trading Desk"
slug: "hypergrok-trading-desk"
description: "Turn Claude Code, Cursor, or Grok Bot into a 7-role Hyperliquid trading desk. Sixteen SKILL.md skills plus seven agent prompts cover market data, risk limits, ticketed execution, and post-trade review. You approve every trade by ticket id. Trade-only API wallet; no withdraw."
category: "Integrations & Connectors"
framework: "Multi-Framework"
verification: listed
source: "https://github.com/galleonlabs/hypergrok-trading-desk"
github_stars: 2
tool_ecosystem:
  github_repo: "galleonlabs/hypergrok-trading-desk"
  github_stars: 2
  license: "MIT"
  maintained: true
---

# HyperGrok Trading Desk

HyperGrok is an open-source Agent Plugin that turns an agent workspace into a seven-role Hyperliquid trading desk. It ships sixteen portable `SKILL.md` skills and seven role prompts. The desk is documentation and instructions, not a hosted bot.

Use this skill when you want research, risk, ticketed execution, and review as separate seats on Hyperliquid perpetual markets.

## What it includes

**Roles:** Desk Lead, Market Analyst, Research Analyst, Strategist, Risk Manager, Execution Trader, Trade Reviewer.

**Hyperliquid skills:** API wallet setup, market data, account state, orders (limit, IOC, take-profit, stop-loss, grouping, client order ids), positions and margin, WebSocket feeds, advanced actions (dead-man's switch, TWAP, spot), and a compact API reference.

**Desk skills:** operating model, trade lifecycle and ticket, risk limits and sizing, execution protocol, monitoring, post-trade review, incident playbooks, and the strategy lab.

Every trade follows the same path: idea → evidence → risk sign-off → your approval by ticket id → one send → reconciliation → review. A trade-only API wallet is the only key the desk holds. It can trade; it cannot withdraw. Testnet first.

## Installation

### Direct repo

```bash
npx skills add galleonlabs/hypergrok-trading-desk
```

### Claude Code marketplace

```bash
claude plugin marketplace add galleonlabs/hypergrok-trading-desk
claude plugin install hypergrok@hypergrok
```

### Hermes

```bash
hermes plugins install galleonlabs/hypergrok-trading-desk
```

### OpenClaw / ClawHub

Skills are published under the `galleonlabs` publisher as `hypergrok-*` slugs (for example `hypergrok-desk-operating-model`).

### Grok Bot

Paste the setup prompt from the upstream README: follow `SETUP.md` to create the seven Bots and the Trading Floor group chat.

## Source

- Upstream: https://github.com/galleonlabs/hypergrok-trading-desk
- Homepage: https://galleonlabs.io
- License: MIT
- Agent Plugins 1.0.0 `plugin.json` at repo root
