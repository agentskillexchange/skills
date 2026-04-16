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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-abilities-api/)
