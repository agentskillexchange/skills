---
title: "WordPress Gutenberg Block Generator"
description: "Scaffolds custom Gutenberg blocks using the @wordpress/create-block CLI and block.json schema, then registers them via register_block_type PHP API. Generates edit/save components with InspectorControls and useBlockProps. Outputs production-ready block plugin structure."
verification: security_reviewed
source: "https://github.com/WordPress/WordPress"
category:
  - "WordPress &amp; CMS"
framework:
  - "Cursor"
---

# WordPress Gutenberg Block Generator

Scaffolds custom Gutenberg blocks using the @wordpress/create-block CLI and block.json schema, then registers them via register_block_type PHP API. Generates edit/save components with InspectorControls and useBlockProps. Outputs production-ready block plugin structure.

This skill handles the full custom block scaffolding workflow: setting up the block plugin directory, writing block.json metadata, creating the edit and save JavaScript components, and registering the block via PHP. It supports static and dynamic blocks, generates Inspector sidebar controls, and applies useBlockProps hooks correctly. Compatible with WordPress 6.x block API version 3.

Use this when building custom blocks for client sites, theme plugins, or block libraries. Particularly useful when you need attribute-driven dynamic content, sidebar settings, or styled wrapper elements. Not for FSE theme template parts — use theme.json patterns instead. Requires Node.js 18+ and @wordpress/scripts installed.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wordpress-gutenberg-block-generator/)
