---
name: WordPress Gutenberg Block Generator
description: Scaffolds custom Gutenberg blocks using the @wordpress/create-block CLI
  and block.json schema, then registers them via register_block_type PHP API. Generates
  edit/save components with InspectorControls and useBlockProps. Outputs production-ready
  block plugin structure.
verification: security_reviewed
source: https://agentskillexchange.com/skills/wordpress-gutenberg-block-generator/
category:
- WordPress &amp; CMS
framework:
- Cursor
---
# WordPress Gutenberg Block Generator

Scaffolds custom Gutenberg blocks using the @wordpress/create-block CLI and block.json schema, then registers them via register_block_type PHP API. Generates edit/save components with InspectorControls and useBlockProps. Outputs production-ready block plugin structure.
This skill handles the full custom block scaffolding workflow: setting up the block plugin directory, writing block.json metadata, creating the edit and save JavaScript components, and registering the block via PHP. It supports static and dynamic blocks, generates Inspector sidebar controls, and applies useBlockProps hooks correctly. Compatible with WordPress 6.x block API version 3.
Use this when building custom blocks for client sites, theme plugins, or block libraries. Particularly useful when you need attribute-driven dynamic content, sidebar settings, or styled wrapper elements. Not for FSE theme template parts — use theme.json patterns instead. Requires Node.js 18+ and @wordpress/scripts installed.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wordpress-gutenberg-block-generator/)
