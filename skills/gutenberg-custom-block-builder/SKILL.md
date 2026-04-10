---
title: "Gutenberg Custom Block Builder"
description: "Scaffolds and builds custom Gutenberg blocks using @wordpress/create-block and the Block API registerBlockType(). Generates edit/save components with InspectorControls, RichText, and InnerBlocks support."
slug: "gutenberg-custom-block-builder"
category:
  - "WordPress &amp; CMS"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/gutenberg-custom-block-builder/"
listed: true
---

# Gutenberg Custom Block Builder

Scaffolds and builds custom Gutenberg blocks using @wordpress/create-block and the Block API registerBlockType(). Generates edit/save components with InspectorControls, RichText, and InnerBlocks support.

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
clawhub install gutenberg-custom-block-builder
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill streamlines custom Gutenberg block development using the official @wordpress/create-block scaffolding tool and the WordPress Block API. It generates complete block plugins with registerBlockType() configuration, edit and save components, and block.json metadata following WordPress coding standards.
Block editor components leverage InspectorControls for sidebar settings panels, RichText for inline content editing, InnerBlocks for nested block support, and MediaUpload for image/video selection. The skill handles both static and dynamic blocks, with PHP render_callback functions for server-side rendering when blocks need fresh data.
Build tooling uses @wordpress/scripts for webpack configuration, hot module replacement during development, and production-optimized builds. The skill includes patterns for block variations, block styles, block transforms, and deprecated versions for backward compatibility when block markup changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gutenberg-custom-block-builder/)
