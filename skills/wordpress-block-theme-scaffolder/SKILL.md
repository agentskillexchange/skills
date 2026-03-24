---
name: "WordPress Block Theme Scaffolder"
description: "Generates complete WordPress block theme structures using theme.json v3, block patterns via register_block_pattern(), and template parts. Produces FSE-ready themes with proper style variations, typography presets, and wp_enqueue_block_editor_assets integration."
category: "WordPress & CMS"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/wordpress-block-theme-scaffolder/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "wordpress"  # from ase_tool_match
  github_stars: 20973  # from ase_github_stars (integer, not string)
  github_repo: "WordPress/WordPress"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# WordPress Block Theme Scaffolder

Generates complete WordPress block theme structures using theme.json v3, block patterns via register_block_pattern(), and template parts. Produces FSE-ready themes with proper style variations, typography presets, and wp_enqueue_block_editor_assets integration.

## Overview

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

- Marketplace: https://agentskillexchange.com/skills/wordpress-block-theme-scaffolder/
