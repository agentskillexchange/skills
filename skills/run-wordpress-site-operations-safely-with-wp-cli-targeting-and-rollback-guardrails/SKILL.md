---
name: "Run WordPress site operations safely with WP-CLI targeting and rollback guardrails"
slug: "run-wordpress-site-operations-safely-with-wp-cli-targeting-and-rollback-guardrails"
description: "Uses the WordPress wp-wpcli-and-ops skill to guide an agent through environment-aware WP-CLI work like search-replace, plugin or theme operations, cron inspection, and multisite-safe targeting. It is an operational runbook for guarded WordPress changes, not a plain entry for the WP-CLI product."
verification: "security_reviewed"
source: "https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-wpcli-and-ops"
author: "WordPress"
publisher_type: "Open Source Project"
category: "WordPress & CMS"
framework: "Multi-Framework"
---

# Run WordPress site operations safely with WP-CLI targeting and rollback guardrails

Uses the WordPress wp-wpcli-and-ops skill to guide an agent through environment-aware WP-CLI work like search-replace, plugin or theme operations, cron inspection, and multisite-safe targeting. It is an operational runbook for guarded WordPress changes, not a plain entry for the WP-CLI product.

## Prerequisites

WP-CLI plus access to the target WordPress environment

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

- Source: https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-wpcli-and-ops
- Extracted from upstream docs: https://raw.githubusercontent.com/WordPress/agent-skills/HEAD/README.md

## Documentation

- https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-wpcli-and-ops

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-wordpress-site-operations-safely-with-wp-cli-targeting-and-rollback-guardrails/)
