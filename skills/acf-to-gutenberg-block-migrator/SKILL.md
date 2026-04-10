---
name: ACF to Gutenberg Block Migrator
description: Converts Advanced Custom Fields field groups into native Gutenberg blocks
  using the ACF Block API v2 and @wordpress/scripts build pipeline. Maps ACF repeaters,
  groups, and flexible content to InnerBlocks and block attributes with server-side
  rendering via acf_register_block_type().
verification: security_reviewed
source: https://www.advancedcustomfields.com/
category:
- WordPress &amp; CMS
framework:
- Codex
---
# ACF to Gutenberg Block Migrator

ACF to Gutenberg Block Migrator bridges the gap between ACF-dependent themes and the native block editor by converting ACF field groups into proper Gutenberg blocks. It reads ACF field group JSON exports, analyzes field types, and generates block.json registrations with matching attributes and server-side render callbacks.
For simple fields like text, image, and select, it maps directly to block attributes with corresponding BlockControls components. ACF repeater fields convert to InnerBlocks with allowedBlocks restrictions, preserving the repeatable data structure. Flexible content layouts become block variations registered through registerBlockVariation().
The migration generates PHP render templates using acf_register_block_type() with render_callback functions that pull data via get_field(). The @wordpress/scripts build pipeline handles JSX compilation, and the output includes both the editor-side JavaScript components and server-side PHP rendering. Existing ACF data in post_meta is preserved and readable by the new blocks through backward-compatible get_field() calls.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/acf-to-gutenberg-block-migrator/)
