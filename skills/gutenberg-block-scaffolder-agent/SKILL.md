---
title: "Gutenberg Block Scaffolder"
description: "Generates custom Gutenberg blocks using @wordpress/create-block and the Block API v3 schema. Produces edit.js, save.js, block.json, and render.php with InnerBlocks support and block.json viewScriptModule."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/gutenberg-block-scaffolder-agent/"
category:
  - "WordPress &amp; CMS"
framework:
  - "Claude Code"
---

# Gutenberg Block Scaffolder

Gutenberg Block Scaffolder automates the creation of WordPress editor blocks following the Block API v3 specification. It uses the @wordpress/create-block scaffold tool as a foundation, then customizes output based on your requirements.

The agent generates complete block packages including block.json metadata with apiVersion 3, edit.js with useBlockProps and InspectorControls, save.js with proper serialization, and optional render.php for dynamic server-side rendering. It supports InnerBlocks with allowedBlocks and template locking, custom BlockControls toolbars, and the new viewScriptModule field for frontend interactivity.

Integrates with @wordpress/scripts for build configuration, generates proper webpack.config.js overrides when needed, and produces PHPUnit test stubs for render_callback functions. Supports block variations, block styles, and block patterns registration via register_block_pattern().

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gutenberg-block-scaffolder-agent/)
