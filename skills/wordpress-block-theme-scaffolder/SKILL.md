---
name: "WordPress Block Theme Scaffolder"
description: "Generates complete WordPress block theme structures using theme.json v3, block patterns via register_block_pattern(), and template parts. Produces FSE-ready themes with proper style variations, typography presets, and wp_enqueue_block_editor_assets integration."
category: "WordPress &amp; CMS"
framework: "Claude Code"
verification: security_reviewed
source: "https://developer.wordpress.org/block-editor/"
---
# WordPress Block Theme Scaffolder

Generates complete WordPress block theme structures using theme.json v3, block patterns via register_block_pattern(), and template parts. Produces FSE-ready themes with proper style variations, typography presets, and wp_enqueue_block_editor_assets integration.

WordPress Block Theme Scaffolder automates the creation of Full Site Editing themes by generating the complete directory structure: templates, parts, patterns, and a fully configured theme.json v3 manifest. It produces valid theme.json with typography, color palette, spacing, and layout settings following WordPress core specifications.

Block patterns are created using register_block_pattern() with proper categories assigned via register_block_pattern_category(). Template parts for headers, footers, and sidebars are generated as HTML files in the parts directory with correct template part area declarations. The scaffolder includes style variation JSON files for alternative theme appearances.

Build tooling is configured through @wordpress/scripts with wp-scripts build and wp-scripts start commands. Editor assets load via wp_enqueue_block_editor_assets, and frontend styles use wp_enqueue_block_style for per-block stylesheets. The output includes a functions.php with proper after_setup_theme hooks, textdomain loading, and block style registration.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill wordpress-block-theme-scaffolder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill wordpress-block-theme-scaffolder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill wordpress-block-theme-scaffolder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill wordpress-block-theme-scaffolder -a codex
```

### OpenClaw

```bash
clawhub install wordpress-block-theme-scaffolder
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wordpress-block-theme-scaffolder/)
