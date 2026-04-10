---
name: "Gutenberg Block Pattern Generator"
description: "Generates custom WordPress Gutenberg block patterns using register_block_pattern() and the Block Editor API. Creates reusable pattern categories with register_block_pattern_category() for organized content libraries."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/gutenberg-block-pattern-generator/"
category:
  - "WordPress &amp; CMS"
framework:
  - "Claude Code"
---

# Gutenberg Block Pattern Generator

The Gutenberg Block Pattern Generator automates the creation of custom block patterns for the WordPress editor. Using register_block_pattern() and register_block_pattern_category(), it builds organized libraries of reusable content layouts. The agent parses existing page designs and converts them into block markup using the @wordpress/blocks package serialize() function. It supports InnerBlocks configurations, dynamic blocks with ServerSideRender, and pattern transformations via the @wordpress/block-editor useBlockProps hook. The generator validates all patterns against the WordPress block grammar specification and tests rendering through the REST API block-renderer endpoint. It handles pattern versioning using post meta and supports import/export via the WordPress export format (WXR). Integration with theme.json allows pattern-aware theme development, and the agent can auto-generate pattern previews using the block preview component from @wordpress/block-editor.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gutenberg-block-pattern-generator/)
