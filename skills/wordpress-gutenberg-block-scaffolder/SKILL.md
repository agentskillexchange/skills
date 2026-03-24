---
name: "WordPress Gutenberg Block Scaffolder"
description: "Generates custom Gutenberg blocks using @wordpress/create-block and the Block API v2. Configures block.json metadata, InspectorControls, and server-side render callbacks with register_block_type."
category: "WordPress & CMS"
framework: "Claude Code"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/wordpress-gutenberg-block-scaffolder/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "wordpress"  # from ase_tool_match
  github_stars: 20973  # from ase_github_stars (integer, not string)
  github_repo: "WordPress/WordPress"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
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
