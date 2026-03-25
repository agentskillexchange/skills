---
name: "Gutenberg Block Pattern Generator"
description: "Generates custom WordPress Gutenberg block patterns using register_block_pattern() and the Block Editor API. Creates reusable pattern categories with register_block_pattern_category() for organized content libraries."
category: "WordPress & CMS"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/gutenberg-block-pattern-generator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "wordpress"  # from ase_tool_match
  github_stars: 20976  # from ase_github_stars (integer, not string)
  github_repo: "WordPress/WordPress"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Gutenberg Block Pattern Generator

Generates custom WordPress Gutenberg block patterns using register_block_pattern() and the Block Editor API. Creates reusable pattern categories with register_block_pattern_category() for organized content libraries.

## Overview

The Gutenberg Block Pattern Generator automates the creation of custom block patterns for the WordPress editor. Using register_block_pattern() and register_block_pattern_category(), it builds organized libraries of reusable content layouts. The agent parses existing page designs and converts them into block markup using the @wordpress/blocks package serialize() function. It supports InnerBlocks configurations, dynamic blocks with ServerSideRender, and pattern transformations via the @wordpress/block-editor useBlockProps hook. The generator validates all patterns against the WordPress block grammar specification and tests rendering through the REST API block-renderer endpoint. It handles pattern versioning using post meta and supports import/export via the WordPress export format (WXR). Integration with theme.json allows pattern-aware theme development, and the agent can auto-generate pattern previews using the block preview component from @wordpress/block-editor.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill gutenberg-block-pattern-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill gutenberg-block-pattern-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill gutenberg-block-pattern-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill gutenberg-block-pattern-generator -a codex
```

### OpenClaw

```bash
clawhub install gutenberg-block-pattern-generator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/gutenberg-block-pattern-generator/
