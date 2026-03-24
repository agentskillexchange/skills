---
name: "Stripe Revenue Reconciliation Agent"
description: "Uses the Stripe API to pull charge, refund, dispute, and payout records within a configurable date window and reconciles them against expected revenue figures. Flags mismatches, duplicate charges, and unmatched refunds, outputting a CSV report with Stripe object IDs."
category: "Integrations & Connectors"
framework: "Codex"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/stripe-revenue-reconciliation-agent/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "stripe"  # from ase_tool_match
  github_stars: 4377  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 8442269  # from ase_npm_downloads
  github_repo: "stripe/stripe-node"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Stripe Revenue Reconciliation Agent

Uses the Stripe API to pull charge, refund, dispute, and payout records within a configurable date window and reconciles them against expected revenue figures. Flags mismatches, duplicate charges, and unmatched refunds, outputting a CSV report with Stripe object IDs.

## Overview

Uses the Stripe API to pull charge, refund, dispute, and payout records within a configurable date window and reconciles them against expected revenue figures. Flags mismatches, duplicate charges, and unmatched refunds, outputting a CSV report with Stripe object IDs.

## Installation

### Any Agent

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

### Codex

```bash
npx skills add agentskillexchange/skills --skill stripe-revenue-reconciliation-agent -a codex
```

### OpenClaw

```bash
clawhub install stripe-revenue-reconciliation-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/stripe-revenue-reconciliation-agent/
