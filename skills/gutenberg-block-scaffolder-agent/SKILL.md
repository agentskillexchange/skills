---
name: "Gutenberg Block Scaffolder"
description: "Generates custom Gutenberg blocks using @wordpress/create-block and the Block API v3 schema. Produces edit.js, save.js, block.json, and render.php with InnerBlocks support and block.json viewScriptModule."
category: "WordPress & CMS"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/gutenberg-block-scaffolder-agent/"
---
# Gutenberg Block Scaffolder

Generates custom Gutenberg blocks using @wordpress/create-block and the Block API v3 schema. Produces edit.js, save.js, block.json, and render.php with InnerBlocks support and block.json viewScriptModule.

Gutenberg Block Scaffolder automates the creation of WordPress editor blocks following the Block API v3 specification. It uses the @wordpress/create-block scaffold tool as a foundation, then customizes output based on your requirements.



The agent generates complete block packages including block.json metadata with apiVersion 3, edit.js with useBlockProps and InspectorControls, save.js with proper serialization, and optional render.php for dynamic server-side rendering. It supports InnerBlocks with allowedBlocks and template locking, custom BlockControls toolbars, and the new viewScriptModule field for frontend interactivity.



Integrates with @wordpress/scripts for build configuration, generates proper webpack.config.js overrides when needed, and produces PHPUnit test stubs for render_callback functions. Supports block variations, block styles, and block patterns registration via register_block_pattern().

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill gutenberg-block-scaffolder-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill gutenberg-block-scaffolder-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill gutenberg-block-scaffolder-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill gutenberg-block-scaffolder-agent -a codex
```

### OpenClaw

```bash
clawhub install gutenberg-block-scaffolder-agent
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gutenberg-block-scaffolder-agent/)
