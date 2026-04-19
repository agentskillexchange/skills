---
title: "WordPress Block Theme Scaffolder"
description: "WordPress Block Theme Scaffolder automates the creation of Full Site Editing themes by generating the complete directory structure: templates, parts, patterns, and a fully configured theme.json v3 manifest. It produces valid theme.json with typography, color palette, spacing, and layout settings following WordPress core specifications. Block patterns are created using register_block_pattern() with proper categories assigned via register_block_pattern_category(). Template parts for headers, footers, and sidebars are generated as HTML files in the parts directory with correct template part area declarations. The scaffolder includes style variation JSON files for alternative theme appearances. Build tooling is configured through @wordpress/scripts with wp-scripts build and wp-scripts start commands. Editor assets load via wp_enqueue_block_editor_assets, and frontend styles use wp_enqueue_block_style for per-block stylesheets. The output includes a functions.php with proper after_setup_theme hooks, textdomain loading, and block style registration."
source: "https://developer.wordpress.org/block-editor/"
verification: "security_reviewed"
category:
  - "WordPress &amp; CMS"
framework:
  - "Claude Code"
---

# WordPress Block Theme Scaffolder

WordPress Block Theme Scaffolder automates the creation of Full Site Editing themes by generating the complete directory structure: templates, parts, patterns, and a fully configured theme.json v3 manifest. It produces valid theme.json with typography, color palette, spacing, and layout settings following WordPress core specifications. Block patterns are created using register_block_pattern() with proper categories assigned via register_block_pattern_category(). Template parts for headers, footers, and sidebars are generated as HTML files in the parts directory with correct template part area declarations. The scaffolder includes style variation JSON files for alternative theme appearances. Build tooling is configured through @wordpress/scripts with wp-scripts build and wp-scripts start commands. Editor assets load via wp_enqueue_block_editor_assets, and frontend styles use wp_enqueue_block_style for per-block stylesheets. The output includes a functions.php with proper after_setup_theme hooks, textdomain loading, and block style registration.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wordpress-block-theme-scaffolder/)
