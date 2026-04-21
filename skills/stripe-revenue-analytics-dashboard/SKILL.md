---
title: "Stripe Revenue Analytics Dashboard Builder"
slug: "stripe-revenue-analytics-dashboard"
description: "Pulls MRR, churn, and LTV metrics from the Stripe Data API using the stripe Node.js SDK and transforms the data using Apache Arrow. Aggregated metrics are pushed to a Metabase dashboard via the Metabase API and refreshed nightly using a cron-triggered Lambda function."
verification: security_reviewed
source: "https://github.com/stripe/stripe-node"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "stripe/stripe-node"
  github_stars: 4385
  npm_package: "stripe"
  npm_weekly_downloads: 9280426
---

# Stripe Revenue Analytics Dashboard Builder

Pulls MRR, churn, and LTV metrics from the Stripe Data API using the stripe Node.js SDK and transforms the data using Apache Arrow. Aggregated metrics are pushed to a Metabase dashboard via the Metabase API and refreshed nightly using a cron-triggered Lambda function.

## Installation

1. Clone this skill into your local skills directory.
2. Review the required tools and environment variables.
3. Install dependencies with your preferred package manager or runtime.
4. Run the upstream install command from the project documentation, if needed.
5. Validate the installation and test the skill in your agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-revenue-analytics-dashboard/)
