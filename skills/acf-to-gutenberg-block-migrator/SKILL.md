---
title: "ACF to Gutenberg Block Migrator"
description: "ACF to Gutenberg Block Migrator bridges the gap between ACF-dependent themes and the native block editor by converting ACF field groups into proper Gutenberg blocks. It reads ACF field group JSON exports, analyzes field types, and generates block.json registrations with matching attributes and server-side render callbacks.\nFor simple fields like text, image, and select, it maps directly to block attributes with corresponding BlockControls components. ACF repeater fields convert to InnerBlocks with allowedBlocks restrictions, preserving the repeatable data structure. Flexible content layouts become block variations registered through registerBlockVariation().\nThe migration generates PHP render templates using acf_register_block_type() with render_callback functions that pull data via get_field(). The @wordpress/scripts build pipeline handles JSX compilation, and the output includes both the editor-side JavaScript components and server-side PHP rendering. Existing ACF data in post_meta is preserved and readable by the new blocks through backward-compatible get_field() calls."
verification: security_reviewed
source: "https://www.advancedcustomfields.com/"
framework:
  - "Codex"
---

# ACF to Gutenberg Block Migrator

ACF to Gutenberg Block Migrator bridges the gap between ACF-dependent themes and the native block editor by converting ACF field groups into proper Gutenberg blocks. It reads ACF field group JSON exports, analyzes field types, and generates block.json registrations with matching attributes and server-side render callbacks.
For simple fields like text, image, and select, it maps directly to block attributes with corresponding BlockControls components. ACF repeater fields convert to InnerBlocks with allowedBlocks restrictions, preserving the repeatable data structure. Flexible content layouts become block variations registered through registerBlockVariation().
The migration generates PHP render templates using acf_register_block_type() with render_callback functions that pull data via get_field(). The @wordpress/scripts build pipeline handles JSX compilation, and the output includes both the editor-side JavaScript components and server-side PHP rendering. Existing ACF data in post_meta is preserved and readable by the new blocks through backward-compatible get_field() calls.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/acf-to-gutenberg-block-migrator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/acf-to-gutenberg-block-migrator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/acf-to-gutenberg-block-migrator/)
