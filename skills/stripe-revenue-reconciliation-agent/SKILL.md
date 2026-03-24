---
name: "Stripe Revenue Reconciliation Agent"
description: "Uses the Stripe API to pull charge, refund, dispute, and payout records within a configurable date window and reconciles them against expected revenue figures. Flags mismatches, duplicate charges, and unmatched refunds, outputting a CSV report with Stripe object IDs."
category: "Integrations & Connectors"
framework: "Codex"
verification: listed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/stripe-revenue-reconciliation-agent/"
tool_ecosystem:
  tool: "stripe"
  github_stars: 4377
  npm_weekly_downloads: 8442269
  github_repo: "stripe/stripe-node"
  license: "MIT"
  maintained: true
---

# Stripe Revenue Reconciliation Agent

Uses the Stripe API to pull charge, refund, dispute, and payout records within a configurable date window and reconciles them against expected revenue figures. Flags mismatches, duplicate charges, and unmatched refunds, outputting a CSV report with Stripe object IDs.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill stripe-revenue-reconciliation-agent
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill stripe-revenue-reconciliation-agent -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill stripe-revenue-reconciliation-agent -a cursor
```

### OpenClaw
```bash
clawhub install stripe-revenue-reconciliation-agent
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill stripe-revenue-reconciliation-agent -a codex
```

## Details

| | |
|---|---|
| **Category** | Integrations & Connectors |
| **Framework** | Codex |
| **Verification** | 📋 Listed |
| **Tool** | [stripe](https://github.com/stripe/stripe-node) — ⭐ 4.4k · MIT |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-revenue-reconciliation-agent/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
