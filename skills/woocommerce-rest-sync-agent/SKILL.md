---
name: "WooCommerce REST Sync Agent"
description: "Synchronizes WooCommerce product data bidirectionally using the WC REST API v3 and wc/v3/products endpoints. Handles batch create/update/delete with OAuth 1.0a authentication and rate-limit backoff."
category: "WordPress & CMS"
framework: "Codex"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/woocommerce-rest-sync-agent/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "sqlite"  # from ase_tool_match
  github_stars: 7041  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 4960915  # from ase_npm_downloads
  github_repo: "WiseLibs/better-sqlite3"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# WooCommerce REST Sync Agent

Synchronizes WooCommerce product data bidirectionally using the WC REST API v3 and wc/v3/products endpoints. Handles batch create/update/delete with OAuth 1.0a authentication and rate-limit backoff.

## Overview

WooCommerce REST Sync Agent manages bidirectional product synchronization between WooCommerce stores or between WooCommerce and external inventory systems. It communicates via the official WC REST API v3, authenticating with OAuth 1.0a consumer key/secret pairs.

The agent uses the `/wc/v3/products/batch` endpoint to process up to 100 products per request, handling create, update, and delete operations atomically. It tracks sync state using product meta fields and SKU matching, resolving conflicts with configurable last-write-wins or source-priority strategies.

Supports complex product types including variable products with attributes and variations via `/wc/v3/products/{id}/variations`, grouped products, and external/affiliate products. Handles product images by URL with `wp_handle_sideload()`, categories via `/wc/v3/products/categories`, and tags. Implements exponential backoff on 429 rate-limit responses and maintains a local SQLite journal for crash recovery.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill woocommerce-rest-sync-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill woocommerce-rest-sync-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill woocommerce-rest-sync-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill woocommerce-rest-sync-agent -a codex
```

### OpenClaw

```bash
clawhub install woocommerce-rest-sync-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/woocommerce-rest-sync-agent/
