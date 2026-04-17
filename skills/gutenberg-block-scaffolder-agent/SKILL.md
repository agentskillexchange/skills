---
title: "Gutenberg Block Scaffolder"
description: "Gutenberg Block Scaffolder automates the creation of WordPress editor blocks following the Block API v3 specification. It uses the @wordpress/create-block scaffold tool as a foundation, then customizes output based on your requirements.\nThe agent generates complete block packages including block.json metadata with apiVersion 3, edit.js with useBlockProps and InspectorControls, save.js with proper serialization, and optional render.php for dynamic server-side rendering. It supports InnerBlocks with allowedBlocks and template locking, custom BlockControls toolbars, and the new viewScriptModule field for frontend interactivity.\nIntegrates with @wordpress/scripts for build configuration, generates proper webpack.config.js overrides when needed, and produces PHPUnit test stubs for render_callback functions. Supports block variations, block styles, and block patterns registration via register_block_pattern()."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/gutenberg-block-scaffolder-agent/"
framework:
  - "Claude Code"
---

# Gutenberg Block Scaffolder

Gutenberg Block Scaffolder automates the creation of WordPress editor blocks following the Block API v3 specification. It uses the @wordpress/create-block scaffold tool as a foundation, then customizes output based on your requirements.
The agent generates complete block packages including block.json metadata with apiVersion 3, edit.js with useBlockProps and InspectorControls, save.js with proper serialization, and optional render.php for dynamic server-side rendering. It supports InnerBlocks with allowedBlocks and template locking, custom BlockControls toolbars, and the new viewScriptModule field for frontend interactivity.
Integrates with @wordpress/scripts for build configuration, generates proper webpack.config.js overrides when needed, and produces PHPUnit test stubs for render_callback functions. Supports block variations, block styles, and block patterns registration via register_block_pattern().

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/gutenberg-block-scaffolder-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/gutenberg-block-scaffolder-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gutenberg-block-scaffolder-agent/)
