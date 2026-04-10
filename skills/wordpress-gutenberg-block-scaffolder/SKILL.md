---
title: "WordPress Gutenberg Block Scaffolder"
description: "Generates custom Gutenberg blocks using @wordpress/create-block and the Block API v2. Configures block.json metadata, InspectorControls, and server-side render callbacks with register_block_type."
slug: "wordpress-gutenberg-block-scaffolder"
category:
  - "WordPress &amp; CMS"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/wordpress-gutenberg-block-scaffolder/"
---

# WordPress Gutenberg Block Scaffolder

Generates custom Gutenberg blocks using @wordpress/create-block and the Block API v2. Configures block.json metadata, InspectorControls, and server-side render callbacks with register_block_type.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install wordpress-gutenberg-block-scaffolder
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill automates the creation of custom Gutenberg blocks for WordPress sites. It uses @wordpress/create-block as the scaffolding tool, generating proper block.json metadata files with apiVersion 3 compliance. Each block includes InspectorControls for sidebar settings panels, BlockControls for toolbar customization, and useBlockProps for proper wrapper element handling. The agent configures server-side rendering via register_block_type() with render_callback functions for dynamic content. It sets up the build pipeline using @wordpress/scripts with wp-scripts build and wp-scripts start commands. Block attributes are defined with proper types, defaults, and source configurations. The skill handles block variations, patterns, and block styles. It integrates with the WordPress theme.json system for consistent spacing, colors, and typography tokens. Includes unit test scaffolding using @wordpress/jest-preset-default.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wordpress-gutenberg-block-scaffolder/)
