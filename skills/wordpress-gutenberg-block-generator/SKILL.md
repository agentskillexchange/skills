---
title: "WordPress Gutenberg Block Generator"
description: "Scaffolds custom Gutenberg blocks using the @wordpress/create-block CLI and block.json schema, then registers them via register_block_type PHP API. Generates edit/save components with InspectorControls and useBlockProps. Outputs production-ready block plugin structure."
verification: "security_reviewed"
source: "https://github.com/WordPress/WordPress"
category:
  - "WordPress & CMS"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "wordpress/wordpress"
  github_stars: 21027
---

# WordPress Gutenberg Block Generator

Scaffolds custom Gutenberg blocks using the @wordpress/create-block CLI and block.json schema, then registers them via register_block_type PHP API. Generates edit/save components with InspectorControls and useBlockProps. Outputs production-ready block plugin structure. This skill handles the full custom block scaffolding workflow: setting up the block plugin directory, writing block.json metadata, creating the edit and save JavaScript components, and registering the block via PHP. It supports static and dynamic blocks, generates Inspector sidebar controls, and applies useBlockProps hooks correctly. Compatible with WordPress 6.x block API version 3. Use this when building custom blocks for client sites, theme plugins, or block libraries. Particularly useful when you need attribute-driven dynamic content, sidebar settings, or styled wrapper elements. Not for FSE theme template parts — use theme.json patterns instead. Requires Node.js 18+ and @wordpress/scripts installed.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/wordpress-gutenberg-block-generator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/wordpress-gutenberg-block-generator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/wordpress-gutenberg-block-generator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wordpress-gutenberg-block-generator/)
