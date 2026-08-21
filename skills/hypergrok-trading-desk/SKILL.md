---
name: "HyperGrok Trading Desk"
slug: "hypergrok-trading-desk"
description: "Turn Claude Code, Cursor, or Grok Bot into a 7-role Hyperliquid trading desk. Sixteen SKILL.md skills plus seven agent prompts cover market data, risk limits, ticketed execution, and post-trade review. You approve every trade by ticket id. Trade-only API wallet; no withdraw."
category: "Integrations & Connectors"
framework: "Multi-Framework"
verification: listed
source: "https://github.com/galleonlabs/hypergrok-trading-desk"
tool_ecosystem:
  github_repo: "galleonlabs/hypergrok-trading-desk"
  license: "MIT"
  maintained: true
---

# HyperGrok Trading Desk

HyperGrok is an open-source Agent Plugin that turns an agent workspace into a seven-role Hyperliquid trading desk. It ships sixteen portable `SKILL.md` skills and seven role prompts. The desk is documentation and instructions, not a hosted bot.

Use this skill when you want research, risk, ticketed execution, and review as separate seats on Hyperliquid perpetual markets.

**Roles:** Desk Lead, Market Analyst, Research Analyst, Strategist, Risk Manager, Execution Trader, Trade Reviewer.

**Hyperliquid skills:** API wallet setup, market data, account state, orders (limit, IOC, take-profit, stop-loss, grouping, client order ids), positions and margin, WebSocket feeds, advanced actions (dead-man's switch, TWAP, spot), and a compact API reference.

**Desk skills:** operating model, trade lifecycle and ticket, risk limits and sizing, execution protocol, monitoring, post-trade review, incident playbooks, and the strategy lab.

Every trade follows the same path: idea → evidence → risk sign-off → your approval by ticket id → one send → reconciliation → review. A trade-only API wallet is the only key the desk holds. It can trade; it cannot withdraw. Testnet first.

## Financial risk boundary

HyperGrok is documentation and instructions, not financial advice. Perpetual futures can liquidate an account. Use testnet first, keep explicit risk limits, and require human approval before any mainnet order.

## Installation

### OpenClaw

```bash
clawhub install hypergrok-trading-desk
```

### Direct repo/manual install

Clone the Agent Skill Exchange repository and copy this skill directory into the skill folder used by your agent runtime:

```bash
git clone https://github.com/agentskillexchange/skills.git
cp -R skills/skills/hypergrok-trading-desk ~/.agent-skills/hypergrok-trading-desk
```

The full sixteen-skill desk also lives upstream:

```bash
git clone https://github.com/galleonlabs/hypergrok-trading-desk.git
```

### Optional Third-Party Installer

The `skills` npm package is maintained by Vercel Labs / third parties, not AgentSkillExchange. If you choose to use it, pin the package version:

```bash
npm exec --package=skills@1.5.23 -- skills add agentskillexchange/skills --skill hypergrok-trading-desk
```

Upstream pack install:

```bash
npm exec --package=skills@1.5.23 -- skills add galleonlabs/hypergrok-trading-desk
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

### Grok Bot

Paste the setup prompt from the upstream README: follow `SETUP.md` to create the seven Bots and the Trading Floor group chat.

## Source

- Upstream: https://github.com/galleonlabs/hypergrok-trading-desk
- Homepage: https://galleonlabs.io
- License: MIT
- Agent Plugins 1.0.0 `plugin.json` at repo root
