---
title: "Stripe Revenue Reconciliation Agent"
description: "Uses the Stripe API to pull charge, refund, dispute, and payout records within a configurable date window and reconciles them against expected revenue figures. Flags mismatches, duplicate charges, and unmatched refunds, outputting a CSV report with Stripe object IDs."
verification: security_reviewed
source: "https://github.com/stripe/stripe-node"
category:
  - "Integrations & Connectors"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "stripe/stripe-node"
  github_stars: 4385
  npm_package: "stripe"
  npm_weekly_downloads: 9280426
---

# Stripe Revenue Reconciliation Agent

Uses the Stripe API to pull charge, refund, dispute, and payout records within a configurable date window and reconciles them against expected revenue figures. Flags mismatches, duplicate charges, and unmatched refunds, outputting a CSV report with Stripe object IDs.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/stripe-revenue-reconciliation-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/stripe-revenue-reconciliation-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/stripe-revenue-reconciliation-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-revenue-reconciliation-agent/)
