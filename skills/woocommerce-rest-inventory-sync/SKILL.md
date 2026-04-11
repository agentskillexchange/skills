---
title: "WooCommerce REST Inventory Sync"
description: "Synchronizes WooCommerce product inventory across multiple channels using the WooCommerce REST API v3 and wp_update_post hooks. Handles stock level reconciliation, low-stock alerts via WP-CLI, and batch product updates through the /wc/v3/products/batch endpoint."
verification: "security_reviewed"
source: "https://github.com/woocommerce/woocommerce"
category:
  - "WordPress &amp; CMS"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "woocommerce/woocommerce"
  github_stars: 10243
---

# WooCommerce REST Inventory Sync

Synchronizes WooCommerce product inventory across multiple channels using the WooCommerce REST API v3 and wp_update_post hooks. Handles stock level reconciliation, low-stock alerts via WP-CLI, and batch product updates through the /wc/v3/products/batch endpoint.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/woocommerce-rest-inventory-sync/)
