---
name: "WordPress Gutenberg Block Scaffolder"
description: "Generates custom Gutenberg blocks using @wordpress/create-block and the Block API v2. Configures block.json metadata, InspectorControls, and server-side render callbacks with register_block_type."
category: "WordPress & CMS"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/wordpress-gutenberg-block-scaffolder/"
tool_ecosystem:
  tool: wordpress
  github_stars: 20976
  github_repo: WordPress/WordPress
  maintained: true
---

# WordPress Gutenberg Block Scaffolder

Generates custom Gutenberg blocks using @wordpress/create-block and the Block API v2. Configures block.json metadata, InspectorControls, and server-side render callbacks with register_block_type.

## Overview

This skill automates the creation of custom Gutenberg blocks for WordPress sites. It uses @wordpress/create-block as the scaffolding tool, generating proper block.json metadata files with apiVersion 3 compliance. Each block includes InspectorControls for sidebar settings panels, BlockControls for toolbar customization, and useBlockProps for proper wrapper element handling. The agent configures server-side rendering via register_block_type() with render_callback functions for dynamic content. It sets up the build pipeline using @wordpress/scripts with wp-scripts build and wp-scripts start commands. Block attributes are defined with proper types, defaults, and source configurations. The skill handles block variations, patterns, and block styles. It integrates with the WordPress theme.json system for consistent spacing, colors, and typography tokens. Includes unit test scaffolding using @wordpress/jest-preset-default.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill wordpress-gutenberg-block-scaffolder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill wordpress-gutenberg-block-scaffolder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill wordpress-gutenberg-block-scaffolder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill wordpress-gutenberg-block-scaffolder -a codex
```

### OpenClaw

```bash
clawhub install wordpress-gutenberg-block-scaffolder
```

## Source

- Marketplace: https://agentskillexchange.com/skills/wordpress-gutenberg-block-scaffolder/
