---
name: "WP Abilities API"
description: "Specialized support for defining, exposing, and debugging WordPress abilities through the Abilities API."
category: "WordPress & CMS"
framework: "Custom Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/wp-abilities-api/"
---
# WP Abilities API

Specialized support for defining, exposing, and debugging WordPress abilities through the Abilities API.

WP Abilities API is a specialist skill for WordPress builders working with wp_register_ability, wp_register_ability_category, /wp-json/wp-abilities/v1/*, and @wordpress/abilities. It focuses on one narrow job: helping teams define abilities cleanly and expose them to clients without falling back to generic WordPress advice.



Best for



- registering WordPress abilities and categories in PHP



- debugging REST exposure and missing client visibility



- implementing permission-aware ability checks in JavaScript clients



Install notes

Install the skill in an OpenClaw workspace that has access to your WordPress plugin, theme, or core checkout. It is most useful in environments targeting WordPress 6.9+ and may also rely on WP-CLI for validation workflows.



Source: OpenClaw-compatible WP Abilities API skill.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wp-abilities-api/)
