---
title: "Stripe Connect Account Provisioner"
description: "Automates Stripe Connect onboarding by provisioning connected accounts via the Stripe API. Handles account creation, KYC link generation with stripe.accountLinks.create(), and webhook verification for account.updated events."
verification: "security_reviewed"
source: "https://github.com/stripe/stripe-node"
author: "Stripe"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "stripe/stripe-node"
  github_stars: 4385
  npm_package: "stripe"
  npm_weekly_downloads: 9280426
---

# Stripe Connect Account Provisioner

Automates Stripe Connect onboarding by provisioning connected accounts via the Stripe API. Handles account creation, KYC link generation with stripe.accountLinks.create(), and webhook verification for account.updated events.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Documentation

- https://docs.stripe.com/connect

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stripe-connect-account-provisioner/)
