---
title: "ACF to Gutenberg Block Migrator"
description: "Converts Advanced Custom Fields field groups into native Gutenberg blocks using the ACF Block API v2 and @wordpress/scripts build pipeline. Maps ACF repeaters, groups, and flexible content to InnerBlocks and block attributes with server-side rendering via acf_register_block_type()."
verification: "security_reviewed"
source: "https://www.advancedcustomfields.com/"
category:
  - "WordPress &amp; CMS"
framework:
  - "Codex"
---

# ACF to Gutenberg Block Migrator

ACF to Gutenberg Block Migrator bridges the gap between ACF-dependent themes and the native block editor by converting ACF field groups into proper Gutenberg blocks. It reads ACF field group JSON exports, analyzes field types, and generates block.json registrations with matching attributes and server-side render callbacks.

For simple fields like text, image, and select, it maps directly to block attributes with corresponding BlockControls components. ACF repeater fields convert to InnerBlocks with allowedBlocks restrictions, preserving the repeatable data structure. Flexible content layouts become block variations registered through registerBlockVariation().

The migration generates PHP render templates using acf_register_block_type() with render_callback functions that pull data via get_field(). The @wordpress/scripts build pipeline handles JSX compilation, and the output includes both the editor-side JavaScript components and server-side PHP rendering. Existing ACF data in post_meta is preserved and readable by the new blocks through backward-compatible get_field() calls.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/acf-to-gutenberg-block-migrator/)
