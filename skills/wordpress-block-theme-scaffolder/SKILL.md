---
title: "WordPress Block Theme Scaffolder"
description: "Generates complete WordPress block theme structures using theme.json v3, block patterns via register_block_pattern(), and template parts. Produces FSE-ready themes with proper style variations, typography presets, and wp_enqueue_block_editor_assets integration."
verification: security_reviewed
source: "https://developer.wordpress.org/block-editor/"
category:
  - "WordPress &amp; CMS"
framework:
  - "Claude Code"
---

# WordPress Block Theme Scaffolder

WordPress Block Theme Scaffolder automates the creation of Full Site Editing themes by generating the complete directory structure: templates, parts, patterns, and a fully configured theme.json v3 manifest. It produces valid theme.json with typography, color palette, spacing, and layout settings following WordPress core specifications.

Block patterns are created using register_block_pattern() with proper categories assigned via register_block_pattern_category(). Template parts for headers, footers, and sidebars are generated as HTML files in the parts directory with correct template part area declarations. The scaffolder includes style variation JSON files for alternative theme appearances.

Build tooling is configured through @wordpress/scripts with wp-scripts build and wp-scripts start commands. Editor assets load via wp_enqueue_block_editor_assets, and frontend styles use wp_enqueue_block_style for per-block stylesheets. The output includes a functions.php with proper after_setup_theme hooks, textdomain loading, and block style registration.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wordpress-block-theme-scaffolder/)
