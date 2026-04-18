---
title: "WordPress Gutenberg Block Scaffolder"
description: "Generates custom Gutenberg blocks using @wordpress/create-block and the Block API v2. Configures block.json metadata, InspectorControls, and server-side render callbacks with register_block_type."
verification: security_reviewed
source: "https://github.com/WordPress/WordPress"
category:
  - "WordPress & CMS"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "wordpress/wordpress"
  github_stars: 21027
---

# WordPress Gutenberg Block Scaffolder

This skill automates the creation of custom Gutenberg blocks for WordPress sites. It uses @wordpress/create-block as the scaffolding tool, generating proper block.json metadata files with apiVersion 3 compliance. Each block includes InspectorControls for sidebar settings panels, BlockControls for toolbar customization, and useBlockProps for proper wrapper element handling. The agent configures server-side rendering via register_block_type() with render_callback functions for dynamic content. It sets up the build pipeline using @wordpress/scripts with wp-scripts build and wp-scripts start commands. Block attributes are defined with proper types, defaults, and source configurations. The skill handles block variations, patterns, and block styles. It integrates with the WordPress theme.json system for consistent spacing, colors, and typography tokens. Includes unit test scaffolding using @wordpress/jest-preset-default.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/wordpress-gutenberg-block-scaffolder
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/wordpress-gutenberg-block-scaffolder` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wordpress-gutenberg-block-scaffolder/)
