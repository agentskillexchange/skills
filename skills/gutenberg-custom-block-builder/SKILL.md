---
title: "Gutenberg Custom Block Builder"
description: "Scaffolds and builds custom Gutenberg blocks using @wordpress/create-block and the Block API registerBlockType(). Generates edit/save components with InspectorControls, RichText, and InnerBlocks support."
verification: "security_reviewed"
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gutenberg-custom-block-builder/)
