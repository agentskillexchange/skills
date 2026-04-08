---
title: WordPress Block Theme Scaffolder
description: 'WordPress Block Theme Scaffolder automates the creation of Full Site
  Editing themes by generating the complete directory structure: templates, parts,
  patterns, and a fully configured theme.json v3 manifest. It produces valid theme.json
  with typography, color palette, spacing, and layout settings following WordPress
  core specifications. Block patterns are created using register_block_pattern() with
  proper categories assigned via register_block_pattern_category(). Template parts
  for headers, footers, and sidebars are generated as HTML files in the parts directory
  with correct template part area declarations. The scaffolder includes style variation
  JSON files for alternative theme appearances. Build tooling is configured through
  @wordpress/scripts with wp-scripts build and wp-scripts start commands. Editor assets
  load via wp_enqueue_block_editor_assets, and frontend styles use wp_enqueue_block_style
  for per-block stylesheets. The output includes a functions.php with proper after_setup_theme
  hooks, textdomain loading, and block style registration.'
verification: security_reviewed
source: https://developer.wordpress.org/block-editor/
category:
- WordPress &amp; CMS
framework:
- Claude Code
---

# WordPress Block Theme Scaffolder

WordPress Block Theme Scaffolder automates the creation of Full Site Editing themes by generating the complete directory structure: templates, parts, patterns, and a fully configured theme.json v3 manifest. It produces valid theme.json with typography, color palette, spacing, and layout settings following WordPress core specifications. Block patterns are created using register_block_pattern() with proper categories assigned via register_block_pattern_category(). Template parts for headers, footers, and sidebars are generated as HTML files in the parts directory with correct template part area declarations. The scaffolder includes style variation JSON files for alternative theme appearances. Build tooling is configured through @wordpress/scripts with wp-scripts build and wp-scripts start commands. Editor assets load via wp_enqueue_block_editor_assets, and frontend styles use wp_enqueue_block_style for per-block stylesheets. The output includes a functions.php with proper after_setup_theme hooks, textdomain loading, and block style registration.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wordpress-block-theme-scaffolder/)
