---
name: "WooCommerce REST Inventory Sync"
slug: "woocommerce-rest-inventory-sync"
description: "Synchronizes WooCommerce product inventory across multiple channels using the WooCommerce REST API v3 and wp_update_post hooks. Handles stock level reconciliation, low-stock alerts via WP-CLI, and batch product updates through the /wc/v3/products/batch endpoint."
github_stars: 10243
verification: "listed"
source: "https://github.com/woocommerce/woocommerce"
author: "woocommerce"
category: "WordPress & CMS"
framework: "OpenClaw"
tool_ecosystem:
  github_repo: "woocommerce/woocommerce"
  github_stars: 10243
---

# WooCommerce REST Inventory Sync

Synchronizes WooCommerce product inventory across multiple channels using the WooCommerce REST API v3 and wp_update_post hooks. Handles stock level reconciliation, low-stock alerts via WP-CLI, and batch product updates through the /wc/v3/products/batch endpoint.

## Installation

Use the upstream install or setup path that matches your environment:
- pnpm install -frozen-lockfile
- pnpm build

Requirements and caveats from upstream:
- To get up and running within the WooCommerce Monorepo, you will need to make sure that you have installed all of the prerequisites.
- [NVM](https://github.com/nvm-sh/nvm#installing-and-updating): While you can always install Node through other means, we recommend using NVM to ensure you're aligned with the version used by our development teams. Our...
- [PHP 7.4+](https://www.php.net/manual/en/install.php): WooCommerce Core currently requires PHP version 7.4 or higher. It is also needed to run Composer and various project build scripts. See [troubleshooting](DEVELOPM...

Basic usage or getting-started notes:
- [PNPM](https://pnpm.io/installation): Our repository utilizes PNPM to manage project dependencies and run various scripts involved in building and testing projects.
- [Composer](https://getcomposer.org/doc/00-intro.md): We use Composer to manage all of the dependencies for PHP packages and plugins.
- Note: A POSIX-compliant operating system (e.g., Linux, macOS) is assumed. If you're working on a Windows machine, the recommended approach is to use [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) (availa...

- Source: https://github.com/woocommerce/woocommerce
- Extracted from upstream docs: https://raw.githubusercontent.com/woocommerce/woocommerce/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/woocommerce-rest-inventory-sync/)
