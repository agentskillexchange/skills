---
title: ACF to Gutenberg Block Migrator
description: ACF to Gutenberg Block Migrator bridges the gap between ACF-dependent
  themes and the native block editor by converting ACF field groups into proper Gutenberg
  blocks. It reads ACF field group JSON exports, analyzes field types, and generates
  block.json registrations with matching attributes and server-side render callbacks.
  For simple fields like text, image, and select, it maps directly to block attributes
  with corresponding BlockControls components. ACF repeater fields convert to InnerBlocks
  with allowedBlocks restrictions, preserving the repeatable data structure. Flexible
  content layouts become block variations registered through registerBlockVariation().
  The migration generates PHP render templates using acf_register_block_type() with
  render_callback functions that pull data via get_field(). The @wordpress/scripts
  build pipeline handles JSX compilation, and the output includes both the editor-side
  JavaScript components and server-side PHP rendering. Existing ACF data in post_meta
  is preserved and readable by the new blocks through backward-compatible get_field()
  calls.
verification: security_reviewed
source: https://www.advancedcustomfields.com/
category:
- WordPress &amp; CMS
framework:
- Codex
---

# ACF to Gutenberg Block Migrator

ACF to Gutenberg Block Migrator bridges the gap between ACF-dependent themes and the native block editor by converting ACF field groups into proper Gutenberg blocks. It reads ACF field group JSON exports, analyzes field types, and generates block.json registrations with matching attributes and server-side render callbacks. For simple fields like text, image, and select, it maps directly to block attributes with corresponding BlockControls components. ACF repeater fields convert to InnerBlocks with allowedBlocks restrictions, preserving the repeatable data structure. Flexible content layouts become block variations registered through registerBlockVariation(). The migration generates PHP render templates using acf_register_block_type() with render_callback functions that pull data via get_field(). The @wordpress/scripts build pipeline handles JSX compilation, and the output includes both the editor-side JavaScript components and server-side PHP rendering. Existing ACF data in post_meta is preserved and readable by the new blocks through backward-compatible get_field() calls.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/acf-to-gutenberg-block-migrator/)
