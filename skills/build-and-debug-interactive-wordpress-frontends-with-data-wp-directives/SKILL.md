---
name: "Build and debug interactive WordPress frontends with data-wp directives"
slug: "build-and-debug-interactive-wordpress-frontends-with-data-wp-directives"
description: "This skill helps an agent create or troubleshoot WordPress Interactivity API behavior, from store wiring to server-rendered state and hydration checks. Use it when a block, theme, or plugin needs directive-driven interactivity rather than ad hoc frontend glue."
verification: "security_reviewed"
source: "https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-interactivity-api"
author: "WordPress Contributors"
publisher_type: "Open Source Project"
category: "WordPress & CMS"
framework: "Multi-Framework"
---

# Build and debug interactive WordPress frontends with data-wp directives

This skill helps an agent create or troubleshoot WordPress Interactivity API behavior, from store wiring to server-rendered state and hydration checks. Use it when a block, theme, or plugin needs directive-driven interactivity rather than ad hoc frontend glue.

## Prerequisites

Node.js; filesystem access; WordPress block tooling; optional WP-CLI

## Installation

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/WordPress/agent-skills.git

Requirements and caveats from upstream:
- node shared/scripts/skillpack-build.mjs --clean
- node shared/scripts/skillpack-install.mjs --global
- node shared/scripts/skillpack-install.mjs --global --skills=wp-playground,wp-block-development

Basic usage or getting-started notes:
- bash
- # Clone agent-skills
- cd agent-skills

- Source: https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-interactivity-api
- Extracted from upstream docs: https://raw.githubusercontent.com/WordPress/agent-skills/HEAD/README.md

## Documentation

- https://github.com/WordPress/agent-skills

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/build-and-debug-interactive-wordpress-frontends-with-data-wp-directives/)
