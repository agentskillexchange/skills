---
name: "Gutenberg Custom Block Builder"
description: "Scaffolds and builds custom Gutenberg blocks using @wordpress/create-block and the Block API registerBlockType(). Generates edit/save components with InspectorControls, RichText, and InnerBlocks support."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/gutenberg-custom-block-builder/"
category:
  - "WordPress &amp; CMS"
framework:
  - "ChatGPT Agents"
---

# Gutenberg Custom Block Builder

This skill streamlines custom Gutenberg block development using the official @wordpress/create-block scaffolding tool and the WordPress Block API. It generates complete block plugins with registerBlockType() configuration, edit and save components, and block.json metadata following WordPress coding standards.
Block editor components leverage InspectorControls for sidebar settings panels, RichText for inline content editing, InnerBlocks for nested block support, and MediaUpload for image/video selection. The skill handles both static and dynamic blocks, with PHP render_callback functions for server-side rendering when blocks need fresh data.
Build tooling uses @wordpress/scripts for webpack configuration, hot module replacement during development, and production-optimized builds. The skill includes patterns for block variations, block styles, block transforms, and deprecated versions for backward compatibility when block markup changes.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gutenberg-custom-block-builder/)
