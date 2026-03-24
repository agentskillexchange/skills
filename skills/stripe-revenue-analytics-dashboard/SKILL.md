---
name: "Stripe Revenue Analytics Dashboard Builder"
description: "Pulls MRR, churn, and LTV metrics from the Stripe Data API using the stripe Node.js SDK and transforms the data using Apache Arrow. Aggregated metrics are pushed to a Metabase dashboard via the Metabase API and refreshed nightly using a cron-triggered Lambda function."
category: "Data Extraction & Transformation"
framework: "MCP-compatible"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/stripe-revenue-analytics-dashboard/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "stripe"  # from ase_tool_match
  github_stars: 4377  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 8442269  # from ase_npm_downloads
  github_repo: "stripe/stripe-node"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Stripe Revenue Analytics Dashboard Builder

Pulls MRR, churn, and LTV metrics from the Stripe Data API using the stripe Node.js SDK and transforms the data using Apache Arrow. Aggregated metrics are pushed to a Metabase dashboard via the Metabase API and refreshed nightly using a cron-triggered Lambda function.

## Overview

Pulls MRR, churn, and LTV metrics from the Stripe Data API using the stripe Node.js SDK and transforms the data using Apache Arrow. Aggregated metrics are pushed to a Metabase dashboard via the Metabase API and refreshed nightly using a cron-triggered Lambda function.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill stripe-revenue-analytics-dashboard
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill stripe-revenue-analytics-dashboard -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill stripe-revenue-analytics-dashboard -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill stripe-revenue-analytics-dashboard -a codex
```

### OpenClaw

```bash
clawhub install stripe-revenue-analytics-dashboard
```

## Source

- Marketplace: https://agentskillexchange.com/skills/stripe-revenue-analytics-dashboard/
