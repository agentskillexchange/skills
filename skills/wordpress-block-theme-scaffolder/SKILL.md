---
title: "WordPress Block Theme Scaffolder"
description: "Generates complete WordPress block theme structures using theme.json v3, block patterns via register_block_pattern(), and template parts. Produces FSE-ready themes with proper style variations, typography presets, and wp_enqueue_block_editor_assets integration."
verification: "security_reviewed"
source: "https://developer.wordpress.org/block-editor/"
category:
  - "WordPress & CMS"
framework:
  - "Claude Code"
---

# WordPress Block Theme Scaffolder

WordPress Block Theme Scaffolder automates the creation of Full Site Editing themes by generating the complete directory structure: templates, parts, patterns, and a fully configured theme.json v3 manifest. It produces valid theme.json with typography, color palette, spacing, and layout settings following WordPress core specifications.

Block patterns are created using register_block_pattern() with proper categories assigned via register_block_pattern_category(). Template parts for headers, footers, and sidebars are generated as HTML files in the parts directory with correct template part area declarations. The scaffolder includes style variation JSON files for alternative theme appearances.

Build tooling is configured through @wordpress/scripts with wp-scripts build and wp-scripts start commands. Editor assets load via wp_enqueue_block_editor_assets, and frontend styles use wp_enqueue_block_style for per-block stylesheets. The output includes a functions.php with proper after_setup_theme hooks, textdomain loading, and block style registration.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/wordpress-block-theme-scaffolder/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/wordpress-block-theme-scaffolder
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/wordpress-block-theme-scaffolder`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wordpress-block-theme-scaffolder/)
