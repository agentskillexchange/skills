---
name: "HyperGrok Trading Desk"
slug: "hypergrok-trading-desk"
description: "Turn Claude Code, Cursor, or Grok Bot into a 7-role Hyperliquid trading desk. Sixteen SKILL.md skills plus seven agent prompts cover market data, risk limits, ticketed execution, and post-trade review. You approve every trade by ticket id. Trade-only API wallet; no withdraw."
github_stars: 39
verification: "listed"
source: "https://github.com/galleonlabs/hypergrok-trading-desk"
author: "galleonlabs"
category: "Integrations & Connectors"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "galleonlabs/hypergrok-trading-desk"
  github_stars: 39
  npm_package: "hypergrok-trading-desk"
  npm_weekly_downloads: 272
---

# HyperGrok Trading Desk

HyperGrok is an open-source Agent Plugin that turns an agent workspace into a seven-role Hyperliquid trading desk. It ships seventeen portable `SKILL.md` skills and seven role prompts. The desk is documentation and instructions, not a hosted bot.

Use this skill when you want research, risk, ticketed execution, and review as separate seats on Hyperliquid perpetual markets.

**Roles:** Desk Lead, Market Analyst, Research Analyst, Strategist, Risk Manager, Execution Trader, Trade Reviewer.

**Hyperliquid skills:** API wallet setup, market data, account state, orders (limit, IOC, take-profit, stop-loss, grouping, client order ids), positions and margin, WebSocket feeds, advanced actions (dead-man's switch, TWAP, spot), and a compact API reference.

**Bootstrap:** pinned release install, zero-key Opening Bell, native role and skill readback, desk doctor, and an evidence receipt.

**Desk skills:** operating model, trade lifecycle and ticket, risk limits and sizing, execution protocol, monitoring, post-trade review, incident playbooks, and the strategy lab.

Every trade follows the same path: idea → evidence → risk sign-off → your approval by ticket id → one send → reconciliation → review. A trade-only API wallet is the only key the desk holds. It can trade; it cannot withdraw. Testnet first. Native approval coverage, Risk PASS, an unexpired exact ticket and single-send reconciliation are required before any exchange write. If native coverage cannot be verified, keep the desk research-only and provision no API key.

## Financial risk boundary

HyperGrok is documentation and instructions, not financial advice. Perpetual futures can liquidate an account. Use testnet first, keep explicit risk limits, and require human approval before any mainnet order.

## Installation

Install or set up from the source-backed instructions:

git clone --depth 1 --branch v1.7.0 https://github.com/galleonlabs/hypergrok-trading-desk.git
cd hypergrok-trading-desk
python3 scripts/opening_bell.py --coin ETH
Follow SETUP.md to configure the agent desk.

- Source: https://github.com/galleonlabs/hypergrok-trading-desk

## Source

- Upstream: https://github.com/galleonlabs/hypergrok-trading-desk
- Homepage: https://galleonlabs.io
- License: MIT
- Reviewed release: [v1.7.0](https://github.com/galleonlabs/hypergrok-trading-desk/releases/tag/v1.7.0)
- Agent Plugins 1.0.0 schema in `plugin.json` at repo root
