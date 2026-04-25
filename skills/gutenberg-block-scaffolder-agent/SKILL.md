---
title: "Gutenberg Block Scaffolder"
description: "Generates custom Gutenberg blocks using @wordpress/create-block and the Block API v3 schema. Produces edit.js, save.js, block.json, and render.php with InnerBlocks support and block.json viewScriptModule."
verification: "security_reviewed"
source: "https://developer.wordpress.org/block-editor/"
category:
  - "WordPress & CMS"
framework:
  - "Claude Code"
---

# Gutenberg Block Scaffolder

Gutenberg Block Scaffolder automates the creation of WordPress editor blocks following the Block API v3 specification. It uses the @wordpress/create-block scaffold tool as a foundation, then customizes output based on your requirements. The agent generates complete block packages including block.json metadata with apiVersion 3, edit.js with useBlockProps and InspectorControls, save.js with proper serialization, and optional render.php for dynamic server-side rendering. It supports InnerBlocks with allowedBlocks and template locking, custom BlockControls toolbars, and the new viewScriptModule field for frontend interactivity. Integrates with @wordpress/scripts for build configuration, generates proper webpack.config.js overrides when needed, and produces PHPUnit test stubs for render_callback functions. Supports block variations, block styles, and block patterns registration via register_block_pattern().

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/gutenberg-block-scaffolder-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/gutenberg-block-scaffolder-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/gutenberg-block-scaffolder-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gutenberg-block-scaffolder-agent/)
