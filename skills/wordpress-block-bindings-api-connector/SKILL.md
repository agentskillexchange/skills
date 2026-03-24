---
name: "WordPress Block Bindings API Connector"
description: "Connects WordPress block attributes to dynamic data sources using the Block Bindings API introduced in WordPress 6.5. Integrates with ACF, custom post meta, and WooCommerce product fields to render real-time values inside core blocks without custom PHP templates."
category: "WordPress & CMS"
framework: "Claude Code"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/wordpress-block-bindings-api-connector/"
---

# WordPress Block Bindings API Connector

Connects WordPress block attributes to dynamic data sources using the Block Bindings API introduced in WordPress 6.5. Integrates with ACF, custom post meta, and WooCommerce product fields to render real-time values inside core blocks without custom PHP templates.

## Overview

Overview

The WordPress Block Bindings API Connector skill enables agents to wire block attributes directly to external or internal data sources using the Block Bindings API available since WordPress 6.5. Instead of building custom PHP block render callbacks for every dynamic value, this skill teaches the agent to register binding sources via `register_block_bindings_source()` and map them to core block attributes like paragraph content, image src, or heading text.

How It Works

The agent inspects the target block’s `block.json` metadata to identify bindable attributes, then generates a PHP source registration that fetches data from the specified provider — whether that is `get_post_meta()`, an ACF field group, a WooCommerce product attribute, or a REST API response cached via the Transients API. The binding source callback receives the block instance context and returns the resolved value, which WordPress injects at render time without any client-side JavaScript.

Technical Details

Supports binding to core/paragraph, core/heading, core/image, and core/button blocks. Handles attribute type coercion, escaping with `esc_html()` and `esc_url()`, and fallback values when the data source returns empty. The skill generates PHPUnit tests using `WP_UnitTestCase` to verify binding resolution and registers the source in a `mu-plugin` or the theme’s `functions.php`. Compatible with WordPress 6.5+ and PHP 8.0+. Outputs clean, WordPress Coding Standards-compliant code that passes `phpcs` with the WordPress ruleset.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill wordpress-block-bindings-api-connector
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill wordpress-block-bindings-api-connector -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill wordpress-block-bindings-api-connector -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill wordpress-block-bindings-api-connector -a codex
```

### OpenClaw

```bash
clawhub install wordpress-block-bindings-api-connector
```

## Source

- Marketplace: https://agentskillexchange.com/skills/wordpress-block-bindings-api-connector/
