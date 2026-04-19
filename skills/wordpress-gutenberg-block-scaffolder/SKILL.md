---
title: "WordPress Gutenberg Block Scaffolder"
description: "This skill automates the creation of custom Gutenberg blocks for WordPress sites. It uses @wordpress/create-block as the scaffolding tool, generating proper block.json metadata files with apiVersion 3 compliance. Each block includes InspectorControls for sidebar settings panels, BlockControls for toolbar customization, and useBlockProps for proper wrapper element handling. The agent configures server-side rendering via register_block_type() with render_callback functions for dynamic content. It sets up the build pipeline using @wordpress/scripts with wp-scripts build and wp-scripts start commands. Block attributes are defined with proper types, defaults, and source configurations. The skill handles block variations, patterns, and block styles. It integrates with the WordPress theme.json system for consistent spacing, colors, and typography tokens. Includes unit test scaffolding using @wordpress/jest-preset-default."
source: "https://github.com/WordPress/WordPress"
verification: "security_reviewed"
category:
  - "WordPress &amp; CMS"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "wordpress/wordpress"
  github_stars: 21027
---

# WordPress Gutenberg Block Scaffolder

This skill automates the creation of custom Gutenberg blocks for WordPress sites. It uses @wordpress/create-block as the scaffolding tool, generating proper block.json metadata files with apiVersion 3 compliance. Each block includes InspectorControls for sidebar settings panels, BlockControls for toolbar customization, and useBlockProps for proper wrapper element handling. The agent configures server-side rendering via register_block_type() with render_callback functions for dynamic content. It sets up the build pipeline using @wordpress/scripts with wp-scripts build and wp-scripts start commands. Block attributes are defined with proper types, defaults, and source configurations. The skill handles block variations, patterns, and block styles. It integrates with the WordPress theme.json system for consistent spacing, colors, and typography tokens. Includes unit test scaffolding using @wordpress/jest-preset-default.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wordpress-gutenberg-block-scaffolder/)
