---
title: "WP Abilities API"
description: "Specialized support for defining, exposing, and debugging WordPress abilities through the Abilities API."
verification: security_reviewed
source: "https://github.com/WordPress/abilities-api"
category:
  - "WordPress &amp; CMS"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "WordPress/abilities-api"
  github_stars: 198
---

# WP Abilities API

WP Abilities API is a specialist skill for WordPress builders working with wp_register_ability, wp_register_ability_category, /wp-json/wp-abilities/v1/*, and @wordpress/abilities. It focuses on one narrow job: helping teams define abilities cleanly and expose them to clients without falling back to generic WordPress advice.

Best for

registering WordPress abilities and categories in PHP
debugging REST exposure and missing client visibility
implementing permission-aware ability checks in JavaScript clients

Install notes
Install the skill in an OpenClaw workspace that has access to your WordPress plugin, theme, or core checkout. It is most useful in environments targeting WordPress 6.9+ and may also rely on WP-CLI for validation workflows.

Source: OpenClaw-compatible WP Abilities API skill.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-abilities-api/)
