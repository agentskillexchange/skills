---
name: "Build and debug custom WordPress REST API endpoints with schema and permission guardrails"
slug: "build-and-debug-custom-wordpress-rest-api-endpoints-with-schema-and-permission-guardrails"
description: "Uses the WordPress wp-rest-api skill to help an agent design, register, validate, and troubleshoot custom REST routes without skipping schema, auth, or permission_callback details. This is for agent-led endpoint work in plugins, themes, or core-adjacent codebases, not for browsing the WordPress REST API as a product catalog."
verification: "listed"
source: "https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-rest-api"
author: "WordPress"
publisher_type: "Open Source Project"
category: "WordPress & CMS"
framework: "Multi-Framework"
---

# Build and debug custom WordPress REST API endpoints with schema and permission guardrails

Uses the WordPress wp-rest-api skill to help an agent design, register, validate, and troubleshoot custom REST routes without skipping schema, auth, or permission_callback details. This is for agent-led endpoint work in plugins, themes, or core-adjacent codebases, not for browsing the WordPress REST API as a product catalog.

## Prerequisites

WordPress codebase access, PHP, and optional WP-CLI for verification

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

- Source: https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-rest-api
- Extracted from upstream docs: https://raw.githubusercontent.com/WordPress/agent-skills/HEAD/README.md

## Documentation

- https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-rest-api

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/build-and-debug-custom-wordpress-rest-api-endpoints-with-schema-and-permission-guardrails/)
