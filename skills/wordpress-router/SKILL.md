---
name: WordPress Router
description: Route WordPress tasks to the right workflow fast. Core Capabilities Manage
  WordPress sites using WP-CLI and the WordPress REST API Automate plugin, theme,
  and core update workflows Handle content op
verification: security_reviewed
source: https://github.com/WordPress/WordPress
category:
- WordPress &amp; CMS
framework:
- OpenClaw
tool_ecosystem:
  github_repo: WordPress/WordPress
  github_stars: 21002
---
# WordPress Router

WordPress Router is built around WordPress CMS and REST API ecosystem. The underlying ecosystem is represented by WordPress/WordPress (20,973+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like posts, pages, taxonomies, media, custom fields, auth, plugin hooks and preserving the operational context that matters for real tasks.
In practice, the skill gives an agent a stable interface to wordpress so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Route WordPress tasks to the right workflow fast. The implementation typically relies on posts, pages, taxonomies, media, custom fields, auth, plugin hooks, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses posts, pages, taxonomies, media, custom fields, auth, plugin hooks instead of scraping a UI, which makes runs easier to audit and retry.
Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.
Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.
Fits into broader integration points such as content publishing, plugin dev, REST endpoints, and editorial automation.

 Key integration points include content publishing, plugin dev, REST endpoints, and editorial automation. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wordpress-router/)
