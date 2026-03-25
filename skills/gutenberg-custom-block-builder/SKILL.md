---
name: "Gutenberg Custom Block Builder"
description: "Scaffolds and builds custom Gutenberg blocks using @wordpress/create-block and the Block API registerBlockType(). Generates edit/save components with InspectorControls, RichText, and InnerBlocks support."
category: "WordPress & CMS"
framework: "ChatGPT Agents"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/gutenberg-custom-block-builder/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "wordpress"  # from ase_tool_match
  github_stars: 20973  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 44849699  # from ase_npm_downloads
  github_repo: "WordPress/WordPress"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Gutenberg Custom Block Builder

Scaffolds and builds custom Gutenberg blocks using @wordpress/create-block and the Block API registerBlockType(). Generates edit/save components with InspectorControls, RichText, and InnerBlocks support.

## Overview

This skill streamlines custom Gutenberg block development using the official @wordpress/create-block scaffolding tool and the WordPress Block API. It generates complete block plugins with registerBlockType() configuration, edit and save components, and block.json metadata following WordPress coding standards.

Block editor components leverage InspectorControls for sidebar settings panels, RichText for inline content editing, InnerBlocks for nested block support, and MediaUpload for image/video selection. The skill handles both static and dynamic blocks, with PHP render_callback functions for server-side rendering when blocks need fresh data.

Build tooling uses @wordpress/scripts for webpack configuration, hot module replacement during development, and production-optimized builds. The skill includes patterns for block variations, block styles, block transforms, and deprecated versions for backward compatibility when block markup changes.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill gutenberg-custom-block-builder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill gutenberg-custom-block-builder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill gutenberg-custom-block-builder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill gutenberg-custom-block-builder -a codex
```

### OpenClaw

```bash
clawhub install gutenberg-custom-block-builder
```

## Source

- Marketplace: https://agentskillexchange.com/skills/gutenberg-custom-block-builder/
