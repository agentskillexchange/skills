---
name: "WordPress Interactivity API State Manager"
description: "Builds reactive front-end interactions for WordPress themes and plugins using the Interactivity API (wp-interactivity). Manages client-side state with wp-data directives, wp-bind attributes, and wp-on event handlers without requiring React or a build step."
category: "WordPress & CMS"
framework: "OpenClaw"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/wordpress-interactivity-api-state-manager/"
---

# WordPress Interactivity API State Manager

Builds reactive front-end interactions for WordPress themes and plugins using the Interactivity API (wp-interactivity). Manages client-side state with wp-data directives, wp-bind attributes, and wp-on event handlers without requiring React or a build step.

## Overview

Overview

The WordPress Interactivity API State Manager skill helps agents create reactive, JavaScript-driven interactions inside WordPress blocks and templates using the Interactivity API introduced in WordPress 6.5. This API provides a declarative, Alpine.js-style approach to client-side interactivity through HTML directives like `data-wp-interactive`, `data-wp-bind`, `data-wp-on`, `data-wp-text`, and `data-wp-context`, eliminating the need for React, a bundler, or `wp-scripts build`.

How It Works

The agent scaffolds an interactive block or template partial by adding the `data-wp-interactive="myNamespace"` directive to the root element. It defines the store using `wp_interactivity_state()` in PHP for server-side initial values and `store()` in a view.js module for client-side actions and callbacks. State mutations trigger automatic DOM updates through the reactive system — no manual querySelector or innerHTML manipulation required. The skill handles common patterns including toggle visibility, fetch-on-click with `wp.apiFetch`, infinite scroll pagination, and form validation with real-time feedback.

Technical Details

Registers the view script as a module via `wp_register_script_module()` with `@wordpress/interactivity` as a dependency. Supports nested contexts for component-scoped state, derived state via `getContext()`, and async actions for REST API calls. Generates clean, progressively-enhanced HTML that works without JavaScript as a baseline. The output passes WordPress Coding Standards for both PHP and JavaScript, and includes inline JSDoc type annotations for the store definition. Compatible with WordPress 6.5+ and all modern browsers.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill wordpress-interactivity-api-state-manager
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill wordpress-interactivity-api-state-manager -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill wordpress-interactivity-api-state-manager -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill wordpress-interactivity-api-state-manager -a codex
```

### OpenClaw

```bash
clawhub install wordpress-interactivity-api-state-manager
```

## Source

- Marketplace: https://agentskillexchange.com/skills/wordpress-interactivity-api-state-manager/
