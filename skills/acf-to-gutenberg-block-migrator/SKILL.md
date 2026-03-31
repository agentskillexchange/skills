---
name: "ACF to Gutenberg Block Migrator"
description: "Converts Advanced Custom Fields field groups into native Gutenberg blocks using the ACF Block API v2 and @wordpress/scripts build pipeline. Maps ACF repeaters, groups, and flexible content to InnerBlocks and block attributes with server-side rendering via acf_register_block_type()."
category: "WordPress & CMS"
framework: "Codex"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/acf-to-gutenberg-block-migrator/"
---
# ACF to Gutenberg Block Migrator

Converts Advanced Custom Fields field groups into native Gutenberg blocks using the ACF Block API v2 and @wordpress/scripts build pipeline. Maps ACF repeaters, groups, and flexible content to InnerBlocks and block attributes with server-side rendering via acf_register_block_type().

## Overview

ACF to Gutenberg Block Migrator bridges the gap between ACF-dependent themes and the native block editor by converting ACF field groups into proper Gutenberg blocks. It reads ACF field group JSON exports, analyzes field types, and generates block.json registrations with matching attributes and server-side render callbacks.

For simple fields like text, image, and select, it maps directly to block attributes with corresponding BlockControls components. ACF repeater fields convert to InnerBlocks with allowedBlocks restrictions, preserving the repeatable data structure. Flexible content layouts become block variations registered through registerBlockVariation().

The migration generates PHP render templates using acf_register_block_type() with render_callback functions that pull data via get_field(). The @wordpress/scripts build pipeline handles JSX compilation, and the output includes both the editor-side JavaScript components and server-side PHP rendering. Existing ACF data in post_meta is preserved and readable by the new blocks through backward-compatible get_field() calls.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill acf-to-gutenberg-block-migrator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill acf-to-gutenberg-block-migrator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill acf-to-gutenberg-block-migrator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill acf-to-gutenberg-block-migrator -a codex
```

### OpenClaw

```bash
clawhub install acf-to-gutenberg-block-migrator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/acf-to-gutenberg-block-migrator/)
