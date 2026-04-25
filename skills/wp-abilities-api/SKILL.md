---
title: "WP Abilities API"
description: "Specialized support for defining, exposing, and debugging WordPress abilities through the Abilities API."
verification: "security_reviewed"
source: "https://github.com/WordPress/abilities-api"
category:
  - "WordPress & CMS"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "wordpress/abilities-api"
  github_stars: 202
---

# WP Abilities API

WP Abilities API is a specialist skill for WordPress builders working with wp_register_ability, wp_register_ability_category, /wp-json/wp-abilities/v1/*, and @wordpress/abilities. It focuses on one narrow job: helping teams define abilities cleanly and expose them to clients without falling back to generic WordPress advice. Best for registering WordPress abilities and categories in PHP debugging REST exposure and missing client visibility implementing permission-aware ability checks in JavaScript clients Install notes Install the skill in an OpenClaw workspace that has access to your WordPress plugin, theme, or core checkout. It is most useful in environments targeting WordPress 6.9+ and may also rely on WP-CLI for validation workflows. Source: OpenClaw-compatible WP Abilities API skill.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/wp-abilities-api/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/wp-abilities-api
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/wp-abilities-api`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-abilities-api/)
