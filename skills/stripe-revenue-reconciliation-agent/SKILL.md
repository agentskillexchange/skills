---
title: "Stripe Revenue Reconciliation Agent"
slug: "stripe-revenue-reconciliation-agent"
description: "Uses the Stripe API to pull charge, refund, dispute, and payout records within a configurable date window and reconciles them against expected revenue figures. Flags mismatches, duplicate charges, and unmatched refunds, outputting a CSV report with Stripe object IDs."
verification: security_reviewed
source: "https://github.com/stripe/stripe-node"
category:
  - "Integrations &amp; Connectors"
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

1. Clone this skill into your local skills directory.
2. Review the required tools and environment variables.
3. Install dependencies with your preferred package manager or runtime.
4. Run the upstream install command from the project documentation, if needed.
5. Validate the installation and test the skill in your agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-revenue-reconciliation-agent/)
