---
name: "WP Abilities API"
description: "Specialized support for defining, exposing, and debugging WordPress abilities through the Abilities API."
category: "WordPress & CMS"
framework: "OpenClaw"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/wp-abilities-api/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "wordpress"  # from ase_tool_match
  github_stars: 20973  # from ase_github_stars (integer, not string)
  github_repo: "WordPress/WordPress"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# WP Abilities API

Specialized support for defining, exposing, and debugging WordPress abilities through the Abilities API.

## Overview

WP Abilities API is a specialist skill for WordPress builders working with `wp_register_ability`, `wp_register_ability_category`, `/wp-json/wp-abilities/v1/*`, and `@wordpress/abilities`. It focuses on one narrow job: helping teams define abilities cleanly and expose them to clients without falling back to generic WordPress advice.

Best for

registering WordPress abilities and categories in PHP

debugging REST exposure and missing client visibility

implementing permission-aware ability checks in JavaScript clients

Install notes

Install the skill in an OpenClaw workspace that has access to your WordPress plugin, theme, or core checkout. It is most useful in environments targeting WordPress 6.9+ and may also rely on WP-CLI for validation workflows.

**Source:** OpenClaw-compatible WP Abilities API skill.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill wp-abilities-api
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill wp-abilities-api -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill wp-abilities-api -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill wp-abilities-api -a codex
```

### OpenClaw

```bash
clawhub install wp-abilities-api
```

## Source

- Marketplace: https://agentskillexchange.com/skills/wp-abilities-api/
