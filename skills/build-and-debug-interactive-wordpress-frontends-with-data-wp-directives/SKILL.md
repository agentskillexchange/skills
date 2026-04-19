---
title: "Build and debug interactive WordPress frontends with data-wp directives"
description: "This entry is based on the wp-interactivity-api skill from the official WordPress/agent-skills repository. The agent behavior is precise: detect existing Interactivity API usage, identify stores and directives, align server-rendered state with client hydration, and debug why interactive markup is inert or inconsistent. That is a concrete job-to-be-done, not a generic description of a frontend API. Use this when a user wants an agent to build or repair directive-based WordPress interactivity, especially around data-wp-interactive , data-wp-on--* , data-wp-bind--* , viewScriptModule , or @wordpress/interactivity stores. It is the right skill when a block or theme should stay inside WordPress’s intended interactivity model instead of drifting into improvised SPA patterns or brittle event wiring. The scope boundary matters here. This is not a listing for the WordPress framework, the block editor, or a JavaScript package. The skill tells an agent when to inspect directives, when to define state in PHP, when to verify server-side rendering, and how to chase hydration mismatches or missing module loads. Integration points include block.json, viewScriptModule entries, PHP helpers such as wp_interactivity_state() , directive markup in templates, and downstream end-to-end tests once the interactive path is working again."
source: "https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-interactivity-api"
verification: "security_reviewed"
category:
  - "WordPress &amp; CMS"
framework:
  - "Multi-Framework"
---

# Build and debug interactive WordPress frontends with data-wp directives

This entry is based on the wp-interactivity-api skill from the official WordPress/agent-skills repository. The agent behavior is precise: detect existing Interactivity API usage, identify stores and directives, align server-rendered state with client hydration, and debug why interactive markup is inert or inconsistent. That is a concrete job-to-be-done, not a generic description of a frontend API. Use this when a user wants an agent to build or repair directive-based WordPress interactivity, especially around data-wp-interactive , data-wp-on--* , data-wp-bind--* , viewScriptModule , or @wordpress/interactivity stores. It is the right skill when a block or theme should stay inside WordPress’s intended interactivity model instead of drifting into improvised SPA patterns or brittle event wiring. The scope boundary matters here. This is not a listing for the WordPress framework, the block editor, or a JavaScript package. The skill tells an agent when to inspect directives, when to define state in PHP, when to verify server-side rendering, and how to chase hydration mismatches or missing module loads. Integration points include block.json, viewScriptModule entries, PHP helpers such as wp_interactivity_state() , directive markup in templates, and downstream end-to-end tests once the interactive path is working again.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/build-and-debug-interactive-wordpress-frontends-with-data-wp-directives/)
