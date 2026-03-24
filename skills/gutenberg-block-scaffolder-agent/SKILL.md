---
name: "Gutenberg Block Scaffolder"
description: "Generates custom Gutenberg blocks using @wordpress/create-block and the Block API v3 schema. Produces edit.js, save.js, block.json, and render.php with InnerBlocks support and block.json viewScriptModule."
category: "WordPress & CMS"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/gutenberg-block-scaffolder-agent/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "wordpress"  # from ase_tool_match
  github_stars: 20973  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 44849699  # from ase_npm_downloads
  github_repo: "WordPress/WordPress"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Gutenberg Block Scaffolder

Generates custom Gutenberg blocks using @wordpress/create-block and the Block API v3 schema. Produces edit.js, save.js, block.json, and render.php with InnerBlocks support and block.json viewScriptModule.

## Overview

Gutenberg Block Scaffolder automates the creation of WordPress editor blocks following the Block API v3 specification. It uses the `@wordpress/create-block` scaffold tool as a foundation, then customizes output based on your requirements.

The agent generates complete block packages including `block.json` metadata with apiVersion 3, `edit.js` with `useBlockProps` and `InspectorControls`, `save.js` with proper serialization, and optional `render.php` for dynamic server-side rendering. It supports `InnerBlocks` with `allowedBlocks` and template locking, custom `BlockControls` toolbars, and the new `viewScriptModule` field for frontend interactivity.

Integrates with `@wordpress/scripts` for build configuration, generates proper `webpack.config.js` overrides when needed, and produces PHPUnit test stubs for `render_callback` functions. Supports block variations, block styles, and block patterns registration via `register_block_pattern()`.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill gutenberg-block-scaffolder-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill gutenberg-block-scaffolder-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill gutenberg-block-scaffolder-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill gutenberg-block-scaffolder-agent -a codex
```

### OpenClaw

```bash
clawhub install gutenberg-block-scaffolder-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/gutenberg-block-scaffolder-agent/
