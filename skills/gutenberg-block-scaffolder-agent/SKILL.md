---
title: Gutenberg Block Scaffolder
description: Gutenberg Block Scaffolder automates the creation of WordPress editor
  blocks following the Block API v3 specification. It uses the @wordpress/create-block
  scaffold tool as a foundation, then customizes output based on your requirements.
  The agent generates complete block packages including block.json metadata with apiVersion
  3, edit.js with useBlockProps and InspectorControls , save.js with proper serialization,
  and optional render.php for dynamic server-side rendering. It supports InnerBlocks
  with allowedBlocks and template locking, custom BlockControls toolbars, and the
  new viewScriptModule field for frontend interactivity. Integrates with @wordpress/scripts
  for build configuration, generates proper webpack.config.js overrides when needed,
  and produces PHPUnit test stubs for render_callback functions. Supports block variations,
  block styles, and block patterns registration via register_block_pattern() .
verification: security_reviewed
source: https://agentskillexchange.com/skills/gutenberg-block-scaffolder-agent/
category:
- WordPress &amp; CMS
framework:
- Claude Code
---

# Gutenberg Block Scaffolder

Gutenberg Block Scaffolder automates the creation of WordPress editor blocks following the Block API v3 specification. It uses the @wordpress/create-block scaffold tool as a foundation, then customizes output based on your requirements. The agent generates complete block packages including block.json metadata with apiVersion 3, edit.js with useBlockProps and InspectorControls , save.js with proper serialization, and optional render.php for dynamic server-side rendering. It supports InnerBlocks with allowedBlocks and template locking, custom BlockControls toolbars, and the new viewScriptModule field for frontend interactivity. Integrates with @wordpress/scripts for build configuration, generates proper webpack.config.js overrides when needed, and produces PHPUnit test stubs for render_callback functions. Supports block variations, block styles, and block patterns registration via register_block_pattern() .

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gutenberg-block-scaffolder-agent/)
