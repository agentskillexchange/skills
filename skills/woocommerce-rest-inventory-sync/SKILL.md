---
name: "WooCommerce REST Inventory Sync"
category: "WordPress & CMS"
verification: "security_reviewed"
source: "https://github.com/woocommerce/woocommerce"
tool_ecosystem:
  github_repo: "woocommerce/woocommerce"
  github_stars: 10233
---

# WooCommerce REST Inventory Sync

Synchronizes WooCommerce product inventory across multiple channels using the WooCommerce REST API v3 and wp_update_post hooks. Handles stock level reconciliation, low-stock alerts via WP-CLI, and batch product updates through the /wc/v3/products/batch endpoint.

## Installation

Install this skill using one of the following methods:

```bash
# ClawHub CLI
clawhub install woocommerce-rest-inventory-sync

# OpenClaw CLI
openclaw skills install woocommerce-rest-inventory-sync

# Chat command
/skill install woocommerce-rest-inventory-sync

# Direct download
curl -L https://agentskillexchange.com/skills/woocommerce-rest-inventory-sync/download -o woocommerce-rest-inventory-sync.zip

# Git clone this repo and copy the skill folder
cp -r skills/woocommerce-rest-inventory-sync ~/.openclaw/workspace/skills/
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/woocommerce-rest-inventory-sync/)
