---
title: "Gutenberg Block Scaffolder"
description: "Gutenberg Block Scaffolder automates the creation of WordPress editor blocks following the Block API v3 specification. It uses the @wordpress/create-block scaffold tool as a foundation, then customizes output based on your requirements. The agent generates complete block packages including block.json metadata with apiVersion 3, edit.js with useBlockProps and InspectorControls , save.js with proper serialization, and optional render.php for dynamic server-side rendering. It supports InnerBlocks with allowedBlocks and template locking, custom BlockControls toolbars, and the new viewScriptModule field for frontend interactivity. Integrates with @wordpress/scripts for build configuration, generates proper webpack.config.js overrides when needed, and produces PHPUnit test stubs for render_callback functions. Supports block variations, block styles, and block patterns registration via register_block_pattern() ."
source: "https://agentskillexchange.com/skills/gutenberg-block-scaffolder-agent/"
verification: "security_reviewed"
category:
  - "WordPress &amp; CMS"
framework:
  - "Claude Code"
---

# Gutenberg Block Scaffolder

Gutenberg Block Scaffolder automates the creation of WordPress editor blocks following the Block API v3 specification. It uses the @wordpress/create-block scaffold tool as a foundation, then customizes output based on your requirements. The agent generates complete block packages including block.json metadata with apiVersion 3, edit.js with useBlockProps and InspectorControls , save.js with proper serialization, and optional render.php for dynamic server-side rendering. It supports InnerBlocks with allowedBlocks and template locking, custom BlockControls toolbars, and the new viewScriptModule field for frontend interactivity. Integrates with @wordpress/scripts for build configuration, generates proper webpack.config.js overrides when needed, and produces PHPUnit test stubs for render_callback functions. Supports block variations, block styles, and block patterns registration via register_block_pattern() .

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gutenberg-block-scaffolder-agent/)
