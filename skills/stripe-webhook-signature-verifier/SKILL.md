---
name: "Stripe Webhook Signature Verifier"
slug: "stripe-webhook-signature-verifier"
description: "Verifies Stripe webhook payload signatures using the Stripe.js SDK and the stripe.webhooks.constructEvent method. Validates the Stripe-Signature header against the raw request body and a configured endpoint secret. Handles tolerance windows for replay attack prevention and logs verification failures to Datadog via the Datadog Logs API."
github_stars: 4385
verification: "listed"
source: "https://github.com/stripe/stripe-node"
category: "Security & Verification"
framework: "ChatGPT Agents"
tool_ecosystem:
  github_repo: "stripe/stripe-node"
  github_stars: 4385
  npm_package: "stripe"
  npm_weekly_downloads: 9280426
---

# Stripe Webhook Signature Verifier

Verifies Stripe webhook payload signatures using the Stripe.js SDK and the stripe.webhooks.constructEvent method. Validates the Stripe-Signature header against the raw request body and a configured endpoint secret. Handles tolerance windows for replay attack prevention and logs verification failures to Datadog via the Datadog Logs API.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-webhook-signature-verifier/)
