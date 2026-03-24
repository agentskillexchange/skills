---
name: "Elementor Template Export Mapper"
description: "Maps Elementor export JSON, template parts, widget settings, and site-kit dependencies so teams can understand what a design package actually needs before import. It helps surface asset references, global colors, custom CSS, and plugin-linked widgets that often break migrations."
category: "WordPress & CMS"
framework: "Codex"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/elementor-template-export-mapper-20260324/"
---

# Elementor Template Export Mapper

Maps Elementor export JSON, template parts, widget settings, and site-kit dependencies so teams can understand what a design package actually needs before import. It helps surface asset references, global colors, custom CSS, and plugin-linked widgets that often break migrations.

## Overview

This skill analyzes **Elementor** template exports and turns opaque JSON bundles into a migration or review plan. Elementor layouts often depend on global styles, theme settings, custom CSS, external fonts, form integrations, and third-party widgets that are not obvious from the visual editor alone. The skill parses exported template data, inventories sections, containers, widgets, dynamic tags, and asset references, then highlights any dependencies on plugins, custom post types, menus, or media that must exist on the destination site. That makes it useful for agency handoffs, staging-to-production promotion, theme rebuilds, and site audits before a redesign.

The workflow can emit a dependency matrix, unresolved widget warnings, a list of required plugins, and a normalized asset map for images, icons, and CSS. It also identifies where template logic touches forms, popups, WooCommerce widgets, or custom shortcodes that will need equivalent support after import. Integration points include version-controlled JSON exports, WP-CLI packaging steps, backup routines, and documentation generated for client delivery or QA sign-off. Outputs may be written as Markdown, CSV, or JSON and paired with screenshots or a checklist for manual verification. In practice, this skill reduces the risk of importing a template that looks complete on disk but fails in production because a small dependency chain was never documented.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill elementor-template-export-mapper-20260324
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill elementor-template-export-mapper-20260324 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill elementor-template-export-mapper-20260324 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill elementor-template-export-mapper-20260324 -a codex
```

### OpenClaw

```bash
clawhub install elementor-template-export-mapper-20260324
```

## Source

- Marketplace: https://agentskillexchange.com/skills/elementor-template-export-mapper-20260324/
