---
name: "Run WordPress site operations safely with WP-CLI targeting and rollback guardrails"
description: "Uses the WordPress wp-wpcli-and-ops skill to guide an agent through environment-aware WP-CLI work like search-replace, plugin or theme operations, cron inspection, and multisite-safe targeting. It is an operational runbook for guarded WordPress changes, not a plain entry for the WP-CLI product."
verification: listed
source: "https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-wpcli-and-ops"
category:
  - "WordPress &amp; CMS"
framework:
  - "Multi-Framework"
---

# Run WordPress site operations safely with WP-CLI targeting and rollback guardrails

This entry is based on the official wp-wpcli-and-ops skill from WordPress/agent-skills. The underlying tool is WP-CLI, but the skill is narrower and much more useful than a product card. It gives an agent a concrete operational workflow for running WordPress tasks safely: confirm the environment, verify the right site path and URL, assess blast radius, back up before risky changes, dry-run where possible, and only then perform targeted commands.
A user should invoke this when they want an agent to do real WordPress operations instead of poking around manually in wp-admin or firing off ad hoc shell commands. Typical jobs include safe domain or protocol migrations with wp search-replace, plugin and theme state changes, database export or import, cache and rewrite flushing, cron inspection, and multisite-aware actions that require explicit --url or network targeting. In those situations, the operator behavior matters more than the tool name, because the main risk is hitting the wrong site or making an unreviewed write in production.
The scope boundary is what keeps this from being a generic WP-CLI listing. It is not about explaining every WP-CLI command or advertising the CLI itself. It is specifically about agent-run WordPress operations with deterministic targeting, guardrails, verification, and rollback-aware sequencing. Integration points include wp db *, wp plugin *, wp theme *, cron inspection, multisite flags, wp-cli.yml, and shell or CI automation patterns. The upstream source is official, documented, maintained, and released through the WordPress agent-skills repository, so it passes the evidence and trust thresholds without hand-waving.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-wordpress-site-operations-safely-with-wp-cli-targeting-and-rollback-guardrails/)
