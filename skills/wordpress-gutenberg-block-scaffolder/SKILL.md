---
name: WordPress Gutenberg Block Scaffolder
description: Generates custom Gutenberg blocks using @wordpress/create-block and the
  Block API v2. Configures block.json metadata, InspectorControls, and server-side
  render callbacks with register_block_type.
verification: security_reviewed
source: https://agentskillexchange.com/skills/wordpress-gutenberg-block-scaffolder/
category:
- WordPress &amp; CMS
framework:
- Claude Code
---
# WordPress Gutenberg Block Scaffolder

This skill automates the creation of custom Gutenberg blocks for WordPress sites. It uses @wordpress/create-block as the scaffolding tool, generating proper block.json metadata files with apiVersion 3 compliance. Each block includes InspectorControls for sidebar settings panels, BlockControls for toolbar customization, and useBlockProps for proper wrapper element handling. The agent configures server-side rendering via register_block_type() with render_callback functions for dynamic content. It sets up the build pipeline using @wordpress/scripts with wp-scripts build and wp-scripts start commands. Block attributes are defined with proper types, defaults, and source configurations. The skill handles block variations, patterns, and block styles. It integrates with the WordPress theme.json system for consistent spacing, colors, and typography tokens. Includes unit test scaffolding using @wordpress/jest-preset-default.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wordpress-gutenberg-block-scaffolder/)
