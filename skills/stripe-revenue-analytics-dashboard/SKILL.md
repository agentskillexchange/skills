---
name: "Stripe Revenue Analytics Dashboard Builder"
slug: "stripe-revenue-analytics-dashboard"
description: "Pulls MRR, churn, and LTV metrics from the Stripe Data API using the stripe Node.js SDK and transforms the data using Apache Arrow. Aggregated metrics are pushed to a Metabase dashboard via the Metabase API and refreshed nightly using a cron-triggered Lambda function."
github_stars: 4385
verification: "security_reviewed"
source: "https://github.com/stripe/stripe-node"
category: "Data Extraction & Transformation"
framework: "MCP"
tool_ecosystem:
  github_repo: "stripe/stripe-node"
  github_stars: 4385
  npm_package: "stripe"
  npm_weekly_downloads: 9280426
---

# Stripe Revenue Analytics Dashboard Builder

Pulls MRR, churn, and LTV metrics from the Stripe Data API using the stripe Node.js SDK and transforms the data using Apache Arrow. Aggregated metrics are pushed to a Metabase dashboard via the Metabase API and refreshed nightly using a cron-triggered Lambda function.

## Installation

Use the upstream install or setup path that matches your environment:
- npm install stripe
- yarn add stripe
- npm install stripe@public-preview --save-exact
- npm install stripe@<some-version>

Requirements and caveats from upstream:
- # Stripe Node.js Library
- [![Build Status](https://github.com/stripe/stripe-node/actions/workflows/main.yml/badge.svg?branch=master)](https://github.com/stripe/stripe-node/actions?query=branch%3Amaster)
- Want to chat live with Stripe engineers? Join us on our [Discord server](https://stripe.com/go/discord/node).

Basic usage or getting-started notes:
- sh
- # or
- The package needs to be configured with your account's secret key, which is

- Source: https://github.com/stripe/stripe-node
- Extracted from upstream docs: https://raw.githubusercontent.com/stripe/stripe-node/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-revenue-analytics-dashboard/)
