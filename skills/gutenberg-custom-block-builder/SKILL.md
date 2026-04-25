---
title: "Gutenberg Custom Block Builder"
description: "Scaffolds and builds custom Gutenberg blocks using @wordpress/create-block and the Block API registerBlockType(). Generates edit/save components with InspectorControls, RichText, and InnerBlocks support."
verification: "security_reviewed"
source: "https://github.com/WordPress/gutenberg"
category:
  - "WordPress & CMS"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "WordPress/gutenberg"
  github_stars: 11624
  npm_package: "@wordpress/create-block"
  npm_weekly_downloads: 20291
---

# Gutenberg Custom Block Builder

This skill streamlines custom Gutenberg block development using the official @wordpress/create-block scaffolding tool and the WordPress Block API. It generates complete block plugins with registerBlockType() configuration, edit and save components, and block.json metadata following WordPress coding standards. Block editor components leverage InspectorControls for sidebar settings panels, RichText for inline content editing, InnerBlocks for nested block support, and MediaUpload for image/video selection. The skill handles both static and dynamic blocks, with PHP render_callback functions for server-side rendering when blocks need fresh data. Build tooling uses @wordpress/scripts for webpack configuration, hot module replacement during development, and production-optimized builds. The skill includes patterns for block variations, block styles, block transforms, and deprecated versions for backward compatibility when block markup changes.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/gutenberg-custom-block-builder/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/gutenberg-custom-block-builder
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/gutenberg-custom-block-builder`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gutenberg-custom-block-builder/)
