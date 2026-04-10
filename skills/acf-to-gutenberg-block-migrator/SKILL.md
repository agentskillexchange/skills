---
title: "ACF to Gutenberg Block Migrator"
description: "Converts Advanced Custom Fields field groups into native Gutenberg blocks using the ACF Block API v2 and @wordpress/scripts build pipeline. Maps ACF repeaters, groups, and flexible content to InnerBlocks and block attributes with server-side rendering via acf_register_block_type()."
slug: "acf-to-gutenberg-block-migrator"
category:
  - "WordPress &amp; CMS"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://www.advancedcustomfields.com/"
listed: true
---

# ACF to Gutenberg Block Migrator

Converts Advanced Custom Fields field groups into native Gutenberg blocks using the ACF Block API v2 and @wordpress/scripts build pipeline. Maps ACF repeaters, groups, and flexible content to InnerBlocks and block attributes with server-side rendering via acf_register_block_type().

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install acf-to-gutenberg-block-migrator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

ACF to Gutenberg Block Migrator bridges the gap between ACF-dependent themes and the native block editor by converting ACF field groups into proper Gutenberg blocks. It reads ACF field group JSON exports, analyzes field types, and generates block.json registrations with matching attributes and server-side render callbacks.
For simple fields like text, image, and select, it maps directly to block attributes with corresponding BlockControls components. ACF repeater fields convert to InnerBlocks with allowedBlocks restrictions, preserving the repeatable data structure. Flexible content layouts become block variations registered through registerBlockVariation().
The migration generates PHP render templates using acf_register_block_type() with render_callback functions that pull data via get_field(). The @wordpress/scripts build pipeline handles JSX compilation, and the output includes both the editor-side JavaScript components and server-side PHP rendering. Existing ACF data in post_meta is preserved and readable by the new blocks through backward-compatible get_field() calls.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/acf-to-gutenberg-block-migrator/)
